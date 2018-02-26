import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))
from resultWriter import ResultWriter
import xml.etree.ElementTree  as ET



class IntegerResultWriter(ResultWriter):
    def Write(self, resultDict):
        builder = ET.TreeBuilder()
        builder.start('expressions', {})
        index = 0
        for id in resultDict:
            builder.start('result', {'id' : id})
            builder.data(str(resultDict[id]))
            builder.end('result')
            
        builder.end('expressions')    
        return builder.close()