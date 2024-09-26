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

# NOTE: there is a way we could make the return statements
# that are contingent on 'if'/'else' be more terse
# by using ternary, but this (more verbose) way
# is more clear i.e. good for illustrative purposes.

def check_file_existence(file_of_interest: str):

    print('\n Checking for existence of "%s"', file_of_interest)

    does_file_exist: bool = True

    if does_file_exist:
    
        return True

    else:

        print('\n ERROR')
        exit()
    

def check_if_file_is_zero_bytes(file_of_interest: str):
            
    print('\n Checking file length')

    file_length = 999

    if file_length.length > 0:

        return True
    
    else:

        print('\n ERROR')
        exit()


def get_checksum_for_file(file_name: str, file_location: str):

    print('\n Creating checksum for copied file')

    checksum = 999

    if checksum:

        return checksum
    
    else:

        print('\n ERROR')
        exit()
    

def get_file_size(file_of_interest: str, file_location: str):

    print('\n Determing size of file')

    file_size: int = 999

    if file_size:

        return file_size
    
    else:

        print('\n ERROR')
        exit()


# NOTE: this could be three seperate methods or
# grouped as here, as they share a common purpose.
def check_destination_location_is_ready(destination_path: str, size_of_file_of_interest: int):

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
    

def copy_file(file_of_interest: str, destination_location: str):

    print('\n Copying file')

    was_file_copied = True

    copied_file = 'path to/name of new file'

    if (copied_file):

        return copied_file
    
    else: 
        
        print('\n ERROR')
        exit()


def compare_checksums(original_file_checksum, copied_file_checksum):

    print('\n Comparing checksums')

    if original_file_checksum == copied_file_checksum:

        return True
    
    else:
        
        print('\n ERROR')
        exit()


def main():

    # NOTE: as we have our breaking conditions
    # in the methods themselves (i.e. exiting there
    # if something undesirable happens) we can
    # forgo having those checks below (as in my demo),
    # but that doesn't have to be final of course.

    check_file_existence(original_file_name)

    check_if_file_is_zero_bytes(original_file_name)

    original_file_checksum = get_checksum_for_file(original_file_name)

    file_size = get_file_size(original_file_name)

    check_destination_location_is_ready(destination_location, file_size)

    copied_file = copy_file(original_file_name, destination_location)

    copied_file_checksum = get_checksum_for_file(copied_file, destination_location)

    compare_checksums(original_file_checksum, copied_file_checksum)

# NOTE: Here we define some global variables.
# Perhaps ultimately these would be arguments
# passed in to our program, but for now
# we would have to either manually define them
# or simply create them (and not assign values to them),
# so that their values can be assigned here
# as the program runs its course.
original_file_name: str = 'name_of_file_of_interest'
copied_file_name: str
original_file_checksum: str
copied_file_checksum: str
file_size: int
destination_location: str

# Call our main function.
# NOTE: i think we are supposed to use
# some Python convention here and name
# our main function '__main' or something, idk...

# NOTE: this will start our program running
# by calling the 'main()' method defined above.
main()
