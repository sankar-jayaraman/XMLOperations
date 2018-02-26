import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'Interfaces'))

import argparse
import xml.etree.ElementTree as ET
from operationTypeSelector import OperationTypeSelector
from operationCheckSelector import OperationCheckSelector
from integerResultWriter import IntegerResultWriter
import xml.dom.minidom as miniD
import collections

# Setting up command line parser
parser = argparse.ArgumentParser(description = 'Perform Arithmetic operations from input XML operations files')
parser.add_argument('inputPath', type = str, help = 'Path where the input XML operations files are stored ')
parser.add_argument('outputPath', type = str, help = 'Path where the output XML operations files should be stored ')
args = parser.parse_args()

# Getting path to input folder and output folder
currentDir = os.getcwd()
inputDir = os.path.abspath(args.inputPath)
outputDir = os.path.abspath(args.outputPath)
os.chdir(inputDir)

# Walking through XML files in input folder and writing results to output folder
for file in os.listdir(inputDir):
    
    if file.endswith('.xml'):
        tree = ET.parse(file)
        root = tree.getroot()
        results = collections.OrderedDict()
        for child in root:
            # Selects between simple and complex operations
            selector = OperationTypeSelector()
            evaluator = selector.Select(child)

            # Selects the type of operation to be checked for valid XML

            operationXMLcheckerSelector = OperationCheckSelector()
            operationXMLChecker = operationXMLcheckerSelector.Select(child)
            try:
                if(operationXMLChecker.IsValidOperationXML(child)):
                   results[child.attrib['id']] = evaluator.Evaluate(child)
            except Exception as err:
                   results[child.attrib['id']] = 'ERROR: ' + err.args[0]
                   break; 
        # Writing results to result file
        writer = IntegerResultWriter()
        resultXMLString = ET.tostring(writer.Write(results))
        resultXML = miniD.parseString(resultXMLString)
        prettyResult = resultXML.toprettyxml()
        inputFileNameWithoutExt = os.path.splitext(file)[0]
        outputFileName = os.path.join(outputDir, inputFileNameWithoutExt + '_result.xml') 
        output = open(outputFileName,'wt')
        output.write(prettyResult)
    
print ('All input XML files processed successfully !! ')






