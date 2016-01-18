## twoPoints.py
# Generates two points and saves it as a shape file
# by: Gert Sterenborg

import os
working_dir = os.getcwd()
os.remove('data/twoPoints.shp')
os.remove('data/twoPoints.prj')
os.remove('data/twoPoints.shx')
os.remove('data/twoPoints.dbf')

## Loading osgeo
try:
  from osgeo import ogr, osr
  print 'Import of ogr and osr from osgeo worked.  Hurray!\n'
except:
  print 'Import of ogr and osr from osgeo failed\n\n'

## Is the ESRI Shapefile driver available?
driverName = "ESRI Shapefile"
drv = ogr.GetDriverByName( driverName )
if drv is None:
    print "%s driver not available.\n" % driverName
else:
    print  "%s driver IS available.\n" % driverName

## choose your own name
## make sure this layer does not exist in your 'data' folder
fn = "data/twoPoints.shp"
layername = "deuxPoint"

## Create shape file
ds = drv.CreateDataSource(fn)
##print ds.GetRefCount()

# Set spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

# Create Layer
layer=ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
layerDefinition = layer.GetLayerDefn()

# Make a coordinate list
coordinates = [[51.987754,5.665803,  "PC_room"],[51.965966,5.650683, "Home_room"]]

# For loop to go through the points within the coordinate list
for coordinate in coordinates:
    point = ogr.Geometry(ogr.wkbPoint)
    point.SetPoint(0, coordinate[1], coordinate[0]) 
    feature = ogr.Feature(layerDefinition)
    feature.SetGeometry(point)
    layer.CreateFeature(feature)

print "The extent:"
print layer.GetExtent()

# Saving the object by destroying it
ds.Destroy()
