"""
Program: salaryGUI_TT.py
Author: Teri  07.19.23

GUI-based application to help you calculate your salary.

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (application name will change project to project)
class SalaryCal(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame constructor method
		EasyFrame.__init__(self, title = "E-Z Salary Calculator", width = 380, height = 280, resizable = False, background = "mediumseagreen")
		self.normalFont = Font(family = "Verdana", size = 10)

		# Adding components to the window
		self.addLabel(text = "E-Z Salary", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "mediumseagreen", foreground = "floralwhite", font = Font(family = "Georgia", size = 28))
		self.addLabel(text = "*Welcome*\n Thank you for using our service!\nBelow enter your hourly wage and amount\nof hours worked to calculate your salary.", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "mediumseagreen", foreground = "black", font = self.normalFont)
		self.addLabel(text = "Hourly Wage: ", row = 2, column = 0, sticky = "NE", background = "mediumseagreen", foreground = "floralwhite", font = self.normalFont)
		self.wage = self.addFloatField(value = 0.0, row = 2, column = 1, sticky = "NW", width = 6)
		self.addLabel(text = "Hours Worked: ", row = 3, column = 0, sticky = "NE", background = "mediumseagreen", foreground = "floralwhite", font = self.normalFont)
		self.hoursWorked = self.addFloatField(value = 0.0, row = 3, column = 1, sticky = "NW", width = 6)

		self.button = self.addButton(text = "Calculate Now", row =  4, column = 0, columnspan = 2, command = self.calculate)

		self.addLabel(text = "Your current salary: ", row = 5, column = 0, sticky = "NE", background = "mediumseagreen", foreground = "floralwhite", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 8)

	# Definition of the calculate() function
	def calculate(self):
		# Grab the user input from the GUI window
		wage = self.wage.getNumber()
		hours = self.hoursWorked.getNumber()

		# Processing phase
		result = wage * hours

		# Output phase
		self.total.setNumber(result)

# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	SalaryCal().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()