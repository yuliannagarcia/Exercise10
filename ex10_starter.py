import sys, glob, os

# Get the directory name
if sys.platform == 'win32':  # Check if the platform is Windows
    hdir = os.environ['HOMEPATH']  # Get the home directory path for Windows
else:  # If the platform is not Windows (e.g., Linux)
    hdir = os.environ['HOME']  # Get the home directory path for Linux

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')  # Create a wildcard pattern for all files in the directory

# Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)  # Get a list of filenames in the directory matching the pattern

# Use os.path.getsize to find each file's size and display non-zero length files
# iterates through the list of filenames obtained from glob.glob()
for filename in filenames:
    # for each filename, os.path.getsize() gets the size of the file
    file_size = os.path.getsize(filename)
    if file_size > 0:  # checks if the file size is bigger than 0 bytes, and if so, it prints the filename and its
        # size.
        base_filename = os.path.basename(filename)  # removes the leading directory name(s) from each filename before
        # printing, so only the filename is displayed
        print(f"{base_filename} - {file_size} bytes")  # Print filename and its size
