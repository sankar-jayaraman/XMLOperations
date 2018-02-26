import unittest
from multiplicationChecker import MultiplicationChecker
import xml.etree.ElementTree  as ET


class Test_MultiplicationChecker(unittest.TestCase):
    def test_WhenNoFactorTagsFound_RaisesError(self):
        input = """<expressions> 
                    <multiplication id="1"> 
                        <factor1>2</factor1>
                        <factor1>3</factor1>
                        <factor1>4</factor1> 
                    </multiplication>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = MultiplicationChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root[0]) 

    