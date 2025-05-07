import os
#defing and expactional handling
def files_in_folder(folders_path):
  try:
    files = os.listdir(folders_path)
    return files, none
  except FileNotFoundError:
    return None, "Folder not found"
  except PermissionError:
        return None, "Permission denied"  

#prompt user input
def main():
  folders_path = imput("provide folders path:").split()
  for folder in folders_path:
      files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()  
