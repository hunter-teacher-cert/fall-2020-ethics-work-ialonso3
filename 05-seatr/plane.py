# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:35:43 2020

@author: Izagma
"""

class Seat(object):
    def __init__(self, r, c, value):
        letter = ["a","b","c","d","e","f"]
        self.occupied = False;
        # automatically creates the seat's location from the row & column pair
        self.loc = str(r+1) + letter[c] 
        self.value = value
 
# creates the plane
def make_plane(rows, columns):
  # value defaults to $105
  plane = [[Seat(r,c,105) for c in range(columns)] for r in range(rows)]
  # add correct values by row and column
  return plane

# prints the plane indicating available seats
def print_plane(plane):
  print("-----------------PLANE---------------------")
  # print the plane seats
  for r in range(len(plane)):
    for c in range(len(plane[0])):
      # add two spaces for the aisle
      if c == 3:
        print(" ",end=" ")
      # adjust for smaller row numbers
      if r < 9:
        print("",end=" ")
      print(plane[r][c].loc,end=" ")
      # -- indicates available, XX indicates occupied
      if plane[r][c].occupied:
        print("XX",end=" ")
      else:
        print("--",end=" ")
    print()


# Occupies the specified seat
def occupy_seat(plane,r,c):
  letter = ["a","b","c","d","e","f"]
  for i in range(len(letter)):
    if letter[i] == c:
      column = i
  # Only occupy it if it is free,
  # Otherwise return false
  if plane[r][column].occupied:
    return False
  else:
    plane[r][column].occupied = True
    return True

# main
my_plane = make_plane(20,6)               # make a plane
success = occupy_seat(my_plane,2,"d")     # Occupy 2d
success = occupy_seat(my_plane,11,"f")    # Occupy 11d
success = occupy_seat(my_plane,11,"f")    # try to Occupy 11d again!
if not success:
  print("Seat 11f is already occupied.")
print_plane(my_plane)                     # Print the plane's current Status
