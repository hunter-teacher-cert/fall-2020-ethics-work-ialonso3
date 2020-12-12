# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 05:27:12 2020

@author: Izagma Alonso & Tsee Lee
"""
import random
from colorama import Back, Style

# constants
MAXPOPULATION = 99
NUM_ROWS = 3
NUM_COLS = 6
NUM_DISTRICTS = 6
# Global variables
purple_state=[[]]
popSums = [0] * (NUM_DISTRICTS+1)   # We start at 1, not 0

class Cell(object):   
    def __init__(self, population, district, vote):
        self.population = population
        self.district = district
        self.vote = vote

def totalPop():
  global purple_state
  total = 0
  for i in range(NUM_ROWS):
    for j in range(NUM_COLS):
      total += purple_state[i][j].population
  return total

def displayState():
  global purple_state
  """
  colors = [x for x in dir(Fore) if x[0] != "_"]
  for color  in colors:
    print(color + " " + f"{color}")
  """
  print()
  print(f"\t\t\t{Back.MAGENTA} Purple State {Style.RESET_ALL}")
  print(f"{Back.MAGENTA}")
  for i in range(1, NUM_COLS+1):
    print("D Pp V",end="\t")
  print(f"{Style.RESET_ALL}")
  
  for i in range(NUM_ROWS):
    # print(i,end="\t")
    
    if i % 2 == 0:
      start = 0
      end = NUM_COLS
      change = 1
    else:
      start = NUM_COLS-1
      end = -1
      change = -1

    for j in range(start,end,change):
        if purple_state[i][j].population < 10:
            separate=" "
        else:
            separate=""
        print(purple_state[i][j].district, 
              str(purple_state[i][j].population)+separate, 
              purple_state[i][j].vote, end="\t")
      
    print()
    

def oldDisplayState():
  global purple_state
  print("Purple State:")
  for i in range(NUM_ROWS):
    print(i,end="\t")
    for j in range(NUM_COLS):
      print(purple_state[i][j].district, purple_state[i][j].population, purple_state[i][j].vote, end=",\t")
    print()


def simpleDistricts():
  global prple_state
  districtCells = NUM_ROWS * NUM_COLS / NUM_DISTRICTS
  distNum = 1
  numCells = 0

  for i in range(NUM_ROWS):
    for j in range(NUM_COLS):
      purple_state[i][j].district = distNum
      numCells += 1
      if numCells >= districtCells:
        distNum += 1
        numCells = 0
        
def printPopSums():
    global popSums
    targetPop = totalPop() / NUM_DISTRICTS
    print()
    print(f"{Back.MAGENTA}Target Population:{Style.RESET_ALL} ", int(targetPop))
    print()
    print(f"{Back.MAGENTA}District Population{Style.RESET_ALL}")
    for i in range(1, NUM_DISTRICTS+1):
        print("\t",i,"\t\t",popSums[i])

"""
def updateVars(distNum,addPop,addCells):
    global purple_state
    global numCells,popSum
    purple_state[i][j].district = distNum
    # popSum = addPop + purple_state[i][j].population
    numCells = addCells + 1
    return popSum + addPop
"""
        
def incDistSaveSums(distNum,popSum):
    global popSums
    popSums[distNum]=popSum
    if distNum < NUM_DISTRICTS:        
          distNum += 1
    return distNum    
    
def makeDistricts():
  global purple_state
  global popSums, popSum, numCells
  targetPop = totalPop() / NUM_DISTRICTS
  districtCells = NUM_ROWS * NUM_COLS / NUM_DISTRICTS
  # popSums = [None] * (NUM_DISTRICTS+1)   # We start at 1, not 0
  popSum = 0
  numCells = 0
  distNum = 1
  over = False

  for i in range(NUM_ROWS):
    for j in range(NUM_COLS):
      if ((over and
           popSum + purple_state[i][j].population >= targetPop)
           or (numCells >= districtCells +1)):
        over = False
        distNum = incDistSaveSums(distNum,popSum)
        purple_state[i][j].district = distNum
        popSum = purple_state[i][j].population
        numCells = 1
      else:
        purple_state[i][j].district = distNum
        popSum += purple_state[i][j].population
        numCells += 1
        if ((popSum >= targetPop)
             or (numCells >= districtCells +1)):
          over = True
          distNum = incDistSaveSums(distNum,popSum)
          popSum = 0
          numCells = 0
  # Update the last sum for the last district
  popSums[NUM_DISTRICTS] += popSum
           
def create_state():
    global purple_state
    purple_state = [[ 
        Cell(random.randint(1,MAXPOPULATION),  # population
             1,                                # district
             random.randint(0,1))              # vote: 0 or 1
        for i in range(NUM_COLS) ] 
          for j in range(NUM_ROWS) ]

# main
create_state()
#simpleDistricts()
makeDistricts()
displayState()
printPopSums()



