# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:49:19 2018
This script will read and print all colum fields and schema info from a shapefile
@author: ow4253
"""
import psycopg2
import osgeo.ogr

connection = psycopg2.connect(database="ca_blocks",user="postgres", password="$%^@#")
cursor = connection.cursor()


#cursor.execute("DROP TABLE IF EXISTS blocks")
#cursor.execute("CREATE TABLE blocks (id SERIAL PRIMARY KEY, fips VARCHAR NOT NULL, pop BIGINT NOT NULL, outline GEOGRAPHY)")
shapefile = osgeo.ogr.Open("cenblkSF.shp")
layer = shapefile.GetLayer(0)


#Get Field Names
layerDefinition = layer.GetLayerDefn()
print ("Name  -  Type  Width  Precision")
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()

    print (fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision))
