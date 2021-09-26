"""Written by  : Oyabunmi oluwadamilare
Description : Uses Pythons eval() function
              as a way to implement calculator.

Functions available are:
--------------------------------------------
                         + : addition
                         - : subtraction
                         * : multiplication
                         / : division
                         % : percentage
                         e : 2.718281...
                        pi : 3.141592...
                      sine : sin(rad)
                    cosine : cos(rad)
                   exponent: x^y
                   tangent : tan(rad)
                 remainder : XmodY
               square root : sqrt(n)
  round to nearest integer : round(n)
convert degrees to radians : rad(deg)
absolute value             : aval(n)
"""

import math


class Calculator:

    def __init__(self, term):
        self.__term = term

    # Converting inputed strings and evaluate them
    def calc(self):
        self.__term = self.__term.replace(' ', '')
        self.__term = self.__term.replace('^', '**')
        self.__term = self.__term.replace('=', '')
        self.__term = self.__term.replace('?', '')
        self.__term = self.__term.replace('%', '/100.00')
        self.__term = self.__term.replace('rad', 'radians')
        self.__term = self.__term.replace('mod', '%')
        self.__term = self.__term.replace('aval', 'abs')

        functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e']

        self.__term = self.__term.lower()

        for func in functions:
            if func in self.__term:
                withmath = 'math.' + func
                self.__term = self.__term.replace(func, withmath)

        try:

            # here goes the actual evaluating.
            self.__term = eval(self.__term)

        # here goes to the error cases.
        except ZeroDivisionError:

            print("Can't divide by 0.  Please try again.")

        except NameError:

            print('Invalid input.  Please try again')

        except AttributeError:

            print('Please check usage method and try again.')
        except TypeError:
            print("please enter inputs of correct datatype ")

        return self.__term

    # To get the result of your questions
    def result(self):
        print(f"\nYour answer is:  {str(Calculator.calc(self))}")
