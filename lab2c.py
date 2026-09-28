
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: September 25th, 2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py
# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
str1=input("Enter a Sentence: ")
str2=input("Enter Another Sentence: ")
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
if len(str1) > len(str2):
    print(f"{str1} is longer than {str2}")
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user
elif len(str1) < len(str2):
    print(f"{str2} is longer than {str1}")
else:
    print(f"{str1} and {str2} are equal.")




