from PyQt5 import QtCore, QtGui, QtWidgets
import sorting
def insertNewSortColumn(self , warea ,area ,Main_Window):
    self.sortColumn1 = QtWidgets.QComboBox(warea)
    font = QtGui.QFont()
    font.setFamily("Times New Roman")
    row = self.formLayout.rowCount()
    self.sortColumn1.setFont(font)
    self.sortColumn1.setEditable(True)
    self.sortColumn1.setObjectName("sortColumn1")
    self.sortColumn1.addItem("Select Column"+str(row+1))
    self.sortColumn1.addItem("Title")
    self.sortColumn1.addItem("Category")
    self.sortColumn1.addItem("Name")
    self.sortColumn1.addItem("Cost")
    self.sortColumn1.addItem("Delivery")
    self.sortColumn1.addItem("Reviews")
    self.sortColumn1.addItem("Ratings")
    
    self.sortingDirection = QtWidgets.QComboBox(warea)
    self.sortingDirection.setObjectName("sortingDirection")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\../../../.designer/backup/Icons/filter (23).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.sortingDirection.addItem(icon, "")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\../../../.designer/backup/Icons/sort (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.sortingDirection.addItem(icon1, "")
    row = self.formLayout.rowCount()
    print(row)
    self.formLayout.setWidget(row,QtWidgets.QFormLayout.LabelRole, self.sortColumn1 )
    self.formLayout.setWidget(row,QtWidgets.QFormLayout.FieldRole, self.sortingDirection )
    print(row)
    area.setWidget(warea)
    _translate = QtCore.QCoreApplication.translate
    Main_Window.setWindowTitle(_translate("Main_Window", "Virtual World Projects"))
    self.sortingDirection.setItemText(0, _translate("Main_Window", "Ascending"))
    self.sortingDirection.setItemText(1, _translate("Main_Window", "Descending"))

def insertNewSearchinColumn(self):
    #Combo Box
    self.selectSearchColumn = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
    self.selectSearchColumn.setEnabled(True)
    self.selectSearchColumn.setObjectName("selectSearchColumn")
    self.selectSearchColumn.addItem("Select Col")
    self.selectSearchColumn.addItem("Title")
    self.selectSearchColumn.addItem("Category")
    self.selectSearchColumn.addItem("Name")
    self.selectSearchColumn.addItem("Cost")
    self.selectSearchColumn.addItem("Delivery")
    self.selectSearchColumn.addItem("Reviews")
    self.selectSearchColumn.addItem("Ratings")
    
    self.horizontalLayout.addWidget(self.selectSearchColumn)
    #Line Edit
    self.searchArea1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
    self.searchArea1.setObjectName("searchArea1")
    self.horizontalLayout.addWidget(self.searchArea1)

def deleteNewSortColumn(area):
    row = area.rowCount()
    if (row > 1):
        area.removeRow(row-1)
def cancelSort(area):
    row = area.rowCount()
    print(row)
    for i in range(row-1 , 0 , -1):
        area.removeRow(i)
def sortStart(self):
    row = self.formLayout.rowCount()
    colIdx = self.sortColumn1.currentIndex()
    sortTypeIdx = self.sortType.currentIndex()
    sortDirection = self.sortingDirection.currentIndex()
    sortType = self.sortType.currentText()
    jobNumber = self.tableWidget.rowCount()

    # for i in range (0 , row):
    #         cat = self.formLayout.itemAt(i , 1).widget().currentText()
    #         direc = self.formLayout.itemAt(i , 0).widget().currentText()
    #         typesort = self.sortType.currentText()
    #         print(cat+" "+direc + " " + typesort)
    sorting.sort(self ,sortTypeIdx ,colIdx , sortDirection)
    rowPosition = self.tableWidget_2.rowCount()
    self.tableWidget_2.setItem(rowPosition-1 , 0 , QtWidgets.QTableWidgetItem(sortType))
    self.tableWidget_2.setItem(rowPosition-1 , 1 , QtWidgets.QTableWidgetItem(str(jobNumber)))
    