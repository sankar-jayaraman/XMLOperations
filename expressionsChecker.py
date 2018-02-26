import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))

from xmlFormChecker import XMLFormChecker

class ExpressionsChecker(XMLFormChecker):
    def IsValidOperationXML(self,root):
        if root.tag != 'expressions':
            raise SyntaxError('XML must contain opening and closing expressions tag')
        return True



