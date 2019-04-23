from colorama import init
init()
from colorama import Fore, Back, Style 
import sys
import math
import random

n=10
total_wumpus=math.floor(n/(n/2))
print("Total wumpus=")
print(total_wumpus)
total_pit=math.floor(n/2)
wumpus=[]
pit=[]
randoms=[]

def printRed():{
    print(Back.RED+ '   ')
}
def printGreen():
    sys.stdout.write(Back.GREEN+ '   ')

def printblue():
    sys.stdout.write(Back.BLUE+ '   ')

def printYellow():{
    sys.stdout.write(Back.YELLOW+ '   ')
}
def printPlayer(row,column):
  for i in range(0,n-1,1):
    for j in range(0,n-1,1):
      if(i==row and j==column):
        print("0") 

def printDice(row,column):
  i_t=0
  j_t=1
  for i in range(0,n-1,1):
    for j in range(0,n-1,1):
      if(row==j and column==i):
        if(j % 2 == i_t):
          sys.stdout.write(Back.GREEN+ ' 0 ')
        else:
          sys.stdout.write(Back.BLUE+ ' 0 ')
      elif(j % 2 == i_t):
        printGreen()
      else:
        printblue()
    k=j_t
    j_t=i_t
    i_t=k
    print("")

def printWumpus(row,column,row1,column1):
  i_t=0
  j_t=1
  for i in range(0,n,1):
    for j in range(0,n,1):
      if((row==j and column==i) or (row1==j and column1==i)):
        if(j % 2 == i_t):
          sys.stdout.write(Back.GREEN+ ' 0 ')
        else:
          sys.stdout.write(Back.BLUE+ ' 0 ')
      elif(j % 2 == i_t):
        printGreen()
      else:
        printblue()
    k=j_t
    j_t=i_t
    i_t=k
    print("")

def add_wumpus():
  present=0
  x=random.randint(0,n-1)
  y=random.randint(0,n-1)
  if(wumpus==[]):
    wumpus.append([x,y])
  else:
    for i in wumpus:
      if(i[0]==x-1 or i[0]==x+1 or i[0]==x):
        if(i[1]==y-1 or i[1]==y+1 or i[1]==y):
          present=1
          add_wumpus()
          break
    if(present==0):
      wumpus.append([x,y])

def add_wumpuses():
  for i in range(0,total_wumpus):
    add_wumpus()

printDice(0,0)
add_wumpuses()







