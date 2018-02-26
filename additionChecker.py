import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))

from xmlFormChecker import XMLFormChecker

class AdditionChecker(XMLFormChecker):
    def IsValidOperationXML(self,child):
        
        if len(child.findall('item')) > 0 :
            return True
        else:
            raise SyntaxError('XML must contain at least one item tag and value')





