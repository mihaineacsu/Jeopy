import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from categories import categoryGrid
from grid import questionGrid

class mainWindow(QWidget):
	def __init__(self, title, width, height, pred, parent = None):
		super(mainWindow, self).__init__(None)
		
		self.pred = pred
		
		self.setMinimumSize(width, height)
		self.setWindowTitle(title)
		
		ButtonSize = QSize(40, 40)

		self.remColumn = QToolButton()
		self.remColumn.setIcon(QIcon("remcol.png"))
		self.remColumn.setIconSize(ButtonSize)
		
		self.addColumn = QToolButton()
		self.addColumn.setIcon(QIcon("addcol.png"))
		self.addColumn.setIconSize(ButtonSize)	
		
		self.remRow = QToolButton()
		self.remRow.setIcon(QIcon("remrow.png"))
		self.remRow.setIconSize(ButtonSize)
		
		self.addRow = QToolButton()
		self.addRow.setIcon(QIcon("addrow.png"))
		self.addRow.setIconSize(ButtonSize)	
	
		self.rows = 2
		self.cols = 2
		
		self.categories = categoryGrid(self.cols, pred = self)	
		self.questions = questionGrid(self.rows, self.cols, self, parent = self.parent())
		
		self.saveButton = QPushButton("Save")
       		self.cancelButton = QPushButton("Cancel")

		layout = QGridLayout()
		
		layout.addWidget(self.remColumn, 2 ,0)
		layout.addWidget(self.addColumn, 2, 1, Qt.AlignLeft)
		layout.addWidget(self.categories, 0, 1)
		layout.addWidget(self.questions, 1, 1)
		layout.addWidget(self.remRow, 0, 2)
		layout.addWidget(self.addRow, 1, 2, Qt.AlignTop)
		layout.addWidget(self.saveButton, 2, 1, Qt.AlignRight)
		layout.addWidget(self.cancelButton, 2, 2)
 
		self.setLayout(layout)
		
		self.connect(self.remColumn, SIGNAL("clicked()"), lambda action="remColumn": self.updateUI(action))
		self.connect(self.addColumn, SIGNAL("clicked()"), lambda action = "addColumn": self.updateUI(action))
		self.connect(self.addRow, SIGNAL("clicked()"), lambda action = "addRow": self.updateUI(action))
		self.connect(self.remRow, SIGNAL("clicked()"), lambda action = "remRow": self.updateUI(action))
		

	def updateUI(self, action):
		if action == "remColumn":
			if self.cols > 0:
				self.cols = self.cols - 1
				self.categories.rem(self.cols)
				self.questions.remColumn(self.rows, self.cols)
		
		if action == "addColumn":
			self.cols = self.cols + 1
			self.categories.add(self.cols)
			self.questions.addColumn(self.rows, self.cols)

		if action == "remRow":
			if self.rows > 0:
				self.rows = self.rows -1
				self.questions.remRow(self.rows, self.cols)

		if action == "addRow":
			self.rows = self.rows + 1
			self.questions.addRow(self.rows, self.cols)

	def saveRound(self):
		pass
#		for c ... :
#		self.d[c]["title"] = ...
#		self.pred["rounds"][self.r]["categories"] = self.d
            

	def closeEvent(self, event):
		self.pred.isOpen = False
    
def main():
	app = QApplication(sys.argv)
	form =  mainWindow()
	form.show()
	app.exec_()	

if __name__ == '__main__':
	main()
