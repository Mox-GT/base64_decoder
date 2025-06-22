## Decode any base64 input (into printable ASCII characters)
## This is a skeleton, NOT functional YET
## UPDATE: now functional

import base64
import binascii
import textwrap


# Take user's input + prompt for said input
print("Hey! Input your base64, and I'll decode it into ASCII.")
user_input = input()

# Function to decode the user's input into a variable
def decode_input(user_input): 
    try:
        decoded_input = base64.standard_b64decode(user_input)
        print("\n")
        print(textwrap.fill("Worked! Here's your input in ASCII."), "\n")
        print(base64.standard_b64decode(user_input), "\n")


    # If input is incorrectly padded
    except binascii.Error: 
        print("\n")
        print(textwrap.fill("The input may be 'incorrectly padded'."), "\n")
        print(textwrap.fill("Which means your input may not be 'proper' base64. Recheck its formatting before you retry.", width=40), "\n")

decode_input(user_input)
