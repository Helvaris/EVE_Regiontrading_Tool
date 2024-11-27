from tkinter import Toplevel, Text, Scrollbar, VERTICAL, END

class DebugWindow:
    def __init__(self, root):
        self.window = Toplevel(root)
        self.window.title("Debug")
        self.text_widget = Text(self.window, wrap="word")
        self.scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def append_log(self, message):
        self.text_widget.insert(END, message + "\n")
        self.text_widget.see(END)
