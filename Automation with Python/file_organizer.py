import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = filename.split('.')[-1]
            
            # Create a directory for the file extension if it doesn't exist
            if not os.path.exists(os.path.join(directory, file_ext)):
                os.makedirs(os.path.join(directory, file_ext))
            
            # Move the file to the corresponding directory
            source = os.path.join(directory, filename)
            destination = os.path.join(directory, file_ext, filename)
            shutil.move(source, destination)
            print(f"Moved {filename} to {file_ext} folder")

# Example usage
organize_files("/path/to/your/directory")
