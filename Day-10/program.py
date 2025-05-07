import os  # Importing the OS module to interact with the file system

# Prompt the user to input folder names separated by spaces, then split the input into a list
folders = input("Please provide list of folder names with spaces in between: ").split()

# Display the list of folder names entered by the user
print("Folders entered:", folders)

# Iterate through each folder name in the list
for folder in folders:
    try:
        # Attempt to list all files in the specified folder
        files = os.listdir(folder)
    except FileNotFoundError:
        # Handle the case where the folder doesn't exist
        print("Please provide a valid folder name for folder:", folder)
        # Skip to the next folder; use 'break' instead if you want to stop the program here
        continue

    # Indicate which folder is currently being processed
    print("===== Listing files for the folder –", folder)

    # Loop through each file in the current folder and print its name
    for file in files:
        print(file)
