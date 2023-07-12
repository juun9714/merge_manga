import os

def rename_files(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)
    
    # Sort the file list in ascending order
    sorted_files = sorted(file_list)
    sorted_files.pop(-1)
    print(sorted_files)
    # Iterate over the sorted files and rename them
    for i, filename in enumerate(sorted_files):
        # Get the file extension
        _, extension = os.path.splitext(filename)
        
        # Create the new filename with a numeric prefix
        new_filename = f"{i+1}{extension}"
        
        # Construct the full paths for the old and new filenames
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        print(f"Renamed: {filename} -> {new_filename}")

# Specify the directory path where the files are located
for i in range(2,28,1):
    directory_path = 'C:/Users/user/Downloads/FA/{}'.format(i)
    # Call the function to rename files
    rename_files(directory_path)
# rename_files("/Users/june/Desktop/manga/merge_manga/hi_fin/6")