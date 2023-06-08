#!/usr/bin/env python3
if __name__ == "__main__":
import sys

args = sys.argv[1:]
int_args = [int(arg) for arg in args]
total = sum(int_args)
print(total)
