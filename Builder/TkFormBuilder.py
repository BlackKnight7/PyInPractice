from Builder.AbstractFormBuilder import AbstractFormBuilder


class TkFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.title = "TkFormBuilder"
        self.statements = []

    def add_title(self, title):
        super().add_title(title)

    def add_lable(self, text, row, column, **kwargs):
        name = self._canonicalize(text)
        create = """self.{}Label = ttk.Label(self, text="{}:")""".format(name, text)
        layout = """self.{}Label.grid(row={}, column={}, sticky=tk.W, \
        padx="0.75m", pady = "0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

    def form(self):
        return TkFormBuilder.TEMPLATE.format(title=self.title, name=self._canonicalize(self.title, False),
                                             statements="\n      ".join(self.statements))

    TEMPLATE = """
    import tkinter as tk
    import tkinter.ttk as ttk

    class {name}Form(tk.Toplevel):
        def __init__(self, master):
            supper().__init__(master)
            self.withdraw()
            self.title("{title}")
            {statements}
            self.bind("<Escape>", lambda *args: self.destroy())
            self.deiconify()
            if self.winfo_viewable():
                self.transient(master)
            self.wait_visibility()
            self.grab_set()
            self.wait_window(self)

     if __name__ == "__main__":
        application = tk.Tk()
        window = {name}Form(application)
        application.protocal("WM_DELETE_WINDOW",application.quite)
        application.mainloop()
    """
