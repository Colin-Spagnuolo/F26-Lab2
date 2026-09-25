# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Colin Spagnuolo
# Date:September 25th, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys
num_args= len(sys.argv)-1
if num_args<2:
    print("This script requires exactly two arguments. No argumnets were provided!")
else:
    if num_args==2:
        print(f"Hello user, good job, you provided two arguments!!")
    else:
        print(f"this script requires exactly two arguments. You provided {num_args} arguments!")