import os
def create_directory(directory_path):
    # Check if the directory already exists
    if os.path.exists(directory_path):
        print(f"Directory '{directory_path}' already exists.")
    else:
        try:
            # Create the directory
            os.mkdir(directory_path)
            print(f"Directory '{directory_path}' created successfully.")
        except OSError as error:
            print(f"Failed to create directory '{directory_path}': {error}")

# Specify the directory path you want to create
for i in range(1,46,1):
    new_directory_path = '/Users/june/Desktop/manga/merge_manga/hi_fin/{}/merged'.format(i)
    # Call the function to create the directory
    create_directory(new_directory_path)
