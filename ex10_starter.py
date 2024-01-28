import sys, glob, os

# Get the directory name
if sys.platform == 'win32':  # Check if the platform is Windows
    hdir = os.environ['HOMEPATH']  # Get the home directory path for Windows
else:  # If the platform is not Windows (e.g., Linux)
    hdir = os.environ['HOME']  # Get the home directory path for Linux

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')  # Create a wildcard pattern for all files in the directory

# Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)  # Get a list of filenames in the directory matching the pattern

# Use os.path.getsize to find each file's size and display non-zero length files
for filename in filenames:
    file_size = os.path.getsize(filename)  # Get the size of each file
    if file_size > 0:  # Check if the file size is greater than 0 bytes
        base_filename = os.path.basename(filename)  # Remove the leading directory name(s) from each filename
        print(base_filename, "-", file_size, "bytes")  # Print filename and its size

