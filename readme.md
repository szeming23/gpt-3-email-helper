# GPT-3 UI project

## how to convert to `.exe` (for Windows) or `.app` file (for macOS)

``pip3 install py2app``

``py2applet --make-setup main.py``

``rm -rf build dist``

alias mode: 
``python3 setup.py py2app -A``

if working properly,  
``python3 setup.py py2app``
