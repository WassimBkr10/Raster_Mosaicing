# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:48:53 2022

@author: wassim
"""
import os
import sys
from qgis.core import *
from qgis.gui import *
import os.path



route = r"C:\WBK\_______PYTHON______\QGIS_DIR_Test\pour_wasim"

dirs = [d for d in os.listdir(route) if os.path.isdir(os.path.join(route, d))]

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    # print(allFiles)
    return allFiles


root = QgsProject.instance().layerTreeRoot()
# for group in dirs:
#     shapeGroup = root.addGroup(group)

filenames = []

for names in dirs:
    shapeGroup = root.addGroup(names)
    test = getListOfFiles('{}\{}'.format(route, names))
    for file in test:
        if ".shp" in file:
            if "xml" not in file:
                fileroute = file
                filename = QgsVectorLayer(fileroute, file[:-4], "ogr")
                QgsProject.instance().addMapLayer(filename, False)
                shapeGroup.insertChildNode(1, QgsLayerTreeLayer(filename))
                filename.setName(os.path.basename(file))
                
                # filename.renderer().symbol().setSize(6)
                # filename.triggerRepaint()
                # filename.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
                
                # for field in filename.fields():
                #     print(field.name(), field.type())


