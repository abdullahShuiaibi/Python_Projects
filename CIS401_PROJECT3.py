# June 3rd 2020
# program: CIS401_PROJECT3
# Programmer: Abdullah Shuiaibi
# program purpose: GUI mortgage calcator

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Application(QDialog):
	def __init__(self):
		super().__init__()
		#set up the font
		


		self.setStyleSheet("background-color:darkgreen;") 
		self.setWindowTitle("Mortgage Calculater")
		
		
		principalLabel = QLabel('Property Price:')
		principalLabel.setFont(QFont('Arial', 11))
		principalLabel.setStyleSheet("color:whitesmoke;")
		
		
		self.principalSpinBox = QDoubleSpinBox()
		self.principalSpinBox.setFont(QFont('Arial', 11))
		self.principalSpinBox.setRange(0, 100_000_000)
		self.principalSpinBox.setValue(250000)
		self.principalSpinBox.setStyleSheet("color:black;background:yellow;")
		self.principalSpinBox.setPrefix('$')
		

		downPaymentLabel = QLabel('Down Payment:')
		downPaymentLabel.setFont(QFont('Arial', 11))
		downPaymentLabel.setStyleSheet("color:whitesmoke;")

		self.downPaymentSpinBox = QDoubleSpinBox()
		self.downPaymentSpinBox.setFont(QFont('Arial', 11))
		self.downPaymentSpinBox.setRange(0, 100_000_000)
		self.downPaymentSpinBox.setValue(50000)
		self.downPaymentSpinBox.setStyleSheet("color:black;background:yellow;")

		
		
		self.downPaymentSpinBox.setPrefix('$')
		

		rateLabel = QLabel('Intrest Rate:')
		rateLabel.setFont(QFont('Arial', 11))
		rateLabel.setStyleSheet("color:whitesmoke;")

		self.rateSpinBox = QDoubleSpinBox()
		self.rateSpinBox.setFont(QFont('Arial', 11))
		self.rateSpinBox.setRange(0, 100) # 0% to 100%
		self.rateSpinBox.setValue(5) # 10% default value
		self.rateSpinBox.setStyleSheet("color:black;background:yellow;")
		self.rateSpinBox.setSuffix("%")
		

		yearLabel = QLabel('Years Amount:')
		yearLabel.setFont(QFont('Arial', 11))
		yearLabel.setStyleSheet("color:whitesmoke;")

		self.yearsComboBox = QComboBox()
		self.yearsComboBox.setFont(QFont('Arial', 11))
		self.yearsComboBox.addItem('1')
		self.yearsComboBox.setStyleSheet("color:black;background:yellow;")
		self.yearsComboBox.addItems(
			['{0} years'.format(year) for year in range(2, 32)]
		)
		

		amountLabel = QLabel('monthly mortage payment:')
		amountLabel.setStyleSheet("color:whitesmoke;")
		self.dollarLabel = QLabel()
		amountLabel.setFont(QFont('Arial', 11))
		self.dollarLabel.setFont(QFont('Arial', 10))


		self.button = QPushButton("calculate")
		self.button.setFont(QFont('Arial', 11))
		self.button.clicked.connect(self.calculate_interest)
		self.button.setStyleSheet("color:white;background:black")

		
		self.button1 = QPushButton("Clear")
		self.button1.setFont(QFont('Arial', 11))
		self.button1.clicked.connect(self.Clear_button)
		self.button1.setStyleSheet("color:white;background:black")


		self.button2 = QPushButton("Exist")
		self.button2.setFont(QFont('Arial', 11))
		self.button2.clicked.connect(self.Exit_button)
		self.button2.setStyleSheet("color:white;background:black")
		

                
		girdLayout = QGridLayout()
		girdLayout.addWidget(principalLabel, 0, 0)
		girdLayout.addWidget(self.principalSpinBox, 0, 1)
		girdLayout.addWidget(downPaymentLabel, 1, 0)
		girdLayout.addWidget(self.downPaymentSpinBox, 1, 1)
		girdLayout.addWidget(rateLabel, 2, 0)
		girdLayout.addWidget(self.rateSpinBox, 2, 1)
		girdLayout.addWidget(yearLabel, 3, 0)
		girdLayout.addWidget(self.yearsComboBox, 3, 1)
		girdLayout.addWidget(self.button, 4, 1)
		girdLayout.addWidget(amountLabel, 5, 0)
		girdLayout.addWidget(self.dollarLabel, 5, 1)
		girdLayout.addWidget(self.button2, 6, 0)
		girdLayout.addWidget(self.button1, 6, 1)
		

		vLayout = QVBoxLayout()
		vLayout.addLayout(girdLayout)
		self.setLayout(vLayout)
                


	def calculate_interest(self):
                
		price = self.principalSpinBox.value()
		down_payment = self.downPaymentSpinBox.value()
		p = price-down_payment
		intrest_rate = self.rateSpinBox.value()
		r = intrest_rate/100/12
		years = self.yearsComboBox.currentIndex() + 1
		y = years*12
		amt = (r/(1-(1+r)**(-y))) * p
		self.dollarLabel.setText('$ {0:.2f}'.format(amt))
		self.dollarLabel.setStyleSheet("background:yellow;border-color:solid black 3px;")
		self.dollarLabel.setFont(QFont('Arial', 11))
	def Exit_button(self):
                
		sys.exit(app.exec_())
		print("Good Bye")
		


		
	def Clear_button(self):
                
		self.dollarLabel.setText("")
		
		
		



	
		
if __name__ == '__main__':
	app = QApplication(sys.argv)

	app_1 = Application()
	app_1.show()

	sys.exit(app.exec_())



