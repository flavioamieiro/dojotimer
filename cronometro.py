#-*- coding: utf-8 -*-
from Tkinter import *
import time
import thread

class Clock(object):

    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()

        self.labelstr = StringVar()
        self.label = Label(frame, textvariable=self.labelstr, fg='#198931', font=('Helvetica', '48'))
        self.label.pack()

        self.start = Button(frame, text='Começar', command=self.start)
        self.start.pack(side=LEFT)

        self.stop = Button(frame, text='Parar', command=self.stop)
        self.stop.pack(side=LEFT)

        self.reset = Button(frame, text='Zerar', command=self.reset)
        self.reset.pack(side=LEFT)

        self.quit = Button(frame, text='Sair', command=frame.quit)
        self.quit.pack(side=LEFT)

        self.running = False
        self.seconds = 60 * 1
        self.labelstr.set('%02d:%02d' % ((self.seconds /60), (self.seconds % 60)))

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
            new_str = '%02d:%02d' % ((self.seconds / 60), (self.seconds % 60))
            self.labelstr.set(new_str)
            self.label.after(1000, self.update)
            self.seconds -= 1
    
    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 60 * 1
        self.label['fg']='#198931'
        new_str = '%02d:%02d' % ((self.seconds /60), (self.seconds % 60))
        self.labelstr.set(new_str)


if __name__ == '__main__':
    root = Tk()
    clock = Clock(root)

    root.mainloop()
