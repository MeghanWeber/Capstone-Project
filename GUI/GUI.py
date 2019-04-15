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


        self.Shapemessage1 = Text(master, size=18, text="Waveform Shape:", grid=[0,2], align="left", font="Times")
        
        self.Waveform1 = PushButton(master, text="Normal", grid=[1,1], width = "10", command = self.show_choices1)
        self.Waveform2 = PushButton(master, text="Abnormal", grid=[1,2], width="10", command = self.show_choices2)
        self.Waveform3 = PushButton(master, text="Leveled", grid=[1,3], width="10",  command = self.show_choices3)

        #self.Waveform1.toggle()
        #self.Waveform2.toggle()
        #self.Waveform3.toggle()

        self.combo1 = Combo(master, options=["10","11","12","13","14","15","16","17"], grid=[2,1], command=self.modelone)
        self.combo2 = Combo(master, options=["17","18","19","20","21","22","23","24","25","26"], grid=[2,2], command=self.modeltwo)
        self.combo3 = Combo(master, options=["0"], grid=[2,3], command=self.modelthree)

        self.combo1.disable()
        self.combo2.disable()
        self.combo3.disable()
        #Creates the three waveform buttons as well as the selection for ICP value
        #When the waveform selected the user is then able to select an ICP value

        self.space2 = Text(master, text=" ", grid=[0,6])
        #Creates space between Waveform Shape and Heart Rate

        self.HRmessage = Text(master, size=18, text="Heart Rate:", grid=[0,10], align="left", font="Times")
        #Creates the HR subtitle

        self.rate = TextBox(master, grid=[1,10])
        self.HRunit = Text(master, size=15, text="BPM", grid=[2,10], font="Times")
        #Creates the HR textbox to allow for typed input

        self.space3 = Text(master, text=" ", grid=[0,11], font="Times")
        #Creates space between Heart Rate and the Update Button

        self.button = PushButton(master, command=self.update_value, width="12", height="10", text="Update", grid=[0,13,2,2], align="bottom")
        #Creates an Update Button that updates the inputed information and exports the user-inputs to the next part of the program
        self.when_clicked = self.update_value
        #self.when_mouse_enters = self.update_value
        #Creates the update button, no new code will be executed until update button is pressed
        
        self.button = PushButton(master, command=self.calibration, width="12", height="4", text="Zero", grid=[2,13], align="bottom")
        #Creates zero button which is used to calibrate
        
        self.button = PushButton(master, command=self.quit, width="12", height="4", text="Quit", grid=[2,14], align="bottom")
        #Creates the quit button which will exit out of app and stop the process from running

        self.pid = -1 #Initialize process id


    #Launches the function for modelone , Normal ICP, in a seperate python process and obtains the process ID
    def modelone(self):
        self.done()

    #Launches the function for modeltwo , Leveled ICP, in a seperate python process and obtains the process ID    
    def modeltwo(self):
        self.done()

    #Launches the function for modelthree, Abnormal ICP, in a seperate python process and obtains the process ID    
    def modelthree(self):
        self.done()
    
    #Launches the calibration
    def calibration(self):
        self.done()
        self.process = subprocess.Popen('python calibration.py', shell=True, preexec_fn=os.setsid)
        self.pid = self.process.pid

    #Used to show the ICP value choices for the normal waveform
    def show_choices1(self):
        self.done()
        if self.Waveform1.value == 0:
            self.combo1.enable()
            self.combo2.disable()
            self.combo3.disable()
        if self.Waveform1.value == 1:
            self.combo1.disable()
            self.combo1.value = 0

    #Used to show the ICP value choices for the abnormal waveform
    def show_choices2(self):
        self.done()
        if self.Waveform2.value == 0:
            self.combo2.enable()
            self.combo1.disable()
            self.combo3.disable()
        if self.Waveform2.value == 1:
            self.combo2.disable()
            self.combo2.value = 0

    #Used to show the ICP value choices for the leveled waveform
    def show_choices3(self):
        self.done()
        if self.Waveform3.value == 0:
            self.combo3.enable()
            self.combo1.disable()
            self.combo2.disable()
        if self.Waveform3.value == 1:
            self.combo3.disable()
            self.combo3.value = 0    

    #Command for updating the heart rate value
    def update_value(self):
        if self.rate.value == "":
            self.rate.value=65
        if self.combo1.value == "10":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "11":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "12":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "13":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "14":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "15":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "16":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == "17":
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid       
        

        if self.combo2.value == 21:
            self.process = subprocess.Popen('python modeltwo.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == 22:
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == 23:
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == 24:
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == 25:
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid
        if self.combo1.value == 26:
            self.process = subprocess.Popen('python modelone.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid


        if self.combo3.value == 0:
            self.process = subprocess.Popen('python modelthree.py {}'.format(self.rate.value), shell=True, preexec_fn=os.setsid)
            self.pid = self.process.pid


        self.combo1.disable()
        self.combo2.disable()
        self.combo3.disable()
 
    #Kills the process that is currently running
    def done(self):
        if self.pid > 0:
            try:
                os.killpg(os.getpgid(self.pid), signal.SIGTERM)
                self.pid = -1
            except ProcessLookupError:
                pass
    def quit(self):
        self.done()
        self.master.destroy()   
root = App(title="Intracranial Pressure Waveform Simulator", width=450, height=450, layout="grid")
#Pulls up the GUI
my_gui = MyGUI(root)
root.display()
#Creates then application window
