from tkinter import Frame, Button, Canvas, Label, Tk, Scale, CENTER


class Tela:
    def __init__(self: object) -> None:
        self._master = Tk()
        self._html(self._master)
        self._css()
        self._master.mainloop()

    def _html(self: object, master: Tk) -> None:
        self._master = master

        self._title = Label(master, text='Vizualizador RGB', name='_title')
        self._title.pack(side='top', fill='x')
        self._sair = Button(master, command=self._master.destroy,
                            text='Sair', name='_sair')
        self._sair.pack(side='bottom', fill='x')

        LABEL_POS = {'relx': 0.5, 'rely': 0.15, 'relwidth': 1,
                     'anchor': CENTER}
        HEXLABEL_POS = {'relx': 0.5, 'rely': 0.4, 'anchor': CENTER}
        SCALE_POS = {'relx': 0.15, 'rely': 0.56, 'relwidth': 0.70}
        MINUS_POS = {'relx': 0, 'rely': 0.7, 'relwidth': 0.15,
                     'relheight': 0.15}
        PLUS_POS = {'relx': 0.85, 'rely': 0.7, 'relwidth': 0.15,
                    'relheight': 0.15}
        GENERALFRAME_POS = {'rely': 0.05, 'relheight': 0.24, 'relwidth': 0.25}

        self.rframe = Frame(master, name='rframe')
        self.rlabel = Label(self.rframe, text='R(red)', name='rlabel')
        self.rhexlabel = Label(self.rframe, text='0', name='rhexlabel')
        self.rscale = Scale(self.rframe, orient='horizontal', from_=0, to=255,
                            command=lambda value: self.change_color(),
                            name='rscale')
        self.rbuttonplus = Button(self.rframe, text='+', name='rbuttonplus',
                                  command=lambda: self.plus(self.rscale))
        self.rbuttonminus = Button(self.rframe, text='-', name='rbuttonminus',
                                   command=lambda: self.minus(self.rscale))

        self.rframe.place(relx=0.05, **GENERALFRAME_POS)
        self.rlabel.place(LABEL_POS)
        self.rhexlabel.place(HEXLABEL_POS)
        self.rscale.place(**SCALE_POS)
        self.rbuttonplus.place(PLUS_POS)
        self.rbuttonminus.place(MINUS_POS)

        self.gframe = Frame(master, name='gframe')
        self.glabel = Label(self.gframe, text='G(reen)', name='glabel')
        self.ghexlabel = Label(self.gframe, text='0', name='ghexlabel')
        self.gscale = Scale(self.gframe, orient='horizontal', from_=0, to=255,
                            name='gscale',
                            command=lambda value: self.change_color())
        self.gbuttonplus = Button(self.gframe, text='+', name='gbuttonplus',
                                  command=lambda: self.plus(self.gscale))
        self.gbuttonminus = Button(self.gframe, text='-', name='gbuttonminus',
                                   command=lambda: self.minus(self.gscale))

        self.gframe.place(relx=0.35, **GENERALFRAME_POS)
        self.glabel.place(LABEL_POS)
        self.ghexlabel.place(HEXLABEL_POS)
        self.gscale.place(SCALE_POS)
        self.gbuttonplus.place(PLUS_POS)
        self.gbuttonminus.place(MINUS_POS)

        self.bframe = Frame(master, name='bframe')
        self.blabel = Label(self.bframe, text='B(lue)', name='blabel')
        self.bhexlabel = Label(self.bframe, text='0', name='bhexlabel')
        self.bscale = Scale(self.bframe, orient='horizontal', from_=0, to=255,
                            name='bscale',
                            command=lambda value: self.change_color())
        self.bbuttonplus = Button(self.bframe, text='+', name='bbuttonplus',
                                  command=lambda: self.plus(self.bscale))
        self.bbuttonminus = Button(self.bframe, text='-', name='bbuttonminus',
                                   command=lambda: self.minus(self.bscale))

        self.bframe.place(relx=0.65, **GENERALFRAME_POS)
        self.blabel.place(LABEL_POS)
        self.bhexlabel.place(HEXLABEL_POS)
        self.bscale.place(SCALE_POS)
        self.bbuttonplus.place(PLUS_POS)
        self.bbuttonminus.place(MINUS_POS)

        self._canvas = Canvas(master, name='_canvas')
        self._canvas.place(relx=0.05, relwidth=0.9, rely=0.3, relheight=0.645)
        self._hexlabel = Label(master, name='_hexlabel')
        self._hexlabel.place(relx=0.5, rely=0.625, anchor=CENTER)
        self.change_color()

        self._widgets = (
            self._master,
            self._title,
            self._sair,
            self.rframe,
            self.rlabel,
            self.rhexlabel,
            self.rscale,
            self.rbuttonplus,
            self.rbuttonminus,
            self.gframe,
            self.glabel,
            self.ghexlabel,
            self.gscale,
            self.gbuttonplus,
            self.gbuttonminus,
            self.bframe,
            self.blabel,
            self.bhexlabel,
            self.bscale,
            self.bbuttonplus,
            self.bbuttonminus,
            self._canvas,
            self._hexlabel
        )

    def _css(self: object) -> None:
        GENERAL_FG = '#FFF'
        GENERAL_BG = '#000'
        RED = '#A00'
        GREEN = '#0A0'
        BLUE = '#00A'
        FONT = ('BigBlueTerm437 nerd font', '18', 'bold')
        for widget in self._widgets:
            if type(widget) is not Tk:
                match (widget._name[0]):
                    case 'r':
                        widget.config(bg=RED)
                    case 'g':
                        widget.config(bg=GREEN)
                    case 'b':
                        widget.config(bg=BLUE)
                    case _:
                        widget.config(bg=GENERAL_BG)
                try:
                    widget.config(fg=GENERAL_FG,
                                  font=FONT)
                except Exception:
                    pass
                if type(widget) is Frame:
                    widget: Frame
                    widget.config(borderwidth=4, relief='sunken')
            else:
                widget.config(bg=GENERAL_BG)
                widget.geometry('800x500')
                widget.resizable(True, True)
                widget.title('RGB Viewer')

    def change_color(self: object) -> None:
        r = hex(int(self.rscale.get())).removeprefix('0x')
        g = hex(int(self.gscale.get())).removeprefix('0x')
        b = hex(int(self.bscale.get())).removeprefix('0x')
        if any(color is None for color in (r, g, b)):
            return
        if len(r) == 1:
            r = '0' + r
        if len(g) == 1:
            g = '0' + g
        if len(b) == 1:
            b = '0' + b
        self.rhexlabel.configure(text=r)
        self.ghexlabel.configure(text=g)
        self.bhexlabel.configure(text=b)
        self._hexlabel.config(text=str(r + g + b).upper())
        color = str('#' + r + g + b)
        self._canvas.config(bg=color)

    def plus(self: object, campo: Scale) -> None:
        from tkinter import messagebox
        valor = campo.get()
        if valor < 255:
            campo.set(campo.get() + 1)
            self.change_color()
            return
        messagebox.showwarning('Aviso', 'Valor maior que o limite (255).')

    def minus(self: object, campo: Scale) -> None:
        from tkinter import messagebox
        valor = campo.get()
        if valor > 0:
            campo.set(campo.get() - 1)
            self.change_color()
            return
        messagebox.showwarning('Aviso', 'Valor menor que o limite (0).')


if __name__ == '__main__':
    Tela()
