import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog


class Window(tk.Frame):
    '''
    1) input email
    2) pass email + instructions into gpt3
    3) get response
    4) output response (corrected email)
    '''
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        ## menu
        self.menubar = tk.Menu()
        ## menu option 1 - file related
        self.menu_file = tk.Menu(self.menubar, tearoff=0)
        # self.menu_file.add_command(label="Open new file", command=self.openfile)
        # self.menu_file.add_command(label="Save", command=self.openfile)
        # self.menu_file.add_command(label="Save as...", command=self.savefileas)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Exit", command=self.quit)
        ## menu option 2 - enhance email
        self.menu_enhance = tk.Menu(self.menubar, tearoff=0)
        # self.menu_enhance.add_command(label="Enhance email", command=self.enhance)
        
        self.menubar.add_cascade(label="File", menu=self.menu_file)
        self.menubar.add_cascade(label="Enhance", menu=self.menu_enhance)
        ## input text area
        self.text = tk.Text()
        self.scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.text.yview)
        # self.scrolledtext_input = scrolledtext.ScrolledText(self, wrap=tk.WORD,
        #                                                     width=40, height=8,
        #                                                     font=("Times New Roman", 15))
        
        
        
        # row 0: menu
        r = 0
        # self.menubar.grid(row=r, column=0, sticky='nsew')
        self.text.pack(side=tk.LEFT)
        self.scrollbar.pack(side=tk.LEFT)
        # row 1: text box
        # r += 1
        # self.label_level.grid(row=r, column=0, sticky='nsew')
        # self.entry_level.grid(row=r, column=1, sticky='nsew')
        # self.label_current.grid(row=r, column=2, sticky='nsew')
        
        for row in range(r+1):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)
            
    def test():
        pass
            
root = tk.Tk()
root.geometry('800x400')
# instance created
app = Window(root)
root.title("Email Enhancer using GPT-3")
app.pack(fill=tk.BOTH, expand=True)
root.config(menu=app.menubar)
# show it and begin mainloop
root.mainloop()