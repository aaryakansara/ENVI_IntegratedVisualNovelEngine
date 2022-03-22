import tkinter as tk
import pygame
from tkinter import *
from tkinter import SUNKEN, PhotoImage, ttk
from tkinter import Button, Toplevel, filedialog, Text
from tkinter import messagebox



myfont11 =("Microsoft YaHei UI", 10)
myfont12 =("Microsoft YaHei UI", 10, "bold")
myfont21 =("Microsoft YaHei UI", 15)
myfont22 =("Microsoft YaHei UI", 15, "bold")
myfont31 =("Microsoft YaHei UI", 20)
myfont32 =("Microsoft YaHei UI", 20, "bold")
myfont41 =("Microsoft YaHei UI", 25)
myfont42 =("Microsoft YaHei UI", 25, "bold")

 

def playonHpage():
    pygame.mixer.init()
    pygame.mixer.music.load("ENVI_algo/ENVI-Projects/Personal-project/music-folder/counting_stars.mp3")
    pygame.mixer.music.play(-1)
playonHpage()



class Myproject(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self,default='')
        tk.Tk.wm_title(self, "Myproject")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Homepage, EnviMenu, EnviMenu2, Startofnovel,):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Homepage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class Homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        def startnovel(event):
            pygame.mixer.init()
            pygame.mixer.music.load("ENVI_algo/ENVI-Projects/Personal-project/music-folder/a_sky_full_of_stars.mp3")
            pygame.mixer.music.play(-1)
            controller.show_frame(Startofnovel)
            
        def loadevent(event):
            controller.show_frame(EnviMenu) 
            
        def settingsframe(event):
            setframe = tk.Frame(self, bg="maroon")
            setframe.place(relwidth=0.745, relheight=0.95, relx=0.24, rely=0.025)
            
            master_frame = Frame(setframe, bg="maroon")
            master_frame.pack(pady=20)

            volume_frame = LabelFrame(master_frame, text="Volume", font=myfont31, bg="maroon", borderwidth=0)
            volume_frame.pack()

            def volume(x):
                pygame.mixer.music.set_volume(volume_slider.get())
                current_volume = pygame.mixer.music.get_volume()
                current_volume = current_volume * 100
                
            volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=HORIZONTAL, value=1, command=volume, length=300)
            volume_slider.pack(pady=10)
            
            def closeframe():
                setframe.destroy()
        
            showbt = Button(setframe, text="Close Frame", borderwidth=0, bg="white", font=myfont31, command=closeframe)
            showbt.pack(pady=20)

        canvas = tk.Canvas(self, height=700, width=1340, bg="lightblue")
        canvas.pack()
        
        frame = tk.Frame(self, bg="coral4")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        frame1 = tk.Frame(self, bg="maroon")
        frame1.place(relwidth=0.225, relheight=1, relx=0, rely=0)

        frame2 = tk.Frame(self, bg="maroon")
        frame2.place(relwidth=0.745, relheight=0.95, relx=0.24, rely=0.025)
        self.img = PhotoImage(file='ENVI_algo/ENVI-Projects/Personal-project/img-folder/Myproject.png')
        label = Label(frame2, image = self.img)
        label.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.1675)
        start = tk.Label(buttonframe, text="Start", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",) 
        start.pack()
        start.bind("<Button-1>", startnovel,)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.2600)
        load = tk.Label(buttonframe, text="Load", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        load.pack()
        load.bind("<Button-1>", loadevent)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.3525)
        gallery = tk.Label(buttonframe, text="Gallery", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.4450)
        gallery = tk.Label(buttonframe, text="About", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
 
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.5380)
        gallery = tk.Label(buttonframe, text="Credits", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
    
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.6305)
        help = tk.Label(buttonframe, text="Help", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        help.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.7230)
        settings = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        settings.pack()
        settings.bind("<Button-1>", settingsframe)
        
        



class EnviMenu(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def startnovel(event):
            controller.show_frame(Startofnovel) 

        canvas = tk.Canvas(self, height=700, width=1340, bg="lightblue")
        canvas.pack()
        
        frame = tk.Frame(self, bg="coral4")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        frame1 = tk.Frame(self, bg="maroon")
        frame1.place(relwidth=0.225, relheight=1, relx=0, rely=0)

        frame2 = tk.Frame(self, bg="maroon")
        frame2.place(relwidth=0.745, relheight=0.95, relx=0.24, rely=0.025)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.1675)
        start = tk.Label(buttonframe, text="Save", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        start.pack()
     
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.2600)
        load = tk.Label(buttonframe, text="Load", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        load.pack()
        def loadevent(event):
            controller.show_frame(EnviMenu)
        load.bind("<Button-1>", loadevent)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.3525)
        gallery = tk.Label(buttonframe, text="Gallery", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
    
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.4450)
        gallery = tk.Label(buttonframe, text="About", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
   
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.5380)
        gallery = tk.Label(buttonframe, text="Credits", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
       
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.6305)
        help = tk.Label(buttonframe, text="Help", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        help.pack()
        
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.7230)
        settings = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        settings.pack()
        
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.8155)
        returntopage = tk.Label(buttonframe, text="Return", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        returntopage.pack()
        def return2(event):
            controller.show_frame(Homepage)
        returntopage.bind("<Button-1>", return2)
        
        
class EnviMenu2(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def startnovel(event):
            controller.show_frame(Startofnovel) 

        canvas = tk.Canvas(self, height=700, width=1340, bg="lightblue")
        canvas.pack()
        
        frame = tk.Frame(self, bg="coral4")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        frame1 = tk.Frame(self, bg="maroon")
        frame1.place(relwidth=0.225, relheight=1, relx=0, rely=0)

        frame2 = tk.Frame(self, bg="maroon")
        frame2.place(relwidth=0.745, relheight=0.95, relx=0.24, rely=0.025)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.1675)
        start = tk.Label(buttonframe, text="Save", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        start.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.2600)
        load = tk.Label(buttonframe, text="Load", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        load.pack()
        def loadevent(event):
            controller.show_frame(EnviMenu)
        load.bind("<Button-1>", loadevent)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.3525)
        gallery = tk.Label(buttonframe, text="Gallery", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.4450)
        gallery = tk.Label(buttonframe, text="About", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
       
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.5380)
        gallery = tk.Label(buttonframe, text="Credits", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
       
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.6305)
        help = tk.Label(buttonframe, text="Help", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        help.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.7230)
        settings = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        settings.pack()
        
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.8155)
        returntopage = tk.Label(buttonframe, text="Return", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        returntopage.pack()
        def return2(event):
            controller.show_frame(Startofnovel)
        returntopage.bind("<Button-1>", return2)

   



class Startofnovel(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? \nAll unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')
                
        def settingsframe(event):
            setframe = tk.Frame(self, bg="maroon")
            setframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            master_frame = Frame(setframe, bg="maroon")
            master_frame.pack(pady=20)

            volume_frame = LabelFrame(master_frame, text="Volume", font=myfont31 , bg="maroon", borderwidth=0)
            volume_frame.pack()

            def volume(x):
                pygame.mixer.music.set_volume(volume_slider.get())
                current_volume = pygame.mixer.music.get_volume()
                current_volume = current_volume * 100
                
            volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=HORIZONTAL, value=1, command=volume, length=300)
            volume_slider.pack(pady=10)
            
            def closeframe():
                setframe.destroy()
        
            showbt = Button(setframe, text="Close Frame", borderwidth=0, bg="white", font=myfont31, command=closeframe)
            showbt.pack(pady=20)
                
        frame = tk.Frame(self, bg="coral4")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        
        def save(event):
            controller.show_frame(EnviMenu2)
        self.bind('<w>', save)
        
        textframe = tk.Frame(frame, bg="maroon")
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)
        
        charnameframe = tk.Frame(frame, bg="maroon")
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg="coral4")
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text="Menu", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        menuonpage.pack()
        menuonpage.bind("<Button-1>", returntitle)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text="Save", padx=250, pady=30, borderwidth=0, fg="white", font=myfont21, bg="maroon", command=lambda: controller.show_frame(EnviMenu2))
        saveonpage.pack()
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text="Load", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        loadonpage.pack()
        def save(event):
            controller.show_frame(EnviMenu2)
        loadonpage.bind("<Button-1>", save)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        setonpage.pack()
        setonpage.bind("<Button-1>", settingsframe)


app = Myproject()
app.mainloop()