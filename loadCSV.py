import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import*



global array1
array1 = []
class virtualProjects:
    title = ""
    category = ""
    name = ""
    ratings = 0
    reviews = 0
    delivery = 0
    cost = 0
def loadDataCSV():
    rows = []
    with open("AllProjects.csv", 'r') as csvfile:
    # creating a csv reader object
        csvreader = csv.reader(csvfile)
        next(csvreader)
    # extracting each data row one by one
        i = 0
        for row in csvreader:
            rows.append(row)
            i+=1
    csvfile.close()
    makeProjObjects(rows)
def makeProjObjects(rows):
    global array1
    array1 = []
    for i in range(len(rows)):
        p = virtualProjects()
        p.title = rows[i][1]
        p.category = rows[i][2]
        p.name = rows[i][3]
        p.cost = rows[i][4].replace(".","").replace(",","")


        p.delivery = rows[i][5]
        p.reviews = rows[i][6]
        p.ratings = rows[i][7]
        rows[i] = p
    array1 = rows
def loadDataInTable(self):
        t = Thread(target=loadDataCSV())
        t.start()
        t.join()
        # print(array1[0])
        for i in range(0,len(array1)):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(i , 0 , QtWidgets.QTableWidgetItem(array1[i].title))
            self.tableWidget.setItem(i , 1 , QtWidgets.QTableWidgetItem(array1[i].category))
            self.tableWidget.setItem(i , 2 , QtWidgets.QTableWidgetItem(array1[i].name))
            self.tableWidget.setItem(i , 3 , QtWidgets.QTableWidgetItem(array1[i].cost))
            self.tableWidget.setItem(i , 4 , QtWidgets.QTableWidgetItem(array1[i].delivery))
            self.tableWidget.setItem(i , 5 , QtWidgets.QTableWidgetItem(array1[i].reviews))
            self.tableWidget.setItem(i , 6 , QtWidgets.QTableWidgetItem(array1[i].ratings))
