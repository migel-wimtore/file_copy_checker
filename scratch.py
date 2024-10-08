# NOTE: this is a totally non functional
# but hopefully helps us think of how
# we might approach our task.
# Any variable assignment done in these
# methods is to show where something would
# need to have a value (determining that value
# will be down to us as we go).
# For illustrative purposes and/or to
# stop the Python interpreter from complaining
# i assigned these variables either 'True' or '999'.

# NOTE: there are many ways we could do this;
# the structure represented here is just
# to hopfully get our heads in the right space
# and is in no way intended to be final.
# Anything is game for changing!

# NOTE: this program flow assumes we are 
# checksumming and copying a single file,
# not a directory.

# NOTE: there is a way we could make the return statements,
# that are contingent on 'if'/'else', be more terse
# by using ternary but here i use the (more verbose) way
# which is more clear i.e. good for illustrative purposes.

#SUZY EDITS, you'd never guess shes got no clue whats shes doing#
import os
import sys
from pathlib import Path

def check_file_exists() 
    my_file = Path("/path/to/file")
    #identify file or directory

print ("Checking for the exsistence of" my_file)

if my_file.exists( ):
    # file or directory exists
    print("True")
    else print ("False")

def file_is_zero_bytes()
    print ("Checking File Size")

    file_size = sys.getsizeof(my_file)
      while file_size > 0
        if file_size = 0
            continue
        print("File size:", file_size, "bytes")
        
##END OF SUZY EDITS, see you all next month!##


def check_file_exists(file_path: str) -> bool:

    print('\n Checking for existence of "' + file_path + "'")

    does_file_exist: bool = True

    if does_file_exist:
    
        return True

    else:

        print('\n ERROR')
        exit()
    

def check_if_file_is_zero_bytes(file_path: str) -> bool:
            
    print('\n Checking file length')

    file_length = 999

    if len(file_length) > 0:

        return True
    
    else:

        print('\n ERROR')
        exit()


def get_file_size(file_path: str) -> int:

    print('\n Determing size of file')

    size: int = 999

    if len(size) > 0:

        return size
    
    else:

        print('\n ERROR')
        exit()
        

def get_checksum_for_file(file_path: str) -> str:

    print('\n Creating checksum for copied file')

    checksum = '999'

    if checksum:

        return checksum
    
    else:

        print('\n ERROR')
        exit()    


# NOTE: this could be three seperate methods or
# grouped as here, as they share a common purpose.
def check_destination_is_ready(size_of_file_of_interest: int, destination_directory_path: str, ) -> bool:

    print('\n Checking destination is mounted')

    is_destination_mounted: bool = True

    print('\n Checking have write access to destination')

    is_there_write_access: bool = True

    print('\n Checking enough space on destination')

    is_there_enough_free_space: bool = True

    if is_destination_mounted and is_there_write_access and is_there_enough_free_space:

        return True
    else:

        print('\n ERROR')
        exit()
    

def copy_file(source_file_path: str, destination_directory_path: str) -> bool:

    print('\n Copying file...')

    was_file_copied = True

    if (was_file_copied):

        return True
    
    else: 
        
        print('\n ERROR')
        exit()


def compare_checksums(original, copied) -> bool:

    print('\n Comparing checksums...')

    if copied == original:

        return True
    
    else:
        
        print('\n ERROR')
        exit()


def main():

    # NOTE: Here we define some variables.
    # Ultimately these could be arguments
    # passed in to our program, but for now
    # we have to manually assign them.
        
    name_of_file_to_be_copied: str = 'name_of_file_of_interest'
    source_path: str = '/my/source/'
    destination_path: str = '/my/destination/'

    
    # NOTE: as we have our breaking conditions
    # in the methods themselves (i.e. exiting there
    # if something undesirable happens) we can
    # forgo having those checks below (as we had it earlier),
    # but that doesn't have to be final of course.

    # NOTE: below you see we use the plus symbol to combine
    # two variables and pass them into some of the functions as one.
    # In these cases it handily makes a single string consisting of
    # the path and file name, which makes our absolute file path.

    check_file_exists(source_path + name_of_file_to_be_copied)

    check_if_file_is_zero_bytes(source_path + name_of_file_to_be_copied)

    file_size = get_file_size(source_path + name_of_file_to_be_copied)

    check_destination_is_ready(file_size, destination_path)

    original_file_checksum = get_checksum_for_file(source_path + name_of_file_to_be_copied)

    copy_file(source_path + name_of_file_to_be_copied, destination_path)

    copied_file_checksum = get_checksum_for_file(destination_path + name_of_file_to_be_copied)

    compare_checksums(original_file_checksum, copied_file_checksum)


# NOTE: this will start our program running
# by calling the 'main()' method defined above.

# NOTE: i think we are supposed to use
# some Python convention here and name
# our main function '__main' or something, idk...

# Run.
main()
