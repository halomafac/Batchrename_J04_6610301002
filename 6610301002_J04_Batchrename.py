import os

def rename_files_in_directory(directory, extension):
    count = 1
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            new_filename = str(count).zfill(3) + extension
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            count += 1

directory = "C:\Batch_rename"  
extension = ".png"  
rename_files_in_directory(directory, extension)
