import sys
import os

encrypted_path = sys.argv[1]

def rename_files():

    file_list = os.listdir(encrypted_path)
    os.chdir(r"/Users/evanmoore/workspace/udacity/secret-message/prank")
    for file_name in file_list:
        print ("Old Name: " + file_name)
        print ("New Name: " + file_name.translate(None, '1234567890'))
        os.rename(file_name, file_name.translate(None, '1234567890'))

rename_files()
