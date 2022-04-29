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
            
            scrollframe = LabelFrame(saveframe, bg="coral4")

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
            
            loadlabel = tk.Label(saveframe, text="Load", fg="white", font=myfont72, bg="maroon",)
            loadlabel.place(x=20, y=20)
            
            photo = Image.open("ENVI_algo/gui/logo/uparrowimage.png")
            resize = photo.resize((50, 50))
            img1 = ImageTk.PhotoImage(resize)
            uplabel = tk.Button(saveframe,  fg="white",  image= img1, bg="maroon",relief=FLAT)
            uplabel.image = img1
            uplabel.place(x=1190, y=100)
            
            photo = Image.open("ENVI_algo/gui/logo/downarrowimage.png")
            resize = photo.resize((50, 50))
            img2 = ImageTk.PhotoImage(resize)
            downlabel = tk.Button(saveframe,  fg="white",  image= img2, bg="maroon",relief=FLAT)
            downlabel.image = img2
            downlabel.place(x=1190, y=545)
            
            countlabel = tk.Label(saveframe,  fg="white",   bg="maroon", text="1", font=myfont42)#image= img2,
            countlabel.place(x=1190, y=345)
            
            def closeframe():
                saveframe.destroy()
            
            showbt = Button(saveframe, text="Return", borderwidth=0, fg="white", bg="maroon", font=myfont42, command=closeframe)
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

        for F in (Homepage, Startofnovel, pgend, pg1, pg2, pg3, pg4, pg5, pg6, pg7, pg8, pg9, pg10, pg11, pg12, pg13, pg14, pg15, pg16, pg17, pg18, pg19, pg20, pg21, pg22, pg23, pg24, pg25, pg26, pg27, pg28, pg29, pg30, pg31, pg32, pg33, pg34, pg35, pg36, pg37, pg38, pg39, pg40, pg41, pg42, pg43, pg44, pg45, pg46, pg47, pg48, pg49, pg50, pg51, pg52,):
            
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
        
        
        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')
                
        def nextpage(event):
            try:
                controller.show_frame(pg1)
            except NameError:
                controller.show_frame(pgend)
                
        def prevpage(event):
            try:
                controller.show_frame(pgend)
            except NameError:
                controller.show_frame(Startofnovel)

        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        # my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg1.png')
        # resize = my_image.resize((1500, 850))
        # img1 = ImageTk.PhotoImage(resize)
        # imagelabel = Label(frame, image= img1, borderwidth=0)
        # imagelabel.image = img1
        # imagelabel.pack()
        frame.bind('<Button-1>', nextpage)
        frame.bind('<Right>', nextpage)
        
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
        
        # charnameframe = tk.Frame(frame, bg="maroon")
        # charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        # charnameinframe = tk.Frame(charnameframe, bg="coral4")
        # charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        
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
        
        
        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')
                
        def thereturn(event):
            pygame.mixer.music.stop()
            playonHpage()
            controller.show_frame(Homepage)
            
        def prevpage(event):
            try:
                controller.show_frame(pgend)
            except NameError:
                controller.show_frame(Startofnovel)

        frame = tk.Frame(self, bg="black")
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        frame.bind('<Button-1>', thereturn)
        frame.bind('<Return>', thereturn)

        
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
        
        # charnameframe = tk.Frame(frame, bg="maroon")
        # charnameframe.place(relwidth=0.2, relheight=0.05, relx=0.01, rely=0.75)
        # charnameinframe = tk.Frame(charnameframe, bg="coral4")
        # charnameinframe.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        
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


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

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

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg1.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg1.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg1.envi', 'r')
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


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

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

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg2.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg2.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg2.envi', 'r')
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


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

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

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg3.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg3.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg3.envi', 'r')
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


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

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

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg4.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg4.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg4.envi', 'r')
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


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg6)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg4)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg5.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg5.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg5.envi', 'r')
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




class pg6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg7)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg5)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg6.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg6.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg6.envi', 'r')
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




class pg7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg8)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg6)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg7.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg7.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg7.envi', 'r')
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




class pg8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg9)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg7)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg8.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg8.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg8.envi', 'r')
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




class pg9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg10)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg8)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg9.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        #imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)
        
        buttonframe = tk.Label(self, bg='black', text='Teddy', fg='white', font=myfont21)
        buttonframe.pack(pady=80)
        buttonframe.bind('<Button-1>', nextpage)
        
        buttonframe = tk.Label(self, bg='black', text='Book', fg='white', font=myfont21)
        buttonframe.pack(pady=80)
        buttonframe.bind('<Button-1>', nextpage)
        
        buttonframe = tk.Label(self, bg='black', text='Watch', fg='white', font=myfont21)
        buttonframe.pack(pady=80)
        buttonframe.bind('<Button-1>', nextpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg9.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg9.envi', 'r')
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




class pg10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg11)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg9)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg10.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg10.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg10.envi', 'r')
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




class pg11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg12)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg10)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg11.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg11.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg11.envi', 'r')
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




class pg12(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                
                controller.show_frame(pg13)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg11)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg12.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg12.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg12.envi', 'r')
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




class pg13(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/say_something.mp3")
                pygame.mixer.music.play(-1)
                controller.show_frame(pg14)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg12)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg13.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg13.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg13.envi', 'r')
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




class pg14(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg15)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg13)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg14.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg14.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg14.envi', 'r')
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




class pg15(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg16)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg14)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg15.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg15.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg15.envi', 'r')
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




class pg16(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg17)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg15)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg16.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg16.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg16.envi', 'r')
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




class pg17(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg18)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg16)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg17.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg17.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg17.envi', 'r')
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




class pg18(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg19)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg17)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg18.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg18.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg18.envi', 'r')
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




class pg19(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg20)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg18)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg19.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg19.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg19.envi', 'r')
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




class pg20(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg21)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg19)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg20.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg20.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg20.envi', 'r')
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




class pg21(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg22)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg20)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg21.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg21.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg21.envi', 'r')
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




class pg22(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg23)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg21)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg22.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg22.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg22.envi', 'r')
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




class pg23(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg24)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg22)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg23.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg23.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg23.envi', 'r')
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




class pg24(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg25)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg23)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg24.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg24.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg24.envi', 'r')
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




class pg25(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg26)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg24)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg25.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg25.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg25.envi', 'r')
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




class pg26(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg27)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg25)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg26.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg26.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg26.envi', 'r')
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




class pg27(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg28)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg26)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg27.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg27.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg27.envi', 'r')
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




class pg28(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg29)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg27)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg28.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg28.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg28.envi', 'r')
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




class pg29(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg30)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg28)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg29.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg29.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg29.envi', 'r')
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




class pg30(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg31)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg29)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg30.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg30.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg30.envi', 'r')
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




class pg31(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg32)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg30)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg31.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg31.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg31.envi', 'r')
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




class pg32(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg33)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg31)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg32.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg32.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg32.envi', 'r')
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




class pg33(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg34)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg32)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg33.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg33.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg33.envi', 'r')
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




class pg34(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg35)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg33)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg34.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg34.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg34.envi', 'r')
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




class pg35(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg36)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg34)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg35.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg35.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg35.envi', 'r')
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




class pg36(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg37)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg35)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg36.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg36.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg36.envi', 'r')
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




class pg37(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg38)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg36)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg37.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg37.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg37.envi', 'r')
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




class pg38(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg39)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg37)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg38.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg38.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg38.envi', 'r')
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




class pg39(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg40)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg38)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg39.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg39.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg39.envi', 'r')
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




class pg40(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg41)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg39)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg40.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg40.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg40.envi', 'r')
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




class pg41(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg42)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg40)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg41.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg41.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg41.envi', 'r')
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




class pg42(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg43)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg41)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg42.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg42.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg42.envi', 'r')
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




class pg43(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg44)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg42)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg43.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg43.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg43.envi', 'r')
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




class pg44(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg45)
            except NameError:
                controller.show_frame(pgend)
                
        def newtpage(event):
            try:
                pygame.mixer.init()
                pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/without_me.mp3")
                pygame.mixer.music.play(-1)
                controller.show_frame(pg51)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg43)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg44.png')
        resize = my_image.resize((1500, 850))
        img1 = ImageTk.PhotoImage(resize)
        imagelabel = Label(frame, image= img1, borderwidth=0)
        imagelabel.image = img1
        imagelabel.pack()
        #imagelabel.bind('<Button-1>', nextpage)
        imagelabel.bind('<Button-3>', prevpage)
        
        buttonframe = tk.Label(self, bg='black', text='He should definitely turn back', fg='white', font=myfont21)
        buttonframe.pack(pady=100)
        buttonframe.bind('<Button-1>', nextpage)
        
        buttonframe = tk.Label(self, bg='black', text='He must not, it is not worth anyway.', fg='white', font=myfont21)
        buttonframe.pack(pady=80)
        buttonframe.bind('<Button-1>', newtpage)


        textframe = tk.Frame(frame, bg='maroon')
        textframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

        txt1area = Text(textframe,  bg='maroon', fg='white', font= myfont22, borderwidth=0,)
        txt1area.place(relwidth=0.95, relheight=1, relx=0.03, rely=0)
        def openDFile():
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg44.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg44.envi', 'r')
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




class pg45(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg46)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg44)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg45.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg45.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg45.envi', 'r')
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




class pg46(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/perfect.mp3")
                pygame.mixer.music.play(-1)
                controller.show_frame(pg47)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/say_something.mp3")
                pygame.mixer.music.play(-1)
                controller.show_frame(pg45)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg46.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg46.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg46.envi', 'r')
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




class pg47(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg48)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg46)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg47.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg47.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg47.envi', 'r')
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




class pg48(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg49)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg47)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg48.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg48.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg48.envi', 'r')
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




class pg49(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg50)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg48)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg49.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg49.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg49.envi', 'r')
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




class pg50(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pgend)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg49)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg50.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg50.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg50.envi', 'r')
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
        
        

class pg51(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pg52)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load("ENVI/ENVI Projects/Personal-project/music-folder/say_something.mp3")
                pygame.mixer.music.play(-1)
                controller.show_frame(pg44)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg51.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg51.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg51.envi', 'r')
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
        
        
        

class pg52(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        def returntitle(event):
            res = messagebox.askquestion('Return to Title Screen?', 'Are you sure you want to go back to Title Screen? All unsaved progress will be lost.')
            if res == 'yes':
                pygame.mixer.music.stop()
                playonHpage()
                controller.show_frame(Homepage)
            elif res == 'no':
                exit
            else:
                messagebox.showwarning('Error', 'Something went wrong!')

        def nextpage(event):
            try:
                controller.show_frame(pgend)
            except NameError:
                controller.show_frame(pgend)


        def prevpage(event):
            try:
                controller.show_frame(pg51)
            except NameError:
                controller.show_frame(pgend)



        frame = tk.Frame(self, bg='black')
        frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        my_image=Image.open('ENVI/ENVI Projects/Personal-project/img-folder/pg52.png')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/lines/pg52.envi', 'r')
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
            tf = open('ENVI/ENVI Projects/Personal-project/text-folder/characters/pg52.envi', 'r')
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