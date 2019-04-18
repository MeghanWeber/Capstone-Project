from guizero import Combo, App, Box, Text, Slider, TextBox, ButtonGroup, PushButton, CheckBox, MenuBar
import subprocess
import signal
import os
import sys

#Pulled in the necessary tools to create the GUI

class MyGUI: 
    def __init__(self, master):
        self.master = master
       #Creates the application window

        self.space2 = Text(master, text=" ", grid=[0,0], width="fill")

        #Creates text for waveform shape
        self.Shapemessage1 = Text(master, size=18, text="  Waveform Shape:", grid=[0,2], align="left", font="Times")
        

        #Creates the waveform buttons
        self.Waveform1 = PushButton(master, text="Normal", grid=[6,1,2,1], width = "10", command = self.normal)
        self.Waveform1.text_size = 12
        self.Waveform2 = PushButton(master, text="Abnormal", grid=[6,2,2,1], width="10", command = self.abnormal)
        self.Waveform2.text_size = 12
        self.Waveform3 = PushButton(master, text="Leveled", grid=[6,3,2,1], width="10",  command = self.leveled)
        self.Waveform3.text_size = 12

        self.space2 = Text(master, text=" ", grid=[0,6])
        self.space2 = Text(master, text=" ", grid=[0,7])

        #Creates space between Waveform Shape and Heart Rate

        self.HRmessage = Text(master, size=18, text="  Heart Rate:", grid=[0,10], align="left", font="Times")
        #Creates the HR subtitle

        self.rate = TextBox(master, grid=[6,10,2,1])
        self.rate.text_size = 20
        self.rate.width = 8
        self.HRunit = Text(master, size=18, text="BPM", grid=[8,10], font="Times")
        #Creates the HR textbox to allow for typed input

        self.space3 = Text(master, text=" ", grid=[0,11], font="Times")
        self.space3 = Text(master, text=" ", grid=[0,12], font="Times")
        self.space3 = Text(master, text=" ", grid=[0,13], font="Times")
        #Creates space between Heart Rate and the Update Button

        self.button = PushButton(master, command=self.update_value, width="12", height="3", text="Update", grid=[0,16,9,1], align="bottom")
        self.button.text_size = 18
        self.button.font = "Times New Roman"
        #Creates an Update Button that updates the inputed information and exports the user-inputs to the next part of the program
        
        
        self.when_clicked = self.update_value
        
        
        self.space3 = Text(master,text = " ", grid = [0,17])
        self.button = PushButton(master, command=self.quit, width="8", height="3", text="Quit", grid=[0,18,9,1], align="bottom")
        self.button.text_size = 15
        self.button.font = "Times New Roman"
        self.button.text_color = "red"
        #Creates the quit button which will exit out of app and stop the process from running

        self.pid = -1 #Initialize process id


    #Colors the Normal button black while other buttons go back to grey
    def normal(self):
        self.done()
        self.waveform = "normal"
        self.Waveform1.bg = (0,0,0)
        self.Waveform1.text_color = (255,255,255)
        self.Waveform2.bg = (214,214,214)
        self.Waveform3.bg = (214,214,214)
    
    
    #Colors the abnormal button black while other buttons go back to grey    
    def abnormal(self):
        self.done()
        self.waveform = "abnormal"
        self.Waveform2.bg = (0,0,0)
        self.Waveform2.text_color = (255,255,255)
        self.Waveform1.bg = (214,214,214)
        self.Waveform3.bg = (214,214,214)


    #Colors the leveled button black while other buttons go back to grey    
    def leveled(self):
        self.done()
        self.waveform = "leveled"
        self.Waveform3.bg = (0,0,0)
        self.Waveform3.text_color = (255,255,255)
        self.Waveform1.bg = (214,214,214)
        self.Waveform2.bg = (214,214,214)


    #Command for updating the heart rate value
    #Also calls specific waveoform value based off of which button is pressed
    def update_value(self):
        self.done()
        if self.rate.value == "":
            self.rate.value=65
        if self.waveform == "normal":
            self.process = subprocess.Popen('python normal.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid       
        

        if self.waveform == "abnormal":
            self.process = subprocess.Popen('python abnormal.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid


        if self.waveform == "leveled":
            self.process = subprocess.Popen('python leveled.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid


    #Kills the process that is currently running
    def done(self):
        if self.pid > 0:
            try:
                os.killpg(os.getpgid(self.pid), signal.SIGTERM)
                self.pid = -1
            except ProcessLookupError:
                pass
    #Kills all processes and closes the window
    def quit(self):
        self.done()
        self.master.destroy()   
root = App(title="Intracranial Pressure Waveform", width=400, height=500, layout="grid")
#Pulls up the GUI
my_gui = MyGUI(root)
root.display()
#Creates then application window
