import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilenames, askopenfilename

files_list = []

def open_file():
    global files_list
    #file = askopenfile(filetypes=[('All Files', '*.*'), ('docx files', '*.docx')])
    files = askopenfilenames(filetypes =[('All Files', '*.*'), ('docx files', '*.docx')])
    if files is not None:
        #print(file.name)
        #print(file.encoding)
        files_list += [fn for fn in files]
        text_file = '\n'.join([fn for fn in files_list])
        print_list_of_files(text_file)
    return files_list

def clear_list_files():
    global files_list
    files_list = []
    files_selected.delete("1.0", "end-1c")  # clear the outputtext text widget


def print_list_of_files(files):
    #Your code that checks the expression
    files_selected.delete("1.0", "end-1c") # clear the outputtext text widget
    files_selected.insert(tk.END, files)

window = tk.Tk()
window.minsize(width=500, height=250)
tk.Grid.columnconfigure(window, 0, weight=1)
tk.Grid.rowconfigure(window, 0, weight=1)

output_frame = tk.Frame(window, bg="#000099")
output_frame.grid(row=0, column=0, sticky='N'+'S'+'E'+'W')

label = tk.Label(output_frame, text="Little label:")
label.grid(row=0, column=0)
files_selected = tk.Text(output_frame)
files_selected.grid(row=1, column=0)

button_frame = tk.Frame(window)
button_frame.grid(row=0, column=1, sticky='N')

button_open = tk.Button(button_frame, text="Open file", width = 10, command=open_file)
button_open.grid(row=0, column=0, sticky='E')
button_export = tk.Button(button_frame, text="Clear", width = 10, command=clear_list_files)
button_export.grid(row=1, column=0, sticky='E')
button_docx = tk.Button(button_frame, text="Convert docx", width = 10)
button_docx.grid(row=2, column=0, sticky='E')
button_export = tk.Button(button_frame, text="Export", width = 10)
button_export.grid(row=3, column=0, sticky='E')





window.mainloop()