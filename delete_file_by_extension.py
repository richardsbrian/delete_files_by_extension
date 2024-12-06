import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

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

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

def on_delete_button_click():
    folder = folder_entry.get()
    extension = extension_entry.get()
    
    if not folder or not extension:
        messagebox.showwarning("Input Error", "Please provide both a folder path and a file extension.")
        return
    
    if not os.path.isdir(folder):
        messagebox.showerror("Folder Error", "The provided folder path is not valid.")
        return
    
    delete_files_with_extension(folder, extension)

# Create the main application window
root = tk.Tk()
root.title("Delete Files by Extension")

# Create and place the folder selection label and entry
folder_label = tk.Label(root, text="Folder:")
folder_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse...", command=select_folder)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Create and place the file extension label and entry
extension_label = tk.Label(root, text="File Extension:")
extension_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

extension_entry = tk.Entry(root, width=50)
extension_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the delete button
delete_button = tk.Button(root, text="Delete Files", command=on_delete_button_click)
delete_button.grid(row=2, column=1, padx=10, pady=20)

# Run the Tkinter main loop
root.mainloop()

