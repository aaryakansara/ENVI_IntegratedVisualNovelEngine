import os
import tkinter as tk
import shutil
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image 


self = tk.Tk()
self.title('Create New Project')
self.resizable(True, True)
self.state("zoomed")

img_folder="ENVI_algo/ENVI-Projects/Personal-project/img-folder/"
music_folder="ENVI_algo/ENVI-Projects/Personal-project/music-folder/"
text_folder="ENVI_algo/ENVI-Projects/Personal-project/text-folder/"
self.counter = 0
myfont42 =("Microsoft YaHei UI", 25, "bold")

def mainalgorithm():
    def minus():
        
        if self.counter <1:
            self.counter=0
        else:
            self.counter -= 1
        #L['text'] = 'Button clicked: ' + str(self.counter)
        
    def plus():
        self.counter -= 1
        #L['text'] = 'Button clicked: ' + str(self.counter)
        

def loadmusic():
    
            filenamem = filedialog.askopenfilename(initialdir="C:/Users/Admin/Music", title="Select Your Music File",
            filetypes=(("MP3","*.mp3"), ("WAV", "*.wav"), ("AAC", "*.aac"), ("3GP", "*.3gp"), ("WEBM", "*.webm")))
            
            try:
                copy = shutil.copy(filenamem, music_folder)
            except FileNotFoundError:
                print("In Create New Project, no music file was selected")  
            
canvas = tk.Canvas(self, height=700, width=1340, bg="white")
canvas.pack()

frame = tk.Frame(self, bg="#6495ED")
frame.place(relwidth=1, relheight=1, relx=0, rely=0)

frameG = tk.Frame(self, bg="grey")
frameG.place(relwidth=1, relheight=0.010, relx=0, rely=0)

frameT = tk.Frame(self, bg="goldenrod1")
frameT.place(relwidth=1, relheight=0.036, relx=0, rely=0.002)

taskfile = tk.Frame(frameT, bg="red2")
taskfile.place(relwidth=0.04, relheight=0.9, relx=0.0009, rely=0.05)
        
bfile = tk.Label(taskfile, text="File", fg="white", padx=25, pady=15, font=('Microsoft YaHei UI', 10, "bold"), bg="red2") #
bfile.pack()

def fileinformation():
    tk.messagebox.showinfo(title="Help", 
    message="File Section can be used to open New or \nExisting project lined up in your system.\n\n"+
    "Also you can save your file in two categories.\n\nCheck out help section in Compile.")

m1 = Menu(bfile, tearoff = 0)
m1.add_command(label ="Open Existing Project")
m1.add_command(label ="New Project")
m1.add_separator()
m1.add_command(label ="Save (Ctrl + S)")
m1.add_command(label ="Save as (Ctrl + F8)")
m1.add_separator()
m1.add_command(label ="Help", command=fileinformation)
def do_popup(event):
            try:
                m1.tk_popup(event.x_root, event.y_root)
            finally:
                m1.grab_release()
        
bfile.bind("<Button-1>", do_popup)
              
taskcompile = tk.Frame(frameT, bg="grey")
taskcompile.place(relwidth=0.06009, relheight=0.9, relx=0.042, rely=0.05)
bcompile = tk.Label(taskcompile, text="Compile", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2")
bcompile.pack()

def compileinformation():
    tk.messagebox.showinfo(title="Help: Know the difference?", 
    message="Compilation of your Project is possible in two formats:\n\n"+
    "Compiling in ENVI format, saves it in Python file, that allows you to run your file in Test Mode.\n\n"+
    "Compiling in an Executable file, it can be easily run on any Windows system.\n\n\n\nGeneral Advice: \n\n"+
    "Compiling in ENVI format helps you identify any unfound mistakes in the process "+
    "and once you're done you can compile it in an Executable.")
    
m2 = Menu(bcompile, tearoff = 0)
m2.add_command(label ="Compile in ENVI editor format")
m2.add_separator()
m2.add_command(label ="Compile in Executable file")
m2.add_separator()
m2.add_command(label ="Help: Know the difference?", command=compileinformation)
def do_popup(event):
            try:
                m2.tk_popup(event.x_root, event.y_root)
            finally:
                m2.grab_release()
        
bcompile.bind("<Button-1>", do_popup)
        
taskview = tk.Frame(frameT, bg="grey")
taskview.place(relwidth=0.04, relheight=0.9, relx=0.1025, rely=0.05)
bview = tk.Label(taskview, text="View", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2")
bview.pack()
m3 = Menu(bview, tearoff = 0)
m3.add_command(label ="View Page Number: (Ctrl + F)")
m3.add_separator()
m3.add_command(label ="View Fullscreen Mode",)  
def do_popup(event):
            try:
                m3.tk_popup(event.x_root, event.y_root)
            finally:
                m3.grab_release()
        
bview.bind("<Button-1>", do_popup)
        
taskedit = tk.Frame(frameT, bg="grey")
taskedit.place(relwidth=0.04, relheight=0.9, relx=0.1435, rely=0.05)
bedit = tk.Label(taskedit, text="Edit", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2",)# command=lambda: controller.show_frame(Pagetakeskipinfo),)# relief=SUNKEN)
bedit.pack()
        
taskback = tk.Frame(frameT, bg="grey")
taskback.place(relwidth=0.03, relheight=0.9, relx=0.938, rely=0.05)
bback = tk.Label(taskback, text="←", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="#FF7256",)# command=warn)
bback.pack()
bback.bind("<Button-1>",)# warn)
        
taskhelp = tk.Frame(frameT, bg="grey")
taskhelp.place(relwidth=0.03, relheight=0.9, relx=0.9685, rely=0.05)
buthelp = tk.Label(taskhelp, text= "?", padx=25, pady=25, fg="white", font=("Arial",10, "bold"), bg="red2")
buthelp.pack()



frame = tk.Frame(self, bg="lightblue")
frame.place(relwidth=0.3, relheight=0.919, relx=0.01, rely=0.06)
v = Scrollbar(frame)
v.pack(side = RIGHT, fill = Y)

frame0 = tk.Frame(self, bg="lightblue")
frame0.place(relwidth=0.6665, relheight=0.66, relx=0.32, rely=0.06)
        
mainframe = tk.Frame(frame0, bg="grey")
mainframe.place(relwidth=0.99, relheight=0.98, relx=0.005, rely=0.01)

def graphic():
    try:
        filenameg = filedialog.askopenfilename(initialdir="/", title="Select Image or Video File",
        filetypes=(("JPG","*.jpg"), ("PNG","*.png"), ("MP4","*.mp4"), ("MKV","*.mkv"), ("All Files", "*.*")))
        
        copy = shutil.copy(filenameg, img_folder)
        
        file_name= os.path.basename(filenameg)
        file=(img_folder+file_name)
        #print(file)
        new_path=(file)
        
        my_image=Image.open(filenameg)
        resize = my_image.resize((900, 460))
        img1 = ImageTk.PhotoImage(resize)
        badd1 = Label(mainframe, image= img1, borderwidth=0)
        badd1.image = img1
        badd1.pack()
        
        def anotherimg():
            os.remove(file)
            graphic()
            badd1.pack_forget()
            
        def deleteimg():
            os.remove(file)
            badd1.pack_forget()
            badd.pack()
            
        def information():
            tk.messagebox.showinfo(title="Help", message=None)
            
        m = Menu(taskfile, tearoff = 0)
        m.add_command(label ="Add another image or video", command=anotherimg)
        m.add_command(label ="Delete current image or video", command=deleteimg)
        m.add_separator()
        m.add_command(label ="Copy")
        m.add_command(label ="Paste")
        m.add_separator()
        m.add_command(label ="Help", command=information)
        
        
        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()
        
        badd1.bind("<Button-3>", do_popup)
        badd.pack_forget()
    except FileNotFoundError:
        print("No file was selected")

photo = Image.open("ENVI_algo/gui/logo/addimage.png")
resize = photo.resize((950, 700))
img = ImageTk.PhotoImage(resize)
badd = tk.Button(mainframe, text="+ADD IMAGE OR VIDEO", padx=600, pady=300, fg="white", image= img, borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="grey",relief=SUNKEN, command=graphic)# command=lambda: controller.show_frame(FlowmapPage))
badd.pack()



prevbuttonframe = tk.Frame(frame0, bg="#6495ED")
prevbuttonframe.place(relwidth=0.05, relheight=0.1, relx=0, rely=0.45)
prevbutton = tk.Button(prevbuttonframe, text="<", padx=95, pady=10, fg="white", borderwidth=0, font=("bold", 30), bg="darkorchid", )
prevbutton.pack()

nextbuttonframe = tk.Frame(frame0, bg="#6495ED")
nextbuttonframe.place(relwidth=0.05, relheight=0.1, relx=0.95, rely=0.45)
nextbutton = tk.Button(nextbuttonframe, text=">", padx=95, pady=10, fg="white", borderwidth=0, font=("bold", 30), bg="darkorchid", )
nextbutton.pack()

textframe1 = tk.Frame(frame0, bg="lightgrey")
textframe1.place(relwidth=0.2, relheight=0.05, relx=0.02, rely=0.700)
textframe2 = tk.Frame(frame0, bg="white")
textframe2.place(relwidth=1, relheight=0.25, relx=0, rely=0.750)


def pgfileminus():
        
        if self.counter <1:
            self.counter=0
        else:
            self.counter -= 1


my_text1=Text(textframe1, width=100, height=10,font=('Helvetica',12,), bg="lightgrey")#)
my_text1.pack()
text_file=open("ENVI_algo/gui/temp/script1.envi",'r')
content=text_file.read()
my_text1.insert(END, content)
text_file.close()
# def save_txt1():
#     save_file=open(pgsavefilechar,'w')
#     save_file.write(my_text1.get(1.0, END))


my_text2=Text(textframe2, width=100, height=10,font=('Helvetica',16))
my_text2.pack()
text_file=open("ENVI_algo/gui/temp/script2.envi",'r')
content=text_file.read()
my_text2.insert(END, content)
text_file.close()
# def save_txt2():
#     save_file=open(pgsavefileline,'w')
#     save_file.write(my_text2.get(1.0, END))
    
def writealgorithm():
    def pgfileplus():
        self.counter += 1
    #L['text'] = 'Button clicked: ' + str(self.counter)
    pgfileplus()
    
    pgsavefilechar = text_folder+"characters/"+"pg"+str(self.counter)+".envi"
    pgsavefileline = text_folder+"lines/"+"pg"+str(self.counter)+".envi"    
        
    def create():
        try:
            with open(pgsavefilechar, 'w') as f:
                f.write('')
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
            
        try:
            with open(pgsavefileline, 'w') as f:
                f.write('')
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
    create()
            
    def save_txt1():
        save_file=open(pgsavefilechar,'w')
        save_file.write(my_text1.get(1.0, END))
    save_txt1()
        
    def save_txt2():
        save_file=open(pgsavefileline,'w')
        save_file.write(my_text2.get(1.0, END))
    save_txt2()
    
    
    

def parametersettings():
    paraframe= tk.Frame(bg="#6495ED")
    paraframe.place(relwidth=1, relheight=1, relx=0, rely=0)
    
    innerparaframe1= tk.Frame(paraframe, bg="lightblue")
    innerparaframe1.place(relwidth=0.380, relheight=0.8, relx=0.1, rely=0.1)
    
    innerparaframe2= tk.Frame(paraframe, bg="lightblue")
    innerparaframe2.place(relwidth=0.380, relheight=0.8, relx=0.520, rely=0.1)
    
    
    
    aboutfileloc= "ENVI/ENVI Projects/Personal-Project/text-folder/AboutProject.envi"
    credfileloc= "ENVI/ENVI Projects/Personal-Project/text-folder/ProjectCredits.envi"
    
    def editabout():
        try:
            textingframe=Frame(innerparaframe2, bg="lightblue")
            textingframe.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.1)
            about_text=Text(textingframe, width=100, height=100,font=('Helvetica',16))
            about_text.pack(anchor="s")
            about_file=open(aboutfileloc,'r')
            content=text_file.read()
            about_text.insert(END, content)
            about_file.close()
        except ValueError:
            print("Nothing was typed or changed")
        
    def editcredit():
        try:
            textingframe=Frame(innerparaframe2, bg="lightblue")
            textingframe.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.1)
            credit_text=Text(textingframe, width=100, height=100,font=('Helvetica',16))
            credit_text.pack(anchor="center")
            cred_file=open(credfileloc,'r')
            content=text_file.read()
            credit_text.insert(END, content)
            cred_file.close()
        except ValueError:
            print("Nothing was typed or changed")
        
    def closeframe():
            paraframe.destroy()
            
            
    buttonframe = tk.Frame(innerparaframe1, bg="#6495ED")
    buttonframe.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.2)
    bflow = tk.Button(buttonframe, text="ABOUT SECTION", padx=700, pady=700, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 20, "bold"), bg="red",command=editabout)
    bflow.pack()
    
    buttonframe = tk.Frame(innerparaframe1, bg="#6495ED")
    buttonframe.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.6)
    bflow = tk.Button(buttonframe, text="CREDITS SECTION", padx=700, pady=700, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 20, "bold"), bg="red",command=editcredit)
    bflow.pack()
            
    showbt = Button(paraframe, text="Return", borderwidth=0, fg="gray1", bg="lightblue", font=myfont42, command=closeframe)
    showbt.place(x=1180, y=600)
        



frame1 = tk.Frame(self, bg="lightblue")
frame1.place(relwidth=0.6665, relheight=0.2385, relx=0.32, rely=0.74045)

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.02, rely=0.16)
bmusic = tk.Button(buttonframe, text="MUSIC", padx=95, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103", command=loadmusic)
bmusic.pack()

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.364, rely=0.16)
bflow = tk.Button(buttonframe, text="FLOW MAP", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103",)# command=lambda: controller.show_frame(FlowmapPage))
bflow.pack()

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.705, rely=0.16)
bbranch = tk.Button(buttonframe, text="BRANCH OPTIONS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bbranch.pack()

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.02, rely=0.6)
bimageset = tk.Button(buttonframe, text="IMAGE SETTINGS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bimageset.pack()

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.364, rely=0.6)
bparaset = tk.Button(buttonframe, text="PARAMETER SETTINGS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103", command=parametersettings)
bparaset.pack()

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.705, rely=0.6)
bsandn = tk.Button(buttonframe, text="SAVE & NEXT", padx=75, pady=10, fg="white", font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103", command=writealgorithm)#command=lambda: [pgfileplus(),create(), save_txt1(), save_txt2(),])
bsandn.pack() 



       
        
        
self.mainloop()