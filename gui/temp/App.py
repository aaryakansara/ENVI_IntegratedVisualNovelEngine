import tkinter as tk
import pygame
from tkinter import *
from tkinter import SUNKEN, PhotoImage, ttk
from tkinter import Button, Toplevel, filedialog, Text
from tkinter import messagebox
from PIL import ImageTk, Image 



myfont11 =("Microsoft YaHei UI", 10)
myfont12 =("Microsoft YaHei UI", 10, "bold")
myfont21 =("Microsoft YaHei UI", 15)
myfont22 =("Microsoft YaHei UI", 15, "bold")
myfont31 =("Microsoft YaHei UI", 20)
myfont32 =("Microsoft YaHei UI", 20, "bold")
myfont41 =("Microsoft YaHei UI", 25)
myfont42 =("Microsoft YaHei UI", 25, "bold")
myfont51 =("Microsoft YaHei UI", 30)
myfont52 =("Microsoft YaHei UI", 30, "bold")
myfont61 =("Microsoft YaHei UI", 35)
myfont62 =("Microsoft YaHei UI", 35, "bold")
myfont71 =("Microsoft YaHei UI", 40)
myfont72 =("Microsoft YaHei UI", 40, "bold")

 

def playonHpage():
    pygame.mixer.init()
    pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/counting_stars.mp3")
    pygame.mixer.music.play(-1)
playonHpage()

def loadframe(event):
    
    loadframe = tk.Frame(bg="maroon")
    loadframe.place(relwidth=1, relheight=1, relx=0, rely=0)
    
    scrollframe = LabelFrame(loadframe, bg="coral4")

    scrollframe.pack(fill="both", expand="yes", padx=200, pady=100)

    innnerframe = Canvas(scrollframe, bg="coral4")
    innnerframe.place(relwidth=1, relheight=1, relx=0, rely=0)

    
    innerframe = tk.Frame(innnerframe, bg="coral4")

    innnerframe.create_window((0, 0), window=innerframe, anchor="nw")
    
    l1 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l1.grid(row=1,column=0)
    
    l2 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l2.grid(row=1,column=1)
    
    l3 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l3.grid(row=1,column=2)
    
    l4 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l4.grid(row=2,column=0)
    
    l5 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l5.grid(row=2,column=1)
    
    l6 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
    l6.grid(row=2,column=2)
    
    loadlabel = tk.Label(loadframe, text="Load", fg="white", font=myfont72, bg="maroon",)
    loadlabel.place(x=20, y=20)
    
    photo = Image.open("ENVI_algo/gui/logo/uparrowimage.png")
    resize = photo.resize((50, 50))
    img1 = ImageTk.PhotoImage(resize)
    uplabel = tk.Button(loadframe,  fg="white",  image= img1, bg="maroon",relief=FLAT)
    uplabel.image = img1
    uplabel.place(x=1190, y=100)
    
    photo = Image.open("ENVI_algo/gui/logo/downarrowimage.png")
    resize = photo.resize((50, 50))
    img2 = ImageTk.PhotoImage(resize)
    downlabel = tk.Button(loadframe,  fg="white",  image= img2, bg="maroon",relief=FLAT)
    downlabel.image = img2
    downlabel.place(x=1190, y=545)
    
    countlabel = tk.Label(loadframe,  fg="white",   bg="maroon", text="1", font=myfont42)#image= img2,
    countlabel.place(x=1190, y=345)
    

    
    def closeframe():
        loadframe.destroy()
    
    showbt = Button(loadframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
    showbt.place(x=1180, y=600)


            
def saveframe(event):
            saveframe = tk.Frame(bg="maroon")
            saveframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(saveframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            v = Scrollbar(innerframe)
            v.pack(side = RIGHT, fill = Y)
            
            savelabel = tk.Label(saveframe, text="Save", fg="white", font=myfont72, bg="maroon",)
            savelabel.place(x=20, y=20)
            
            def closeframe():
                saveframe.destroy()
            
            showbt = Button(saveframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont72, command=closeframe)
            showbt.place(x=1180, y=600)
            
def galleryframe(event):

            galleryframe = tk.Frame(bg="maroon")
            galleryframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(galleryframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            
            l1 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l1.grid(row=1,column=0)
            
            l2 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l2.grid(row=1,column=1)
            
            l3 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l3.grid(row=1,column=2)
            
            l4 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l4.grid(row=2,column=0)
            
            l5 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l5.grid(row=2,column=1)
            
            l6 = tk.Button(innerframe, bg="grey", padx=156, pady=115,)
            l6.grid(row=2,column=2)
                    
            gallerylabel = tk.Label(galleryframe, text="Gallery", fg="white", font=myfont72, bg="maroon",)
            gallerylabel.place(x=20, y=20)
            
            def closeframe():
                galleryframe.destroy()
            
            showbt = Button(galleryframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
            showbt.place(x=1180, y=600)

def aboutframe(event):
            aboutframe = tk.Frame(bg="maroon")
            aboutframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(aboutframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            
            v = Scrollbar(innerframe)

            
            txtarea = Text(innerframe,  bg='coral4', fg='orange1', font= myfont22, yscrollcommand = v.set, borderwidth=0)#width=75, height=20,
            txtarea.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
            def openFile():
                tf = open("ENVI/ENVI Projects/Personal-project/text-folder/AboutProject.envi", 'r')  # or tf = open(tf, 'r')
                data = tf.read()
                txtarea.insert(END, data)
                tf.close()
            openFile()
            v.config(command=txtarea.yview)
            
            aboutlabel = tk.Label(aboutframe, text="About", fg="white", font=myfont72, bg="maroon",)
            aboutlabel.place(x=20, y=20)
            
            def closeframe():
                aboutframe.destroy()
            
            showbt = Button(aboutframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
            showbt.place(x=1180, y=600)
            
def creditsframe(event):
            creditsframe = tk.Frame(bg="maroon")
            creditsframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(creditsframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            
            v = Scrollbar(innerframe)
        
            
            txtarea = Text(innerframe,  bg='coral4', fg='orange1', font= myfont22, yscrollcommand = v.set, borderwidth=0)#width=75, height=20,
            txtarea.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
            def openFile():
                tf = open("ENVI/ENVI Projects/Personal-project/text-folder/ProjectCredits.envi", 'r')  # or tf = open(tf, 'r')
                data = tf.read()
                txtarea.insert(END, data)
                tf.close()
            openFile()
            v.config(command=txtarea.yview)
            
            creditslabel = tk.Label(creditsframe, text="Credits", fg="white", font=myfont72, bg="maroon",)
            creditslabel.place(x=20, y=20)
            
            def closeframe():
                creditsframe.destroy()
            
            showbt = Button(creditsframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
            showbt.place(x=1180, y=600)
            
def helpframe(event):
            helpframe = tk.Frame(bg="maroon")
            helpframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(helpframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            
            v = Scrollbar(innerframe)
           
            
            txtarea = Text(innerframe,  bg='coral4', fg='orange1', font= myfont22, yscrollcommand = v.set, borderwidth=0)#width=75, height=20,
            txtarea.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
            def openFile():
                tf = open("ENVI/ENVI Projects/Personal-project/text-folder/ProjectHelp.envi", 'r')  # or tf = open(tf, 'r')
                data = tf.read()
                txtarea.insert(END, data)
                tf.close()
            openFile()
            txtarea.config(state=DISABLED)
            
            
            helplabel = tk.Label(helpframe, text="Help", fg="white", font=myfont72, bg="maroon",)
            helplabel.place(x=20, y=20)
            
            def closeframe():
                helpframe.destroy()
            
            showbt = Button(helpframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
            showbt.place(x=1180, y=600)
            
def settingsframe(event):
            setframe = tk.Frame(bg="maroon")
            setframe.place(relwidth=1, relheight=1, relx=0, rely=0)
            
            innerframe = tk.Frame(setframe, bg="coral4")
            innerframe.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)
            
            setlabel = tk.Label(setframe, text="Settings", fg="white", font=myfont72, bg="maroon",)
            setlabel.place(x=20, y=20)
                        
            master_frame = Frame(innerframe, bg="coral4")
            master_frame.pack(anchor="w")

            volume_frame = LabelFrame(master_frame, text="Volume", bg="coral4", borderwidth=0, font=myfont42, fg="gray1")
            volume_frame.pack(padx=350, pady=175)

            def volume(x):
                pygame.mixer.music.set_volume(volume_slider.get())
                current_volume = pygame.mixer.music.get_volume()
                current_volume = current_volume * 100
                
            volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=HORIZONTAL, value=1, command=volume, length=300,)
            volume_slider.pack(pady=10)
            
            def closeframe():
                setframe.destroy()
            
            showbt = Button(setframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
            showbt.place(x=1180, y=600) 
            
            
            
def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                app.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')            
            
            



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

        for F in (Homepage, Startofnovel, pgend, pg1, pg2, pg3, pg4, pg5,):
            
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Homepage)
        self.state("zoomed")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()




        
class Homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        def startnovel(event):
            pygame.mixer.init()
            pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/a_sky_full_of_stars.mp3")
            pygame.mixer.music.play(-1)
            controller.show_frame(Startofnovel)

        canvas = tk.Canvas(self, height=700, width=1340, bg="lightblue")
        canvas.pack()
        
        frame = tk.Frame(self, bg="coral4")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        frame1 = tk.Frame(self, bg="maroon")
        frame1.place(relwidth=0.225, relheight=1, relx=0, rely=0)

        frame2 = tk.Frame(self, bg="maroon")
        frame2.place(relwidth=0.745, relheight=0.95, relx=0.24, rely=0.025)
        selfimg = Image.open('ENVI/ENVI Projects/Personal-project/img-folder/Myproject.png')
        resize = selfimg.resize((1020, 670))
        img = ImageTk.PhotoImage(resize)
        label = Label(frame2, image = img)
        label.image = img
        label.pack()

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.1675)
        start = tk.Label(buttonframe, text="Start", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)# command=lambda: controller.show_frame(Startofnovel), relief=SUNKEN) 
        start.pack()
        start.bind("<Button-1>", startnovel,)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.2600)
        load = tk.Label(buttonframe, text="Load", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        load.pack()
        load.bind("<Button-1>", loadframe)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.3525)
        gallery = tk.Label(buttonframe, text="Gallery", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        gallery.pack()
        gallery.bind("<Button-1>", galleryframe)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.4450)
        about = tk.Label(buttonframe, text="About", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        about.pack()
        about.bind("<Button-1>", aboutframe)
 
        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.5380)
        credits = tk.Label(buttonframe, text="Credits", padx=200, pady=30, fg="white", font=myfont32, bg="maroon",)
        credits.pack()
        credits.bind("<Button-1>", creditsframe)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.6305)
        help = tk.Label(buttonframe, text="Help", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        help.pack()
        help.bind("<Button-1>", helpframe)

        buttonframe = tk.Frame(frame1, bg="maroon")
        buttonframe.place(relwidth=0.9, relheight=0.09, relx=0.05, rely=0.7230)
        settings = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont32, bg="maroon")
        settings.pack()
        settings.bind("<Button-1>", settingsframe)
        

   


class Startofnovel(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
                
        def nextpage(event):
            try:
                controller.show_frame(pg1)
            except NameError:
                controller.show_frame(pgend)

        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        frame.bind('<Button-1>', nextpage)

        
        textframe = tk.Frame(frame, bg="maroon")
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)
        
        txtarea = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)#width=75, height=20,
        txtarea.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openFile():
            tf = open("ENVI/ENVI Projects/Personal-project/text-folder/Page0.envi", 'r')  # or tf = open(tf, 'r')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()
        openFile()
        txtarea.config(state=DISABLED)

        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text="Menu", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        menuonpage.pack()
        menuonpage.bind("<Button-1>", returntitle)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text="Save", padx=250, pady=30, borderwidth=0, fg="white", font=myfont21, bg="maroon",)# command=lambda: controller.show_frame(Savefile)) #, selectbg="maroon"
        saveonpage.pack()
        saveonpage.bind("<Button-1>", saveframe)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text="Load", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        loadonpage.pack()
        loadonpage.bind("<Button-1>", loadframe)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        setonpage.pack()
        setonpage.bind("<Button-1>", settingsframe)
        
        


class pgend(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
 
                
        def thereturn(event):
            pygame.mixer.music.stop()
            playonHpage()
            controller.show_frame(Homepage)

        frame = tk.Frame(self, bg="black")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        frame.bind('<Button-1>', thereturn)

        
        textframe = tk.Frame(frame, bg="maroon")
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)
        
        txtarea = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)#width=75, height=20,
        txtarea.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openFile():
            tf = open("ENVI/ENVI Projects/Personal-project/text-folder/Pageend.envi", 'r')  # or tf = open(tf, 'r')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()
        openFile()
        txtarea.config(state=DISABLED)
        

        
        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text="Menu", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        menuonpage.pack()
        menuonpage.bind("<Button-1>", returntitle)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text="Save", padx=250, pady=30, borderwidth=0, fg="white", font=myfont21, bg="maroon",)# command=lambda: controller.show_frame(Savefile)) #, selectbg="maroon"
        saveonpage.pack()
        saveonpage.bind("<Button-1>", saveframe)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text="Load", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        loadonpage.pack()
        loadonpage.bind("<Button-1>", loadframe)
        
        buttonframe = tk.Frame(textframe, bg="maroon")
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text="Settings", padx=250, pady=30, fg="white", font=myfont21, bg="maroon")
        setonpage.pack()
        setonpage.bind("<Button-1>", settingsframe)





class pg1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def nextpage(event):
            try:
                controller.show_frame(pg2)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(Startofnovel)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-tutorial/img-folder/pg1.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/lines/pg1.envi', 'r')
            data = tf.read()
            txt1area.insert(END, data)
            tf.close()
        openDFile()
        txt1area.config(state=DISABLED)

        charnameframe = tk.Frame(frame, bg='maroon')
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg='coral4')
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        txt2area = Text(charnameinframe,  bg='coral4', fg='white', font= myfont22, borderwidth=0,)
        txt2area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openCFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/characters/pg1.envi', 'r')
            data = tf.read()
            txt2area.insert(END, data)
            tf.close()
        openCFile()
        txt2area.config(state=DISABLED)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text='Menu', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        menuonpage.pack()
        menuonpage.bind('<Button-1>', returntitle)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text='Save', padx=250, pady=30, borderwidth=0, fg='white', font=myfont21, bg='maroon',)
        saveonpage.pack()
        saveonpage.bind('<Button-1>', saveframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text='Load', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        loadonpage.pack()
        loadonpage.bind('<Button-1>', loadframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text='Settings', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        setonpage.pack()
        setonpage.bind('<Button-1>', settingsframe)




class pg2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        def nextpage(event):
            try:
                controller.show_frame(pg3)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg1)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-tutorial/img-folder/pg2.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/lines/pg2.envi', 'r')
            data = tf.read()
            txt1area.insert(END, data)
            tf.close()
        openDFile()
        txt1area.config(state=DISABLED)

        charnameframe = tk.Frame(frame, bg='maroon')
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg='coral4')
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        txt2area = Text(charnameinframe,  bg='coral4', fg='white', font= myfont22, borderwidth=0,)
        txt2area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openCFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/characters/pg2.envi', 'r')
            data = tf.read()
            txt2area.insert(END, data)
            tf.close()
        openCFile()
        txt2area.config(state=DISABLED)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text='Menu', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        menuonpage.pack()
        menuonpage.bind('<Button-1>', returntitle)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text='Save', padx=250, pady=30, borderwidth=0, fg='white', font=myfont21, bg='maroon',)
        saveonpage.pack()
        saveonpage.bind('<Button-1>', saveframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text='Load', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        loadonpage.pack()
        loadonpage.bind('<Button-1>', loadframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text='Settings', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        setonpage.pack()
        setonpage.bind('<Button-1>', settingsframe)




class pg3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


       

        def nextpage(event):
            try:
                controller.show_frame(pg4)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg2)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-tutorial/img-folder/pg3.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/lines/pg3.envi', 'r')
            data = tf.read()
            txt1area.insert(END, data)
            tf.close()
        openDFile()
        txt1area.config(state=DISABLED)

        charnameframe = tk.Frame(frame, bg='maroon')
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg='coral4')
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        txt2area = Text(charnameinframe,  bg='coral4', fg='white', font= myfont22, borderwidth=0,)
        txt2area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openCFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/characters/pg3.envi', 'r')
            data = tf.read()
            txt2area.insert(END, data)
            tf.close()
        openCFile()
        txt2area.config(state=DISABLED)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text='Menu', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        menuonpage.pack()
        menuonpage.bind('<Button-1>', returntitle)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text='Save', padx=250, pady=30, borderwidth=0, fg='white', font=myfont21, bg='maroon',)
        saveonpage.pack()
        saveonpage.bind('<Button-1>', saveframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text='Load', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        loadonpage.pack()
        loadonpage.bind('<Button-1>', loadframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text='Settings', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        setonpage.pack()
        setonpage.bind('<Button-1>', settingsframe)




class pg4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        def nextpage(event):
            try:
                controller.show_frame(pg5)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg3)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-tutorial/img-folder/pg4.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/lines/pg4.envi', 'r')
            data = tf.read()
            txt1area.insert(END, data)
            tf.close()
        openDFile()
        txt1area.config(state=DISABLED)

        charnameframe = tk.Frame(frame, bg='maroon')
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg='coral4')
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        txt2area = Text(charnameinframe,  bg='coral4', fg='white', font= myfont22, borderwidth=0,)
        txt2area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openCFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/characters/pg4.envi', 'r')
            data = tf.read()
            txt2area.insert(END, data)
            tf.close()
        openCFile()
        txt2area.config(state=DISABLED)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text='Menu', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        menuonpage.pack()
        menuonpage.bind('<Button-1>', returntitle)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text='Save', padx=250, pady=30, borderwidth=0, fg='white', font=myfont21, bg='maroon',)
        saveonpage.pack()
        saveonpage.bind('<Button-1>', saveframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text='Load', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        loadonpage.pack()
        loadonpage.bind('<Button-1>', loadframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text='Settings', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        setonpage.pack()
        setonpage.bind('<Button-1>', settingsframe)




class pg5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


   

        def nextpage(event):
            try:
                controller.show_frame(pgend)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg4)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-tutorial/img-folder/pg5.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/lines/pg5.envi', 'r')
            data = tf.read()
            txt1area.insert(END, data)
            tf.close()
        openDFile()
        txt1area.config(state=DISABLED)

        charnameframe = tk.Frame(frame, bg='maroon')
        charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        charnameinframe = tk.Frame(charnameframe, bg='coral4')
        charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        txt2area = Text(charnameinframe,  bg='coral4', fg='white', font= myfont22, borderwidth=0,)
        txt2area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openCFile():
            tf = open('ENVI/ENVI Projects/Personal-tutorial/text-folder/characters/pg5.envi', 'r')
            data = tf.read()
            txt2area.insert(END, data)
            tf.close()
        openCFile()
        txt2area.config(state=DISABLED)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.3, rely=0.82)
        menuonpage = tk.Label(buttonframe, text='Menu', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        menuonpage.pack()
        menuonpage.bind('<Button-1>', returntitle)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.4, rely=0.82)
        saveonpage = tk.Button(buttonframe, text='Save', padx=250, pady=30, borderwidth=0, fg='white', font=myfont21, bg='maroon',)
        saveonpage.pack()
        saveonpage.bind('<Button-1>', saveframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.5, rely=0.82)
        loadonpage = tk.Label(buttonframe, text='Load', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        loadonpage.pack()
        loadonpage.bind('<Button-1>', loadframe)

        buttonframe = tk.Frame(textframe, bg='maroon')
        buttonframe.place(relwidth=0.1, relheight=0.15, relx=0.6, rely=0.82)
        setonpage = tk.Label(buttonframe, text='Settings', padx=250, pady=30, fg='white', font=myfont21, bg='maroon')
        setonpage.pack()
        setonpage.bind('<Button-1>', settingsframe)




    

app = Myproject()
app.mainloop()