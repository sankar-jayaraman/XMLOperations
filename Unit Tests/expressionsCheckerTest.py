import unittest
from expressionsChecker import ExpressionsChecker
import xml.etree.ElementTree  as ET


class Test_ExpressionsCheckerTest(unittest.TestCase):
    def test_WhenNoExpressionTagFoundRaisesError(self):
        input = """<exp> 
                    <addition id="1"> 
                        <item>2</item>
                        <item>3</item>
                        <item>4</item> 
                    </addition>
               </exp>"""

        root = ET.fromstring(input)
        checker = ExpressionsChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root) 
    
    


