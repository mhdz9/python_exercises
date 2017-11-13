class Calculator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = 15

    def addition(self):
        print "The result is: ", self.value1 + self.value2

    def subtraction(self):
        print "The result is: ", self.value2 - self.value1

    def multiplication(self):
        print "The result is: ", self.value1 * self.value2

    def division(self):
        print "The result is: ", self.value2 / self.value1

    def prompt(self):
        while True:
            try:
                choice = int(raw_input("Please enter the number of the operation you want to execute\n"
                                       "1. Addition (+)\n"
                                       "2. Subtraction (-)\n"
                                       "3. Multiplication (*)\n"
                                       "4. Division (/)\n"
                                       "5. Exit\n"))
            except:
                print "Please enter a valid option"
            #print "Lo que sea"
            if choice in [1,2,3,4]:
                #print "X"
                if choice == 1:
                    self.addition()
                elif choice == 2:
                    self.subtraction()
                elif choice == 3:
                    self.multiplication()
                elif choice == 4:
                    self.division()
            else:
                break

calc = Calculator(5,20)
calc.prompt()
#calc.addition()
#calc.division()