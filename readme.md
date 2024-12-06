README
======

Overview
--------
This tool provides a graphical user interface (GUI) to delete all files with a specified extension from a chosen folder. It uses Python's built-in os and glob modules to identify and remove files, and it leverages the tkinter library for the GUI components.

Features
--------
- Folder Selection: A "Browse" button allows you to pick a folder using a standard directory selection dialog.
- Extension Input: Enter the desired file extension (e.g., txt, jpg, csv) into a text field.
- Delete Operation: Upon clicking the "Delete Files" button, all files with the given extension in the selected folder will be deleted.
- User Notifications: If no files are found, a message will inform you. If files are deleted successfully, the number of deleted files will be shown.

Requirements
------------
- Python 3.x
- Tkinter (usually included with most Python installations)
- Necessary permissions to delete files in the selected folder

How to Use
----------
1. Clone or Download: Copy the Python file to your local machine.
2. Run the Script:
   python delete_files_by_extension.py

   This will open the GUI window.
   
3. Select a Folder: Click the "Browse..." button and navigate to the folder from which you want to remove files.
4. Enter Extension: In the "File Extension" field, enter the extension of the files you want to delete (without the leading dot). For example, if you want to delete all .txt files, just type txt.
5. Delete Files: Click the "Delete Files" button. If any files match your criteria, they will be deleted, and a success message will be shown. If no files are found, you'll be notified.

Example
-------
If you have a folder like C:\Users\Username\Documents\TestFolder that contains several .txt files:

- Select the folder C:\Users\Username\Documents\TestFolder.
- Enter txt in the file extension field.
- Click "Delete Files".
- All .txt files in that folder will be removed.

Why is this Tool Useful?
------------------------
- Quickly clean up directories by removing unwanted files of a certain type.
- Streamline tasks such as removing old log files, temporary data, or outdated images.
- Save time and reduce manual effort by providing a simple, user-friendly interface for bulk deletions.
- Minimize the risk of manual errors that might occur when deleting files individually.

Code Snippet
------------
Below is a portion of the code that performs the core functionality of finding and deleting files based on the provided extension. It uses the os and glob modules to search for files matching the pattern, removes them from the file system, and then displays a message to the user indicating the outcome.

def delete_files_with_extension(folder_path, extension):
    # Create the full search pattern
    search_pattern = os.path.join(folder_path, f'*.{extension}')
    
    # Find all files that match the pattern
    files_to_delete = glob.glob(search_pattern)
    
    if not files_to_delete:
        messagebox.showinfo("No Files Found", "No files with the specified extension were found.")
        return
    
    # Delete each file
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
            messagebox.showerror("Error", f"Error deleting {file_path}: {e}")
    
    messagebox.showinfo("Success", f"Deleted {len(files_to_delete)} files with the .{extension} extension.")

Notes
-----
- Use this tool carefully, as deleted files cannot be recovered.
- Ensure you have the necessary permissions to delete files in the selected folder.
- This tool does not traverse subdirectories; it only deletes files in the chosen folder.
