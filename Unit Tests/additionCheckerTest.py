import unittest
from additionChecker import AdditionChecker
import xml.etree.ElementTree  as ET


class Test_AdditionCheckerTest(unittest.TestCase):
    def test_WhenNoItemTagsFound_RaisesError(self):
        input = """<expressions> 
                    <addition id="1"> 
                        <item1>2</item1>
                        <item1>3</item1>
                        <item1>4</item1> 
                    </addition>
               </expressions>
               """

        root = ET.fromstring(input)
        checker = AdditionChecker()
        with self.assertRaises(SyntaxError):
            checker.IsValidOperationXML(root[0]) 

    