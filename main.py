import tkinter as tk
from tkinter import ttk
from gpt3 import model as gpt_model

def model(**args):
    try:
        response = gpt_model(**args)
    except Exception as e:
        response = f"Error encountered:\n{e}"
    return response

def enhance():
    # get input
    input_text = text_input.get("1.0", "end")
    # call model and get response
    response = model(task = "Creatively improve the English in the following: \n",
                     body = input_text,
                     save = False)
    # replace text_output with response
    text_output.delete("1.0", "end")
    text_output.insert(tk.INSERT, response)
    
root = tk.Tk()
## main structure
### wrapper 1: input email
wrapper1 = tk.LabelFrame(root, text="Input email here", padx=5, pady=3, height=265)
wrapper1.pack(fill=tk.BOTH, padx=10, pady=5)
### enhance button:
button_enhance = tk.Button(root, text="Enhance", padx=3, pady=3, command=enhance)
button_enhance.pack(expand=False, pady=3)
### wrapper 2: GPT-3 output
wrapper2 = tk.LabelFrame(root, text="GPT-3 enhanced email", padx=5, pady=3, height=265)
wrapper2.pack(fill=tk.BOTH, padx=10, pady=5)

## input email box
text_input = tk.Text(wrapper1)
text_input.place(x=10, y=3, height=225, width=700)

## output email box
text_output = tk.Text(wrapper2)
text_output.place(x=10, y=3, height=225, width=700)


root.geometry('750x600') # width x height
root.title("GPT-3 email enhancer")
root.mainloop()