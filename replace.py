#!/bin/python3

# Find: [^\S\r\n]+\n
# Replace: \n

import sys

if len(sys.argv) != 2:
    print("incorrect number of program arguments, expected: 1: file path")
    sys.exit(1)

FILE_PATH = sys.argv[1]
with open(FILE_PATH, "r") as file:
    data = file.read().splitlines()
for i in range(len(data)):
    data[i] = data[i].rstrip()
with open(FILE_PATH, "w") as file:
    file.write("\n".join(data))

