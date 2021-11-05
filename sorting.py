import time
import Codes.allSortingAlgorithms
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import*
import sys
from PyQt5.QtWidgets import QMessageBox
def updateAllArrays(allData , Indexes):
    newUpdatedArrays = [[]for j in range(len(Indexes))]
    idx = 0
    for i in Indexes:
        newUpdatedArrays[idx].append(allData[1][i])
        newUpdatedArrays[idx].append(allData[2][i])
        newUpdatedArrays[idx].append(allData[3][i])
        newUpdatedArrays[idx].append(allData[4][i])
        newUpdatedArrays[idx].append(allData[5][i])
        newUpdatedArrays[idx].append(allData[6][i])
        newUpdatedArrays[idx].append(allData[7][i])
        idx += 1
    return newUpdatedArrays




def getColumnFromTable(self):
    row = self.tableWidget.rowCount()
    idx = []
    title = []
    category = []
    name = []
    cost = []
    delivery = []
    reviews = []
    ratings = []
    i = 0
    for r in range(0 , row):
        idx.append(i)
        title.append(str(self.tableWidget.item(r , 0).text()))
        category.append(str(self.tableWidget.item(r , 1).text()))
        name.append(str(self.tableWidget.item(r , 2).text()))
        cost.append(int((self.tableWidget.item(r , 3).text())))
        delivery.append(int((self.tableWidget.item(r , 4).text())))
        reviews.append(int((self.tableWidget.item(r , 5).text())))
        ratings.append(float((self.tableWidget.item(r , 6).text())))
        i+=1
    return [idx ,title , category , name , cost , delivery ,reviews ,ratings]               # Return table values in the form of array

def sort(self , sortTypeidx , sortColumnidx , sortDirection):
    if (sortTypeidx == 0):
        pass
    else:
        # try:
        allTableData = getColumnFromTable(self)
        indexes = allTableData[0]
        arrayToSort = allTableData[sortColumnidx]
        if (sortTypeidx == 1):
            indexes = Codes.allSortingAlgorithms.insertionSort(arrayToSort , indexes)
        elif (sortTypeidx == 2):
            arrayToSort , indexes = Codes.allSortingAlgorithms.selectionSort(arrayToSort , indexes)
        elif (sortTypeidx == 3):
            A = arrayToSort.copy()
            start = time.time()
            indexes = Codes.allSortingAlgorithms.mergeSort(A , 0 , len(A)-1, indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
        elif (sortTypeidx == 4):
            A = arrayToSort.copy()
            start = time.time()
            indexes = Codes.allSortingAlgorithms.bubbleSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
        
        elif (sortTypeidx == 5):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.quickSort(A ,0,len(A)-1, indexes)
            
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
        elif (sortTypeidx == 6):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.radixSort(A , indexes)
            if indexes != 0:
                end = time.time()
                Codes.allSortingAlgorithms.diff = (end - start)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Radix Sort is not working on float data type")
                x = msg.exec_()
                return
        elif (sortTypeidx == 7):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.countingSort(A , indexes)
            if indexes != 0:
                end = time.time()
                Codes.allSortingAlgorithms.diff = (end - start)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Counting Sort is not working on float data type")
                x = msg.exec_()
                return
        elif (sortTypeidx == 8):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()

            indexes = Codes.allSortingAlgorithms.bucketSort(A , indexes)
            if indexes != 0:
                end = time.time()
                Codes.allSortingAlgorithms.diff = (end - start)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Bucket Sort is not working on string data type")
                x = msg.exec_()
                return
        elif (sortTypeidx == 9):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.heapSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
        elif (sortTypeidx == 10):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.gnomeSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
            
        elif (sortTypeidx == 11):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.combSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
            
        elif (sortTypeidx == 12):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.pigeonholeSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
           
        elif (sortTypeidx == 13):
            A = arrayToSort.copy()
            print(sys.getrecursionlimit())
            start = time.time()
            indexes = Codes.allSortingAlgorithms.shellSort(A , indexes)
            end = time.time()
            Codes.allSortingAlgorithms.diff = (end - start)
            
        
        updatedArrys = updateAllArrays(allTableData , indexes)
        self.tableWidget
        rowPosition = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(rowPosition)
        self.tableWidget_2.setItem(rowPosition , 2 , QtWidgets.QTableWidgetItem(str(round(Codes.allSortingAlgorithms.diff , 10))))
        Codes.allSortingAlgorithms.diff = 0        

        t = Thread(target = insertDataInTable(self , updatedArrys))
        t.start()
    # # except:
    #         msg = QMessageBox()
    #         msg.setWindowTitle("Error")
    #         msg.setText("Sorting Process Could Not Complete")
    #         x = msg.exec_()
# def insertDataInTable(self , array):
#     emptyTable(self)
def insertDataInTable(self , array):
    rows = self.tableWidget.rowCount()
    # print(rows)
    # print(self.tableWidget.item(5,0).text())
    for i in range(0 , rows):
        # print(i)
        # print(array[i][0])
        # print(array[i][1])
        # print(array[i][2])
        # print(array[i][3])
        # print(array[i][4])
        # print(array[i][5])
        # print(array[i][6])
        self.tableWidget.setItem(i , 0 , QtWidgets.QTableWidgetItem(array[i][0]))
        self.tableWidget.setItem(i , 1 , QtWidgets.QTableWidgetItem(str(array[i][1])))
        self.tableWidget.setItem(i , 2 , QtWidgets.QTableWidgetItem(str(array[i][2])))
        self.tableWidget.setItem(i , 3 , QtWidgets.QTableWidgetItem(str(array[i][3])))
        self.tableWidget.setItem(i , 4 , QtWidgets.QTableWidgetItem(str(array[i][4])))
        self.tableWidget.setItem(i , 5 , QtWidgets.QTableWidgetItem(str(array[i][5])))
        self.tableWidget.setItem(i , 6 , QtWidgets.QTableWidgetItem(str(array[i][6])))