from additionChecker import AdditionChecker
from subtractionChecker import SubtractionChecker
from divisionChecker import DivisionChecker
from multiplicationChecker import MultiplicationChecker

class OperationCheckSelector(object):
    """description of class"""
    def Select(self, child):
        if child.tag == 'addition':
             return AdditionChecker()
        elif child.tag == 'subtraction': 
             return SubtractionChecker()
        elif child.tag == 'division': 
             return DivisionChecker()
        elif child.tag == 'multiplication':
             return MultiplicationChecker()  
        else:
             raise SyntaxError('SubElement of expressions must be one of addition, subtraction, division or multiplication')   


