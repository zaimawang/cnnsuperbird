# os is a library that gives us the ability to make OS changes
import os


def increment_file_numbers(directory, string, integer):
    # iterate over every file name in the directory
    print (directory)
    file_number = startcount
    for file_name in os.listdir(directory):
        file_number = file_number + 1
        extension = ".jpg"
        file_name2 = objectname+"."
        # example format : bird.01.jpg
        new_file_name = '%s/%s%02d%s' % (directory, file_name2, file_number, extension)
        old_file_name = '%s/%s' % (directory, file_name)
        print (old_file_name)
        print (new_file_name)
        # rename the file!
        os.rename(old_file_name, new_file_name)


# This is the path to the files
# C:\Users\ACER\Downloads\google-images-download-master\bird
PATH = os.path.abspath('/Users/ACER/Downloads/google-images-download-master/bird')
objectname = "bird"
startcount = 0

# Let's rename the files
increment_file_numbers(PATH, objectname, startcount)
