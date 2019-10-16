#Import Libraries
import os
import subprocess
import sysconfig
import tkinter
import time
import platform
import tkinter.messagebox
import tkinter.scrolledtext as tkst
from tkinter import *

global operate
operate = platform.system()
if operate == "Darwin":
    operate = "OSx"
    
#Variables
global hashCommand
global hashCat
if operate == "Windows":
    hashCat = "hashcat64.exe"
else:
    hashCat = "hashcat"
global deviceType
global attackType
global hashType
global fileOutput
global outputType
global workloadProfile
global ruleType
global rules
global wordList_1
global wordList_2
global attackMask
global hashValue
global hashPathValue
global hashPathEntry
global fileOutputEntry

#Functions
def makeWordlist():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global wordList_1Entry
    attackType = "0"
    ruleType = "0"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    wordList_1Label = Label(topFrame,text="File Path to Wordlist:")
    wordList_1Entry = Entry()
    wordList_1Label.grid(row=6)
    wordList_1Entry.grid(row=6,column=1)

def makeWordlistRules():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global wordList_1Entry
    global rulesEntry
    attackType = "0"
    ruleType = "1"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    wordList_1Label = Label(topFrame,text="File Path to Wordlist:")
    wordList_1Entry = Entry()
    wordList_1Label.grid(row=6)
    wordList_1Entry.grid(row=6,column=1)
    rulesLabel = Label(topFrame,text="File Path to Rules:")
    rulesEntry = Entry()
    rulesLabel.grid(row=7)
    rulesEntry.grid(row=7,column=1)

def makeCombination():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global wordList_1Entry
    global wordList_2Entry
    attackType = "1"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    wordList_1Label = Label(topFrame,text="File Path to Wordlist:")
    wordList_1Entry = Entry()
    wordList_1Label.grid(row=6)
    wordList_1Entry.grid(row=6,column=1)
    wordList_2Label = Label(topFrame,text="File Path to Second Wordlist:")
    wordList_2Entry = Entry()
    wordList_2Label.grid(row=7)
    wordList_2Entry.grid(row=7,column=1)

def makeBruteforce():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global attackMaskEntry
    attackType = "3"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    attackMaskLabel = Label(topFrame,text="Attack Mask:")
    attackMaskEntry = Entry()
    attackMaskLabel.grid(row=6)
    attackMaskEntry.grid(row=6,column=1)

def makeHybridWord():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global wordList_1Entry
    global attackMaskEntry
    attackType = "6"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    wordList_1Label = Label(topFrame,text="File Path to Wordlist:")
    wordList_1Entry = Entry()
    wordList_1Label.grid(row=6)
    wordList_1Entry.grid(row=6,column=1)
    attackMaskLabel = Label(topFrame,text="Attack Mask:")
    attackMaskEntry = Entry()
    attackMaskLabel.grid(row=7)
    attackMaskEntry.grid(row=7,column=1)

def makeHybridMask():
    global attackType
    global ruleType
    global hashTypeEntry
    global hashValueEntry
    global workloadProfileEntry
    global deviceTypeEntry
    global attackMaskEntry
    global wordList_1Entry
    attackType = "7"
    hashTypeLabel = Label(topFrame,text="Hash Type #:")
    hashTypeEntry = Entry()
    hashTypeLabel.grid(row=2)
    hashTypeEntry.grid(row=2,column=1)
    hashValueLabel = Label(topFrame,text="Hash:")
    hashValueEntry = Entry()
    hashValueLabel.grid(row=3)
    hashValueEntry.grid(row=3,column=1)
    workloadLabel = Label(topFrame,text="Workload Profile #:")
    workloadProfileEntry = Entry()
    workloadLabel.grid(row=4)
    workloadProfileEntry.grid(row=4,column=1)
    deviceTypeLabel = Label(topFrame,text="Device Type #:")
    deviceTypeEntry = Entry()
    deviceTypeLabel.grid(row=5)
    deviceTypeEntry.grid(row=5,column=1)
    attackMaskLabel = Label(topFrame,text="Attack Mask:")
    attackMaskEntry = Entry()
    attackMaskLabel.grid(row=6)
    attackMaskEntry.grid(row=6,column=1)
    wordList_1Label = Label(topFrame,text="File Path to Wordlist:")
    wordList_1Entry = Entry()
    wordList_1Label.grid(row=7)
    wordList_1Entry.grid(row=7,column=1)

def generateCommand():
    global hashCommand
    global deviceType
    global attackType
    global hashType
    global fileOutput
    global outputType
    global workloadProfile
    global ruleType
    global rules
    global wordList_1
    global wordList_2
    global attackMask
    global hashValue
    global hashPathValue
    global fileOutputEntry
    outputType = "3"
    if attackType == "0" and ruleType == "0":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        wordList_1 = wordList_1Entry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,wordList_1)
    elif attackType == "0" and ruleType == "1":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        wordList_1 = wordList_1Entry.get()
        rules = rulesEntry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {} -r {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,wordList_1,rules)
    elif attackType == "1":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        wordList_1 = wordList_1Entry.get()
        wordList_2 = wordList_2Entry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {} {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,wordList_1,wordList_2)
    elif attackType == "3":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        attackMask = attackMaskEntry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,attackMask)
    elif attackType == "6":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        wordList_1 = wordList_1Entry.get()
        attackMask = attackMaskEntry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,wordList_1,attackMask)
    elif attackType == "7":
        fileOutput = fileOutputEntry.get()
        hashType = hashTypeEntry.get()
        hashValue = hashValueEntry.get()
        workloadProfile = workloadProfileEntry.get()
        deviceType = deviceTypeEntry.get()
        attackMask = attackMaskEntry.get()
        wordList_1 = wordList_1Entry.get()
        hashCommand = "{} --quiet --potfile-disable --outfile {} --outfile-format {} -w {} -D {} -a {} -m {} {} {}".format(hashCat,fileOutput,outputType,workloadProfile,deviceType,attackType,hashType,hashValue,attackMask,wordList_1)
    showCommandButton = Button(bottomFrame,text="Show Command",command=showCommand)
    showCommandButton.grid(row=1,column=3)
def showCommand():
    global hashCommand
    tkinter.messagebox.showinfo("Hashcat Command",str(hashCommand))

def showHashTypes():
    hashFile = [line.rstrip('\n') for line in open("./hashtypes.txt")]
    hashFileView = ""
    for i in hashFile:
        hashFileView += (str(hashFile) + "\n")
    hashWindow = Tk()
    hashWindow.title("Hash Types")
    frame = tkinter.Frame(hashWindow, bg='white')
    frame.pack(fill='both', expand='yes')
    edit_space = tkst.ScrolledText(
        master = frame,
        wrap = 'word',
        width = 63,
        height = 25,
        bg='beige'
    )
    edit_space.pack(fill='both',expand=True,padx=4,pady=4)
    edit_space.insert('insert', str(hashFileView))
    hashWindow.mainloop()

def showResults():
    global fileOutput
    global fileOutputEntry
    fileOutput = fileOutputEntry.get()
    cwd = os.getcwd()
    print(str(cwd))    
    resultFile = [line.rstrip('\n') for line in open(str(fileOutput))]
    results = ""
    for i in resultFile:
        results += str(i) +"\n"
    tkinter.messagebox.showinfo('Results', str(results))

def showDeviceTypes():
    tkinter.messagebox.showinfo('Device Types',"Devices Types are selected by using their numerical value:\n1.CPU\n2.GPU\3.FPGA, DSP, Co-Processor\nMultiple devices can be used by entering #,# ex: 1,2")
def showWorkload():
    tkinter.messagebox.showinfo('Workload Profiles',"- [ Workload Profiles ] -\n   | Performance | Runtime | Power Consumption | Desktop Impact\n ===+=============+=========+===================+=================\n  1 | Low         |   2 ms  | Low               | Minimal\n  2 | Default     |  12 ms  | Economic          | Noticeable\n  3 | High        |  96 ms  | High              | Unresponsive\n  4 | Nightmare   | 480 ms  | Insane            | Headless")
def showRules():
    tkinter.messagebox.showinfo('Rules',"Hashcat Rules are availible in the same directory as your hashcat install\nRules are used in the wordlist rules attack\nAn entry for the rules input looks like:\nrules/best64.rule")
def showMask():
    maskWindow = Tk()
    maskWindow.title("Attack Masks")
    frame = tkinter.Frame(maskWindow, bg='white')
    frame.pack(fill='both', expand='yes')
    edit_space = tkst.ScrolledText(
        master = frame,
        wrap = 'none',
        width = 100,
        height = 23,
        bg='beige'
    )
    edit_space.pack(fill='both',expand=True,padx=4,pady=4)
    maskText = '''\
    Attack Masks are created using character sets:
    ? | Charset
    ===+=========
    l | abcdefghijklmnopqrstuvwxyz
    u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
    d | 0123456789
    h | 0123456789abcdef
    H | 0123456789ABCDEF
    s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    a | ?l?u?d?s
    b | 0x00 - 0xff  
    Lowercase letters are denoted via ?l
    Uppercase Letters are denoted via ?u
    Digits are denoted via ?d
    Hexdecimal Characters are denoted via ?h and ?H
    Symbols are denoted via ?s  
    An example Attack Mask would Be: ?u?l?l?l?l?l?d?s
    This attack mask would be a 8 Character password starting with an Uppercase Letter,
    Followed by 5 Lowercase Letters, Then One Digit and Lastly One Symbol,  
    You can put multiple masks into a file and use the file as a collection of masks to try.
    '''
    edit_space.insert('insert', maskText)
    maskWindow.mainloop()

def executeCommand():
    global hashCommand
    global hashPathEntry
    global hashPathValue
    hashPathValue = hashPathEntry.get()
    if operate == "Windows" or operate == "OSx":
        os.chdir(str(hashPathValue))
    os.system(str(hashCommand))
    
#tkinter variable
root = Tk()
root.title("Hashcat Automation Utility")
root.geometry("500x300")

#Menu Creation
menu = Menu(root)
root.config(menu=menu)

#SubMenu Creation
attackMenu = Menu(menu)
menu.add_cascade(label="Attack Type", menu=attackMenu)
attackMenu.add_command(label="Wordlist",command=makeWordlist)
attackMenu.add_command(label="Wordlist + Rules",command=makeWordlistRules)
attackMenu.add_command(label="Combination",command=makeCombination)
attackMenu.add_command(label="Brute Force",command=makeBruteforce)
attackMenu.add_command(label="Hybrid Wordlist + Mask",command=makeHybridWord)
attackMenu.add_command(label="Hybrid Mask + Wordlist",command=makeHybridMask)

hashMenu = Menu(menu)
menu.add_command(label="Hash Types",command=showHashTypes)

deviceMenu = Menu(menu)
menu.add_command(label="Device Types",command=showDeviceTypes)

workloadMenu = Menu(menu)
menu.add_command(label="Workloads",command=showWorkload)

rulesMenu = Menu(menu)
menu.add_command(label="Rules",command=showRules)

maskMenu = Menu(menu)
menu.add_command(label="Attack Masks",command=showMask)

#tkinter frames
topFrame = Frame(root)
topFrame.grid(row=0,rowspan=10)
bottomFrame = Frame(root)
bottomFrame.grid(row=11,rowspan=3)


#Hashcat Directory Check for Non UNix Systems
if operate == "Windows" or operate == "OSx":
    hashPathLabel = Label(topFrame,text="Path to folder containing hashcat executable:")
    hashPathEntry = Entry()
    hashPathLabel.grid(row=0)
    hashPathEntry.grid(row=0,column=1)
fileOutputLabel = Label(topFrame,text="File Output Name:")
fileOutputEntry = Entry()
fileOutputLabel.grid(row=1)
fileOutputEntry.grid(row=1,column=1)
#Generate and Execute
generateButton = Button(bottomFrame, text="Generate Command",command=generateCommand)
generateButton.grid(row=1,column=0)
executeButton = Button(bottomFrame,text="Execute Hashcat",command=executeCommand)
executeButton.grid(row=1,column=1)
resultButton = Button(bottomFrame,text="View Results",command=showResults)
resultButton.grid(row=1,column=2)
root.mainloop()