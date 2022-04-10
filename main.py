"""
The Time Box by exdarku.
Inspired from a tiktok I saw.

Base app created in around 2 hours.


Kindly do not remove this if you're modifying the application. But you can add your credits here also!!
Thank you! 
"""

version = 1.0

from PyQt5 import QtWidgets, uic, QtTest, QtGui, QtCore
import os
from datetime import datetime
import time
import pickle

def resource_path(relative_path): # For py2exe
    if hasattr(os.sys, '_MEIPASS'):
        return os.path.join(os.sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class mainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWin, self).__init__()
        self.ui = uic.loadUi(resource_path("main.ui"), self)
        self.ui.closeEvent = self.closeEvent

        self.setWindowIcon(QtGui.QIcon(resource_path("logo.ico")))
        self.setWindowTitle(f"The Time Box | Version {version} | laurencelesmoras.dev")

        # Date box
        self.date_box = self.findChild(QtWidgets.QDateEdit, "dateEdit")
        self.year = datetime.today().strftime('%Y')
        self.month = datetime.today().strftime('%m')
        self.day = datetime.today().strftime('%d')
        self.current_date = QtCore.QDate(int(self.year), int(self.month), int(self.day))
        self.date_box.setDate(self.current_date)


        # Priority Box
        self.topPriority_box1 = self.findChild(QtWidgets.QPlainTextEdit, "topprio1_box")
        self.topPriority_box2 = self.findChild(QtWidgets.QPlainTextEdit, "topprio2_box")
        self.topPriority_box3 = self.findChild(QtWidgets.QPlainTextEdit, "topprio3_box")

        # Brain Dump
        self.brainDump_box = self.findChild(QtWidgets.QTextEdit, "braindump_box")

        # Time Boxes
        # 00
        self.five_box = self.findChild(QtWidgets.QPlainTextEdit, "five00_box")
        self.six_box = self.findChild(QtWidgets.QPlainTextEdit, "six00_box")
        self.seven_box = self.findChild(QtWidgets.QPlainTextEdit, "seven00_box")
        self.eight_box = self.findChild(QtWidgets.QPlainTextEdit, "eight00_box")
        self.nine_box = self.findChild(QtWidgets.QPlainTextEdit, "nine00_box")
        self.ten_box = self.findChild(QtWidgets.QPlainTextEdit, "ten00_box")
        self.eleven_box = self.findChild(QtWidgets.QPlainTextEdit, "eleven00_box")
        self.twelve_box = self.findChild(QtWidgets.QPlainTextEdit, "twelve00_box")
        self.one_box = self.findChild(QtWidgets.QPlainTextEdit, "one00_box")
        self.two_box = self.findChild(QtWidgets.QPlainTextEdit, "two00_box")
        self.three_box = self.findChild(QtWidgets.QPlainTextEdit, "three00_box")
        self.four_box = self.findChild(QtWidgets.QPlainTextEdit, "four00_box")
        self.fivepm_box = self.findChild(QtWidgets.QPlainTextEdit, "five00pm_box")
        self.sixpm_box = self.findChild(QtWidgets.QPlainTextEdit, "six00pm_box")
        self.sevenpm_box = self.findChild(QtWidgets.QPlainTextEdit, "seven00pm_box")
        self.eightpm_box = self.findChild(QtWidgets.QPlainTextEdit, "eight00pm_box")
        self.ninepm_box = self.findChild(QtWidgets.QPlainTextEdit, "nine00pm_box")
        self.tenpm_box = self.findChild(QtWidgets.QPlainTextEdit, "ten00pm_box")
        self.elevenpm_box = self.findChild(QtWidgets.QPlainTextEdit, "eleven00pm_box")

        # 30
        self.five30_box = self.findChild(QtWidgets.QPlainTextEdit, "five30_box")
        self.six30_box = self.findChild(QtWidgets.QPlainTextEdit, "six30_box")
        self.seven30_box = self.findChild(QtWidgets.QPlainTextEdit, "seven30_box")
        self.eight30_box = self.findChild(QtWidgets.QPlainTextEdit, "eight30_box")
        self.nine30_box = self.findChild(QtWidgets.QPlainTextEdit, "nine30_box")
        self.ten30_box = self.findChild(QtWidgets.QPlainTextEdit, "ten30_box")
        self.eleven30_box = self.findChild(QtWidgets.QPlainTextEdit, "eleven30_box")
        self.twelve30_box = self.findChild(QtWidgets.QPlainTextEdit, "twelve30_box")
        self.one30_box = self.findChild(QtWidgets.QPlainTextEdit, "one30_box")
        self.two30_box = self.findChild(QtWidgets.QPlainTextEdit, "two30_box")
        self.three30_box = self.findChild(QtWidgets.QPlainTextEdit, "three30_box")
        self.fou30_box = self.findChild(QtWidgets.QPlainTextEdit, "four30_box")
        self.fivepm30_box = self.findChild(QtWidgets.QPlainTextEdit, "five30pm_box")
        self.sixpm30_box = self.findChild(QtWidgets.QPlainTextEdit, "six30pm_box")
        self.sevenpm30_box = self.findChild(QtWidgets.QPlainTextEdit, "seven30pm_box")
        self.eightpm30_box = self.findChild(QtWidgets.QPlainTextEdit, "eight30pm_box")
        self.ninepm30_box = self.findChild(QtWidgets.QPlainTextEdit, "nine30pm_box")
        self.tenpm30_box = self.findChild(QtWidgets.QPlainTextEdit, "ten30pm_box")
        self.elevenpm30_box = self.findChild(QtWidgets.QPlainTextEdit, "eleven30pm_box")

        # Checking if there is already a data for that day
        if os.path.isfile("data\\TimeBox_" + str(self.year) + str(self.month) + str(self.day) + ".tbx"):
            self.loadData()

        # Checking if there is folder
        try:
            if not os.path.isfile("data\\init_file"):
                os.mkdir("data")
                f = open("data\\init_file", "a")
                f.write("Just an init file, nothing special.")
                f.close()
        except:
            pass

        self.show()

        # Auto Save Function
        self.saveData()
            
    def closeEvent(self, event):
        quit()

    def loadData(self):
        infile = open("data\\TimeBox_" + str(self.year) + str(self.month) + str(self.day) + ".tbx",'rb')
        data = pickle.load(infile)
        infile.close()

        self.brainDump_box.setPlainText(data["brain_dump"])
        self.topPriority_box1.setPlainText(data["top_priority_1"])
        self.topPriority_box2.setPlainText(data["top_priority_2"])
        self.topPriority_box3.setPlainText(data["top_priority_3"])

        self.five_box.setPlainText(data["five"])
        self.six_box.setPlainText(data["six"])
        self.seven_box.setPlainText(data["seven"])
        self.eight_box.setPlainText(data["eight"])
        self.nine_box.setPlainText(data["nine"])
        self.ten_box.setPlainText(data["ten"])
        self.eleven_box.setPlainText(data["eleven"])
        self.twelve_box.setPlainText(data["twelve"])
        self.one_box.setPlainText(data["one"])
        self.two_box.setPlainText(data["two"])
        self.three_box.setPlainText(data["three"])
        self.four_box.setPlainText(data["four"])
        self.fivepm_box.setPlainText(data["fivepm"])
        self.sixpm_box.setPlainText(data["sixpm"])
        self.sevenpm_box.setPlainText(data["sevenpm"])
        self.eightpm_box.setPlainText(data["eightpm"])
        self.ninepm_box.setPlainText(data["ninepm"])
        self.tenpm_box.setPlainText(data["tenpm"])
        self.elevenpm_box.setPlainText(data["elevenpm"])

        self.five30_box.setPlainText(data["five30"])
        self.six30_box.setPlainText(data["six30"])
        self.seven30_box.setPlainText(data["seven30"])
        self.eight30_box.setPlainText(data["eight30"])
        self.nine30_box.setPlainText(data["nine30"])
        self.ten30_box.setPlainText(data["ten30"])
        self.eleven30_box.setPlainText(data["eleven30"])
        self.twelve30_box.setPlainText(data["twelve30"])
        self.one30_box.setPlainText(data["one30"])
        self.two30_box.setPlainText(data["two30"])
        self.three30_box.setPlainText(data["three30"])
        self.four30_box.setPlainText(data["four30"])
        self.five30pm_box.setPlainText(data["five30pm"])
        self.six30pm_box.setPlainText(data["six30pm"])
        self.seven30pm_box.setPlainText(data["seven30pm"])
        self.eight30pm_box.setPlainText(data["eight30pm"])
        self.nine30pm_box.setPlainText(data["nine30pm"])
        self.ten30pm_box.setPlainText(data["ten30pm"])
        self.eleven30pm_box.setPlainText(data["eleven30pm"])
        
        

    def saveData(self):
        while True:
            data = {
                "year": self.year,
                "month": self.month,
                "day": self.day,
                "brain_dump": self.brainDump_box.toPlainText(),
                "top_priority_1": self.topPriority_box1.toPlainText(),
                "top_priority_2": self.topPriority_box2.toPlainText(),
                "top_priority_3": self.topPriority_box3.toPlainText(),
                "five": self.five_box.toPlainText(),
                "six": self.six_box.toPlainText(),
                "seven": self.seven_box.toPlainText(),
                "eight": self.eight_box.toPlainText(),
                "nine": self.nine_box.toPlainText(),
                "ten": self.ten_box.toPlainText(),
                "eleven": self.eleven_box.toPlainText(),
                "twelve": self.twelve_box.toPlainText(),
                "one": self.one_box.toPlainText(),
                "two": self.two_box.toPlainText(),
                "three": self.three_box.toPlainText(),
                "four": self.four_box.toPlainText(),
                "fivepm": self.fivepm_box.toPlainText(),
                "sixpm": self.sixpm_box.toPlainText(),
                "sevenpm": self.sevenpm_box.toPlainText(),
                "eightpm": self.eightpm_box.toPlainText(),
                "ninepm": self.ninepm_box.toPlainText(),
                "tenpm": self.tenpm_box.toPlainText(),
                "elevenpm": self.elevenpm_box.toPlainText(),

                "five30": self.five30_box.toPlainText(),
                "six30": self.six30_box.toPlainText(),
                "seven30": self.seven30_box.toPlainText(),
                "eight30": self.eight30_box.toPlainText(),
                "nine30": self.nine30_box.toPlainText(),
                "ten30": self.ten30_box.toPlainText(),
                "eleven30": self.eleven30_box.toPlainText(),
                "twelve30": self.twelve30_box.toPlainText(),
                "one30": self.one30_box.toPlainText(),
                "two30": self.two30_box.toPlainText(),
                "three30": self.three30_box.toPlainText(),
                "four30": self.four30_box.toPlainText(),
                "five30pm": self.fivepm30_box.toPlainText(),
                "six30pm": self.sixpm30_box.toPlainText(),
                "seven30pm": self.sevenpm30_box.toPlainText(),
                "eight30pm": self.eightpm30_box.toPlainText(),
                "nine30pm": self.ninepm30_box.toPlainText(),
                "ten30pm": self.tenpm30_box.toPlainText(),
                "eleven30pm": self.elevenpm30_box.toPlainText(),
            }
            self.filename = "TimeBox_" + str(self.year) + str(self.month) + str(self.day) + ".tbx"
            outfile = open("data\\" + self.filename,'wb') # Opening File
            pickle.dump(data,outfile) # Dumping data
            outfile.close() # Closing
            QtTest.QTest.qWait(5000) # Waiting for 5 seconds


app = QtWidgets.QApplication(os.sys.argv)
window = mainWin()
os.sys.exit(app.exec())