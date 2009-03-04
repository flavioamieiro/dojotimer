#-*- coding: utf-8 -*-
from Tkinter import *
import time
import thread

class Clock(object):

    def __init__(self, master):

        self.master = master

        # Crio o frame principal.
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.master.title("Dojo Rio")

        # Os outros widgets ficam num método separado
        self.create_widgets()

        # Defino alguns valores padrão.
        self.running = False
        self.default_time = 1 # Tempo padrão (em minutos)
        self.seconds = 60 * self.default_time
        self.labelstr.set('%02d:%02d' % ((self.seconds /60), (self.seconds % 60)))

    def create_widgets(self):

        # Crio o label. self.labelstr é o que vai ser usado como texto. Quando for atualizada com o
        # método .set('str') o label vai ser atualizado.
        self.labelstr = StringVar()
        self.label = Label(self.frame, textvariable=self.labelstr, fg='#198931', font=('Helvetica', '48'))
        self.label.pack()

        # Crio alguns botões
        self.start = Button(self.frame, text='Começar', command=self.start)
        self.start.pack(side=LEFT)

        self.stop = Button(self.frame, text='Parar', command=self.stop)
        self.stop.pack(side=LEFT)

        self.reset = Button(self.frame, text='Zerar', command=self.reset)
        self.reset.pack(side=LEFT)

        self.quit = Button(self.frame, text='Sair', command=self.frame.quit)
        self.quit.pack(side=LEFT)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def update(self):
        if self.running:
            if 0 < self.seconds <= 30:
                self.label['fg']='#efbf16'
            elif self.seconds <= 0:
                self.label['fg']='#d70505'
                self.running = False
                for i in range(10):
                    self.master.bell()
                self.master.lift()
            new_str = '%02d:%02d' % ((self.seconds / 60), (self.seconds % 60))
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            self.seconds -= 1
    
    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 60 * self.default_time
        self.label['fg']='#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)


if __name__ == '__main__':
    root = Tk()
    clock = Clock(root)

    root.mainloop()
