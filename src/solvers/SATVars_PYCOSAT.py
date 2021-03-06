
# modified from https://github.com/palvaro/ldfi-py

# **************************************** #

#############
#  IMPORTS  #
#############
# standard python packages
import pycosat
from types import *
import inspect, os, sys, time

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../.." )
sys.path.append( packagePath )

from utils import tools
# **************************************** #


######################
#  SAT VARS PYCOSAT  #
######################
class SATVars_PYCOSAT :


  ################
  #  ATTRIBUTES  #
  ################
  var2num = None
  num2var = None
  counter = None


  #################
  #  CONSTRUCTOR  #
  #################
  def __init__(self):
    self.var2num = {}
    self.num2var = {}
    self.counter = 1


  ################
  #  LOOKUP VAR  #
  ################
  # given variable, return the integer id
  def lookupVar(self, var):
    print "var = " + str( var )

    if not self.var2num.has_key(var) :

      # assign the id
      if "NOT" in var : # negate id if it's a negative variable
        var = var.replace( "_NOT_", "" ) # cleaning hack for good aesthetics
        self.var2num[var] = int(-1) * self.counter
      else :
        self.var2num[var] = self.counter

      self.num2var[self.counter] = var
      self.counter += 1

    return self.var2num[var]


  ################
  #  LOOKUP NUM  #
  ################
  # given integer id, return the assocated variable
  def lookupNum(self, num):
    if num < 0:
      return "NOT " + self.num2var[-num]
    else:
      return self.num2var[num]


#########
#  EOF  #
#########
