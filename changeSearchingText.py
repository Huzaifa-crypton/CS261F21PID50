import loadCSV
from threading import*
import sorting
def changeText(self):
    composite = ""
    if (self.compositeFilters.currentText()!="Composite Filters"):
        composite = self.compositeFilters.currentText() +" "
        self.compositeFilters.setCurrentIndex(0)

    if (self.integerFilter.currentText()!="Ranges"):
        
        self.searchArea1.setText(composite+self.integerFilter.currentText() + " ")
        self.integerFilter.setCurrentIndex(0)
    elif (self.stringFilter.currentText()!="Filters"):
        self.searchArea1.setText(composite+self.stringFilter.currentText() +" ")
        print(self.stringFilter.currentIndex())
        self.stringFilter.setCurrentIndex(0)
    
