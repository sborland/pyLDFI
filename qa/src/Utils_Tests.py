#!/usr/bin/env python

'''
PyLDFI_TestSuite_.py
  Defines unit tests for utils.
'''

#############
#  IMPORTS  #
#############
# standard python packages
import os, sys, unittest

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../../../src" )
sys.path.append( packagePath )
testPath = os.path.abspath(__file__+"/../../../qa")
from utils import tools, extractors, parseCommandLineInput
# ------------------------------------------------------ #

################
#  UNIT TESTS  #
################
class Utils_Tests( unittest.TestCase ) :


###########
# Tools   #
###########
  def test_bp_tools(self):
    with self.assertRaises(SystemExit) as cm:
      tools.bp("testfile", "testfunc", "testmsg")
    self.assertTrue(cm.exception.code in "BREAKPOINT in file testfile at function testfunc :\n>>> testmsg FAIL") 
  
  def test_getRandomAttName_tools( self ) :
    outputResult = 16
    self.assertEqual( len( tools.getRandomAttName( ) ), outputResult )
    self.assertTrue(tools.getRandomAttName( ).isalpha())
    self.assertTrue(tools.getRandomAttName( ).isupper()) 
  
  def test_getID_tools( self ) :
    outputResult = 16
    self.assertEqual( len( tools.getID( ) ), outputResult )
    self.assertTrue(tools.getID( ).isalpha())
    self.assertTrue(tools.getID( ).islower())
    
  def test_getEvalResults_file_c4_tools(self):
    c4respath = testPath  + "/testfiles/c4dump.txt"
    with self.assertRaises(SystemExit) as cm:
      tools.getEvalResults_file_c4("")
    self.assertTrue(cm.exception.code=="Cannot open file : ")
    dictRes = tools.getEvalResults_file_c4(c4respath)
    self.assertFalse(dictRes['node']==None)
    self.assertFalse(dictRes['pre']==None)
    self.assertFalse(dictRes['post']==None)
    
  def test_checkParentheses_tools( self ) :
    inputArg  = "node(Node, Neighbor)@next :- node(Node, Neighbor) ;"
    outputResult = True
    self.assertEqual( tools.checkParentheses( inputArg ), outputResult )
  
  
  def test_toAscii_list_tools(self):
    unitestfile = testPath + "/testfiles/unicodetest.txt"
    with open(unitestfile,"r") as f:
      line = f.readlines()[0][6:]
      x = 0
      testmulti = []
      while x != 5:      
        testmulti.append(line)
        x= x+1
      self.assertFalse(tools.toAscii_list(testmulti)==None)
    
  
  def test_toAscii_multiList_tools(self):
    unitestfile = testPath + "/testfiles/unicodetest.txt"
    with open(unitestfile,"r") as f:
      line = [f.readlines()[0][6:]]
      x = 0
      testmulti = []
      while x != 5:      
        testmulti.append(line)
        x= x+1
      self.assertFalse(tools.toAscii_multiList(testmulti)==None)
        
  
  def test_toAscii_str_tools(self):
    unitestfile = testPath + "/testfiles/unicodetest.txt"
    with open(unitestfile,"r") as f:
      line = [f.readlines()[0][6:]]
      line = tools.toAscii_str(line)
      self.assertFalse(line.decode('utf-8')==None)
      
  def test_skip_tools(self):
    testline = "\n"
    self.assertTrue(tools.skip(testline)==True)
    testline = "/       "
    self.assertTrue(tools.skip(testline)==True)
    testline = "hello world / !"
    self.assertTrue(tools.skip(testline)==False)

  def test_getAllIncludedFiles_tools(self):
    #Test: base case
    testDict = {"Utils_Tests.py": True}
    self.assertTrue(tools.getAllIncludedFiles(testDict)==testDict)
    #Test: Unable to find file error hit
    testDict = {"FakeFile": False}
    with self.assertRaises(SystemExit) as cm:
      tools.getAllIncludedFiles(testDict)
    self.assertTrue("ERROR" in cm.exception.code)
    #Test: Succesfully finding included files in .ded
    dedtestfile = testPath + "/testfiles/testInclude.ded"
    testDict = {dedtestfile: False}
    self.assertTrue(tools.getAllIncludedFiles(testDict)==testDict)
    
  def test_combineLines_tools(self):
    testList = [["Hello"],["World","!"],["!"]]
    self.assertTrue(tools.combineLines(testList)=="HelloWorld!!")
    
  def test_attSearchPass2_tools(self):
    testList = "datalog,Rule,THISISAWILDCARDNFDEICZANGTPSRFE,Hello,\
    THISISAWILDCARDCATDOGANEUXLFEVN,World"
    outputList = ["THISISAWILDCARDNFDEICZANGTPSRFE",
    "THISISAWILDCARDCATDOGANEUXLFEVN"]
    self.assertTrue(len(tools.attSearchPass2(testList))==2)
    self.assertTrue(tools.attSearchPass2(testList)==outputList)
    
  def test_isString_tools(self):
    testVar = "'String'"
    self.assertTrue(tools.isString(testVar)==True)
    testVar = '"String"'
    self.assertTrue(tools.isString(testVar)==True)
    testVar = '9'
    self.assertTrue(tools.isString(testVar)==False)
    
  def test_isInt_tools(self):
    testVar = "!!!!"
    self.assertTrue(tools.isInt(testVar)==False)
    testVar = '"String"'
    self.assertTrue(tools.isInt(testVar)==False)
    testVar = '123456789'
    self.assertTrue(tools.isInt(testVar)==True)
    
##############
# Extractors #
##############
  def test_isLastItem_extractors(self):
    self.assertTrue(extractors.isLastItem(9,10)==True)
    self.assertTrue(extractors.isLastItem(8,10)==False)
    
  def test_extractAdditionalArgs_extractors( self ) :
    inputArg  = [ 'notin', 'node', '(', 'Node', ',', 'Neighbor', ')' ]
    outputResult = ['notin']
    self.assertEqual( extractors.extractAdditionalArgs( inputArg ), outputResult )

  def test_extractGoal_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', '@', 'next', ':-', 'node', '(', 'Node', ',', 'Neighbor', ')', ';' ]
    outputResult = [ 'node', '(', 'Node', ',', 'Neighbor', ')', '@', 'next' ]
    self.assertEqual( extractors.extractGoal( inputArg ), outputResult )

  def test_isEqn_extractors(self):
    testString = "Hello World!"
    testArr = [ "1+1", "45-asd", "   *", "asdf/", ">1", "2<", "<=",\
    ">=", "5==5", "2345!=965" ]
    self.assertTrue(extractors.isEqn(testString)==False)
    for item in testArr:
      self.assertTrue(extractors.isEqn(item)==True)	
  
  def test_hasOp_extractors(self):
    testString = "Hello World!"
    testArr = [ "1+1", "45-asd", "   *", "asdf/", ">1", "2<", "<=",\
    ">=", "5==5", "2345!=965" ]
    self.assertTrue(extractors.hasOp(testString)==False)
    for item in testArr:
      self.assertTrue(extractors.hasOp(item)==True)	

  def test_extractSubgoalList_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', '@', 'next', ':-', 'node', '(', 'Node', ',', 'Neighbor', ')' ]
    outputResult = ['node(Node,Neighbor)'] 
    self.assertEqual( extractors.extractSubgoalList( inputArg ), outputResult )

  def test_extractTimeArg_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', '@', 'next' ]
    outputResult = "next"
    self.assertEqual( extractors.extractTimeArg( inputArg ), outputResult )

  def test_extractAttList_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', ';' ]
    outputResult = [ 'Node', 'Neighbor' ]
    self.assertEqual( extractors.extractAttList( inputArg ), outputResult )

  def test_extractSubgoalName_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', ';' ]
    outputResult = ["node"]
    self.assertEqual( extractors.extractSubgoalName( inputArg ), outputResult )

  def test_extractName_extractors( self ) :
    inputArg  = [ 'node', '(', 'Node', ',', 'Neighbor', ')', ';' ]
    outputResult = "node"
    self.assertEqual( extractors.extractName( inputArg ), outputResult )



#########################
#  THREAD OF EXECUTION  #
#########################
# use this main if running this script exclusively.
if __name__ == "__main__" :
  unittest.main( verbosity=2 )


#########
#  EOF  #
#########
