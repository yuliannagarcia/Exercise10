# Get the directory name from the environment
import os

if 'HOMEPATH' in os.environ:  # Check if running on Windows
    directory = os.environ['HOMEPATH']  # Get the home directory path for Windows
else:  # If not running on Windows (e.g., Linux)
    directory = os.environ['HOME']  # Get the home directory path for Linux

# Construct a portable wildcard pattern
pattern = directory + '/*'  # Create a wildcard pattern for all files in the directory

# Use os.listdir() to obtain the list of filenames
filenames = os.listdir(directory)  # Get a list of filenames in the directory

# Iterate through the filenames
for filename in filenames:
    # Get the full path of each file
    full_path = directory + '/' + filename  # Concatenate directory path with filename to get full path

    # Add a test to only display files that are not zero length
    if os.path.getsize(full_path) > 0:  # Check if file size is greater than 0 bytes
        # Remove the leading directory name(s) from each filename before printing
        base_filename = filename.split('/')[-1]  # Split the full path to extract the filename
        print(base_filename, "-", os.path.getsize(full_path), "bytes")  # Print filename and its size
