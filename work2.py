"""
project 8.8
Anthony Simmons
03/6/2022
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class TextEditor(EasyFrame):
    """Demonstartes the use of a file dialog"""

    def __init__(self):
        """Set up the windoq and widgets."""
        EasyFrame.__init__(self, "Text Editor")
        self.outputArea = self.addTextArea("", row = 0, column = 0, columnspan = 3, width = 80, height = 15)
        self.addButton(text = "New", row = 1, column = 0, command = self.newFile)
        self.addButton(text = "Open", row = 1, column = 1, command = self.openFile)
        self.addButton(text = "Save", row = 1, column = 2, command = self.saveFile)
    def newFile(self):
        """Clears the text"""
        self.outputArea.setText("")
        self.setTitle("Text Editor")
    def openFile(self):
        """Pops up and open file dialog"""
        fList = [("Python files","*.py"),("Text files","*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)
    def saveFile(self):
        """Pops up and open file. Saves it"""
        if fileName != "":
            file = open(fileName, 'w')
            file.write(self.outputArea.getText())
            file.close()
            self.setTitle(fileName)

def main():
    """Pops the window open"""
    TextEditor().mainloop()

if __name__ == "__main__":
    main()
    
        
                
