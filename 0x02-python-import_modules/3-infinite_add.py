#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
  args = sys.argv[1:]
  
  #cast arguments into integers
  int_args = [int(arg) for arg in args]
  
  #calculate the result of the addition
  result = sum (int_args)
  
  print(result)
