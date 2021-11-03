import csv
from PyQt5 import QtCore, QtGui, QtWidgets
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
        for row in csvreader:
            rows.append(row)
    csvfile.close()
    return makeProjObjects(rows)
def makeProjObjects(rows):
    for i in range(len(rows)):
        p = virtualProjects()
        p.title = rows[i][1]
        p.category = rows[i][2]
        p.name = rows[i][3]
        p.cost = rows[i][4]
        p.delivery = rows[i][5]
        p.reviews = rows[i][6]
        p.ratings = rows[i][7]
        rows[i] = p
    return rows
def loadDataInTable(self):
        data = loadDataCSV()
        for i in range(0,len(data)):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(i , 0 , QtWidgets.QTableWidgetItem(data[i].title))
            self.tableWidget.setItem(i , 1 , QtWidgets.QTableWidgetItem(data[i].category))
            self.tableWidget.setItem(i , 2 , QtWidgets.QTableWidgetItem(data[i].name))
            self.tableWidget.setItem(i , 3 , QtWidgets.QTableWidgetItem(data[i].cost))
            self.tableWidget.setItem(i , 4 , QtWidgets.QTableWidgetItem(data[i].delivery))
            self.tableWidget.setItem(i , 5 , QtWidgets.QTableWidgetItem(data[i].reviews))
            self.tableWidget.setItem(i , 6 , QtWidgets.QTableWidgetItem(data[i].ratings))
