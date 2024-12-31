from tkinter import Frame, Entry, Button, Canvas, Label, Tk, CENTER


class Tela:
    def __init__(self: object) -> None:
        self._master = Tk()
        self._html(self._master)
        self._css()
        self._master.mainloop()

    def _html(self: object, master: Tk) -> None:
        self._master = master

        self.rframe = Frame(master)
        self.rlabel = Label(self.rframe, text='R(red)')
        self.rentry = Entry(self.rframe)
        self.rbuttonplus = Button(self.rframe, text='+', command=lambda: expressionself.rplus)
        self.rbuttonminus = Button(self.rframe, text='-', command=self.rminus)

        self.rframe.place(relx=0.05, rely=0.05, relheight=0.20, relwidth=0.20)
        self.rlabel.place(relx=0.5, rely=0.05, anchor=CENTER)
        self.rentry.place(relx=0.1, rely=0.6, relwidth=0.6)
        self.rbuttonplus.place(
            relx=0.8, rely=0.6, relwidth=0.08, relheight=0.08
        )
        self.rbuttonminus.place(
            relx=0.8, rely=0.7, relwidth=0.08, relheight=0.08
        )

    def _css(self: object) -> None:
        pass

    def plus(self: object, campo: Entry) -> None:
        pass

    def minus(self: object, campo: Entry) -> None:
        pass


if __name__ == '__main__':
    Tela()
