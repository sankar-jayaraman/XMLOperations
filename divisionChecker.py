import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))

from xmlFormChecker import XMLFormChecker


class DivisionChecker(XMLFormChecker):
    def IsValidOperationXML(self,child):
        
        if len(child) == 2 and child[0].tag == 'dividend' and child[1].tag == 'divisor':
            return True
        else:
            raise SyntaxError('XML must contain exactly one dividend and divisor')

