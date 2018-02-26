import unittest
from integerResultWriter import IntegerResultWriter
import xml.etree.ElementTree  as ET
import collections

class Test_IntegerResultWriterTest(unittest.TestCase):
    
    def make_pretty_xml(self,input):
        return miniD.parseString(input).toprettyxml()

    def test_WritesOutResultsCorrectly(self):
        resultdict = collections.OrderedDict ()
        resultdict['1'] = 9
        resultdict['2'] = 1
        resultdict['3'] = 240
        resultdict['4'] = 6
            
        expectedXML = """<expressions><result id="1">9</result><result id="2">1</result><result id="3">240</result><result id="4">6</result></expressions>"""
        result = ET.tostring(IntegerResultWriter().Write(resultdict))
        self.assertEquals(expectedXML, result )

    

