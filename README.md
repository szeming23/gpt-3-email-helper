# GPT-3 email enhancer UI project

Python tkinter UI that allows layman to leverage on GPT-3 to enhance their emails with proper grammar as well as more creative adjectives and better structure.

## how to convert `.py` to `.exe` file (for Windows)

``pip install pyinstaller``

``pyinstaller --onefile <file>.py``
  
## how to convert a `.py` to `.app` file (for macOS)

``pip3 install py2app``

``py2applet --make-setup main.py``

``rm -rf build dist``

Build in alias mode:  
``python3 setup.py py2app -A``

Build for deployment, if working properly in alias mode:  
``python3 setup.py py2app``
