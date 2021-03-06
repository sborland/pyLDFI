#!/usr/bin/env python

'''
newProgGenerationTools.py
  code for building new datalog programs 
  given a previously determined solution set.
'''

# **************************************** #

#############
#  IMPORTS  #
#############
# python packages
import inspect, os, sys, time
from types import *

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../.." )
sys.path.append( packagePath )

from utils import dumpers, tools

# **************************************** #

ITER_COUNT = None
DEBUG      = True


####################
#  BUILD NEW PROG  #
####################
def buildNewProg( solnSet, irCursor, iter_count ) :

  if DEBUG :
    print "...running buildNewProg..."

  ITER_COUNT = iter_count

  if iter_count == 1 :
    print "ITER_COUNT = " + str( ITER_COUNT )

  newProgSavePath = None  # initialize as None to trigger later sanity check in the event of failure

  ##############################################
  # check if program save directory exists
  testpath        = os.path.abspath( __file__ + "/../.." ) + "/evaluators/programFiles/"
  newProgSavePath = os.path.abspath( __file__ + "/../.." ) + "/evaluators/programFiles/" + "c4program.olg"

  if os.path.isdir( testpath ) :
    pass
  else :
    tools.bp( __name__, inspect.stack()[0][3], "FATAL ERROR1: directory for storing datalog programs does not exist:\n" + testpath + "\nThat's pretty weird. Aborting... " )

  # save the old program
  oldprogpath = None
  if os.path.isfile( newProgSavePath ) :
    oldprogpath = newProgSavePath + "_saved_" + str(time.strftime("%d-%m-%Y")) + "_" + str(time.strftime("%H"+"hrs-"+"%M"+"mins-"+"%S" +"secs" ) ) + "_" + str( iter_count )
    os.system( "mv " + newProgSavePath + " " + oldprogpath )

  ##############################################

  # need to pick one of the solutions
  #print "solnSet = " + str( solnSet )
  preferredSoln = getPreferredSoln( solnSet, irCursor )

  # case no preferred soln exists
  if not preferredSoln :
    return ( newProgSavePath, None )

  # ----------------------------------------- #
  # parse clock soln records
  parsedClockRecords = parseClock( preferredSoln )

  # reset clock.
  # flip the inclusion of clock records (simInclude) in the solution from 'True' to 'False' 
  # and ensure all other clock records are 'True' wrt the inclusion attribute (simInclude).
  setNewClock( parsedClockRecords, irCursor )

  # ----------------------------------------- #
  # build new clock configuration

  if DEBUG :
    print ">> CLOCK DUMP before <<"
    dumpers.clockDump( irCursor )

  # falsify the appropriate record(s)
  shootClockRecs( parsedClockRecords, irCursor )

  if DEBUG :
    print ">> CLOCK DUMP after <<"
    dumpers.clockDump( irCursor )

  # ----------------------------------------- #
  # build a copy of the old program, minus the clock fact lines
  copyProg( oldprogpath, testpath, newProgSavePath ) # edits the new program file directly

  # add the new clock lines.
  finalizeNewProg( testpath, newProgSavePath, irCursor )

  ##############################################

  # sanity checks are good for the soul  ~(^.^)~
  if newProgSavePath :
    #print "preferredSoln = " + str( preferredSoln )
    return ( newProgSavePath, preferredSoln )
  else :
    tools.bp( __name__, inspect.stack()[0][3], "FATAL ERROR: failed to write new program to " + newProgSavePath )


######################
#  SHOOT CLOCK RECS  #
######################
def shootClockRecs( parsedClockRecords, irCursor ) :

  # flip all the simIncludes to True to reset to newest clock soln configuration
  simInclude = "True"
  irCursor.execute( "UPDATE Clock SET simInclude='" + simInclude + "'" )

  # flip the simIncludes for the target clock records
  simInclude = "False"
  for rec in parsedClockRecords :
    src       = rec[0]
    dest      = rec[1]
    sndTime   = rec[2]
    delivTime = rec[3]

    # optimistic by default
    qSRC       = "src=='" + src + "'"
    qDEST      = " AND dest=='" + dest + "'"
    qSNDTIME   = " AND sndTime==" + sndTime + ""
    qDELIVTIME = " AND delivTime==" + delivTime + ""

    # erase query components as necessary
    # EXISTING BUG TODO : does not work if _ in src --> need to handle ANDs more intelligently
    if "_" in src :
      qSRC = ""
    if "_" in dest :
      qDEST = ""
    if "_" in sndTime :
      qSNDTIME = ""
    if "_" in delivTime :
      qDELIVTIME = ""

    # set query
    query = "UPDATE Clock SET simInclude='" + simInclude + "' WHERE " + qSRC + qDEST + qSNDTIME + qDELIVTIME

    if DEBUG :
      print "query = " + str(query)

    # execute query
    irCursor.execute( query )


########################
#  GET PREFERRED SOLN  #
########################
# solnSet is an array
# pick the first soln containing only clock facts
# returns a list of one or more clock facts
def getPreferredSoln( solnSet, irCursor ) :

  solnChoice = None

  for aSoln in solnSet :
    if aSoln == [] : # skip empties
      pass

    # grab the first soln containing only clock facts
    valid = True
    for var in aSoln :
      if not "clock(" in var :
        valid = False
    if valid :
      solnChoice = aSoln
      break

  if solnChoice :
    dataList = parseClock( solnChoice )
    dataList = dataList[0]
    if "_" in dataList :
      # get all corrsponding clock facts
      src       = dataList[0]
      dest      = dataList[1]
      sndTime   = dataList[2]
      delivTime = dataList[3]

      # optimistic by default
      qSRC       = "src=='" + src + "'"
      qDEST      = " AND dest=='" + dest + "'"
      qSNDTIME   = " AND sndTime==" + sndTime + ""
      qDELIVTIME = " AND delivTime==" + delivTime + ""

      # erase query components as necessary
      # EXISTING BUG TODO : does not work if _ in src --> need to handle ANDs more intelligently
      if "_" in src :
        qSRC  = ""
      if "_" in dest :
        qDEST = ""
      if "_" in sndTime :
        qSNDTIME = ""
      if "_" in delivTime :
        qDELIVTIME = ""

      # set query
      query = "SELECT src,dest,sndTime,delivTime FROM Clock WHERE " + qSRC + qDEST + qSNDTIME + qDELIVTIME

      if DEBUG :
        print "query = " + str(query)

      # execute query
      irCursor.execute( query )
      solnList = irCursor.fetchall()
      solnList = tools.toAscii_multiList( solnList )

      # format solns
      solnChoice = []
      for soln in solnList :
        soln = [ str(i) for i in soln ] # convert all data to strings
        atts = ",".join(soln)
        solnChoice.append( "clock([" + atts + "])" )

  return solnChoice


#################
#  PARSE CLOCK  #
#################
def parseClock( preferredSoln ) :

  parsedFacts = []

  for clockFact in preferredSoln :
    fact = getContents( clockFact )
    fact = fact.split( "," )
    parsedFacts.append( fact )

  return parsedFacts


##################
#  GET CONTENTS  #
##################
# extract the data from the clock fact
def getContents( clockFact ) :

  openParen   = None
  closedParen = None
  for i in range(0,len(clockFact)) :
    if clockFact[i] == "(" :
      openParen = i
    elif clockFact[i] == ")" :
      closedParen = i

  return clockFact[ openParen+2:closedParen-1 ]


###################
#  SET NEW CLOCK  #
###################
def setNewClock( parsedClockRecords, irCursor ) :

  # flip all the simIncludes to True
  simInclude = "True"
  irCursor.execute( "UPDATE Clock SET simInclude='" + simInclude + "'" )

  # flip the simIncludes for the target clock records
  simInclude = "False"
  for rec in parsedClockRecords :
    src       = rec[0]
    dest      = rec[1]
    sndTime   = rec[2]
    delivTime = rec[3]

    # optimistic by default
    qSRC       = "src='" + src + "'"
    qDEST      = " AND dest='" + dest + "'"
    qSNDTIME   = " AND sndTime='" + sndTime + "'"
    qDELIVTIME = " AND delivTime='" + delivTime + "'"

    # erase query components as necessary
    if "__WILDCARD__" in src :
      qSRC = ""
    if "__WILDCARD__" in dest :
      qDEST = ""
    if "__WILDCARD__" in sndTime :
      qSNDTIME = ""
    if "__WILDCARD__" in delivTime :
      qDELIVTIME = ""

    # set query
    query = "UPDATE Clock SET simInclude='" + simInclude + "' WHERE " + qSRC + qDEST + qSNDTIME + qDELIVTIME 

    # execute query
    irCursor.execute( query )

    # update crash table
    # (using the long way because the sql statements were tempermental)
    # (easy future update: make this less clunky)

    # grab all the dropped clock facts
    irCursor.execute( "SELECT src,dest,sndTime,delivTime,simInclude FROM Clock WHERE simInclude=='False'" )
    clockTable = irCursor.fetchall()
    clockTable = tools.toAscii_multiList( clockTable )

    # grab the entire contents of crash
    irCursor.execute( "SELECT src,dest,sndTime,delivTime,simInclude FROM Crash" )
    crashTable = irCursor.fetchall()
    crashTable = tools.toAscii_multiList( crashTable )

    # if the dropped clock fact does not already exist in crash table,
    # then add the fact to crash table.
    for row in clockTable :
      if not row in crashTable :
        src        = row[0]
        dest       = row[1]
        sndTime    = row[2]
        delivTime  = row[3]
        simInclude = row[4]
        irCursor.execute( "INSERT INTO Crash (src,dest,sndTime) VALUES ('" + src + "','" + dest + "','" + str(sndTime) + "')" )


###############
#  COPY PROG  #
###############
def copyProg( oldProgPath, testpath, newProgPath ) :

  programLines = []

  # copy old program, except for clock lines
  if os.path.isfile( oldProgPath ) :
    outfile = open( oldProgPath, "r" )
    programLines = outfile.readlines()
    outfile.close()
  else :
    sys.exit( "FATAL ERROR: cannot open old C4 Overlog program at : " + oldProgPath )

  # assumes program is formatted as a single line of concatenated program statements (may be c4 specific)
  #programLines = programLines[0].split( ";" )

  newProgLines = []
  for line in programLines :
    if not line.startswith( "clock(" ) :
      newProgLines.append( line )

  #newProg = "; ".join( newProgLines ) # <--- use this if program formatted as a series of concatenated lines.
  newProg = "".join( newProgLines ) # <--- use this if lines are delimited by carriage returns.

  ##############################################
  # save the new c4 program
  # repetition is redundant, but very reassuring.
  if programLines :
    if os.path.isdir( testpath ) :
      outfile = open( newProgPath, "w" )
      outfile.write( newProg )
      outfile.close()
    else :
      sys.exit( "FATAL ERROR: directory for saving C4 Overlog program does not exist at : " + testpath )
  else :
    sys.exit( "FATAL ERROR: no old program specified. Aborting..." )
  ##############################################


#######################
#  FINALIZE NEW PROG  #
#######################
# build the final version of the new program with the new clock fact configuration
def finalizeNewProg( testpath, newProgSavePath, irCursor ) :

  # get all clock facts where simInclude == True
  irCursor.execute( "SELECT src,dest,sndTime,delivTime FROM Clock WHERE simInclude=='True'" )
  res = irCursor.fetchall()
  res = tools.toAscii_multiList( res )

  # copy all True clock facts into the new program
  newClockFacts = []
  for data in res :
    src       = data[0]
    dest      = data[1]
    sndTime   = data[2]
    delivTime = data[3]
    # replace any single quotes with double quotes
    src  = src.replace(  '"', "'" )
    dest = dest.replace( '"', "'" )
    newClockLine = 'clock("' + src + '","' + dest + '",' + str( sndTime ) + "," + str( delivTime ) + ") ;\n"
    newClockFacts.append( newClockLine )

  # concatenate all clock facts into a single line
  newClockLines = None
  newClockLines = "".join( newClockFacts )
  if not newClockLines :
    tools.bp( __name__, inspect.stack()[0][3], "ERROR: no new clock configurations to explore." )

  ##############################################
  # save the new c4 program
  # repetition is redundant, but very reassuring.
  if os.path.isdir( testpath ) :
    outfile = open( newProgSavePath, "a" )
    # appends to end of last line -> may mess with the correctness 
    # in copyProg wrt the assumption that the program exists as a single line
    outfile.write( newClockLines )
    outfile.close()
  else :
    sys.exit( "FATAL ERROR2: directory for saving C4 Overlog program does not exist: " + testpath )
  ##############################################

  if ITER_COUNT == 1 :
    os.system( "cat " + newProgSavePath )
    sys.exit()

#########
#  EOF  #
#########
