import sys
import os

# Make a list of all the files in the specified path
encrypted_path = sys.argv[1]
file_list = os.listdir(encrypted_path)

# Iterate over each file
    # remove the numbers from the filename
    # save the new file name
