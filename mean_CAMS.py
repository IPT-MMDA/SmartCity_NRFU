import osgeo.gdal as gdal
import glob
import numpy 

inPath = "H:/Smart_City_Proj_NFDU/CAMS_work/test_mean/"
outPath = "H:/Smart_City_Proj_NFDU/CAMS_work/test_mean/rez.tif"


def openfile(inPath):
    fl = glob.glob(inPath  + '*.tif')
    files = []
    for f in fl:
        files.append(gdal.Open(f))
    return files



files = openfile(inPath)
gdalData = files [0]

if gdalData is None:
  print ("ERROR: can't open raster")
  sys.exit( 1 )
  
print ("Number of bands", gdalData.RasterCount)

def bandAsArray( Data, bandNum ):
  gdalData = Data
  gdalBand = gdalData.GetRasterBand( bandNum )
  array = gdalBand.ReadAsArray().astype( numpy.float32 )
  gdalBand = None
  gdalData = None
  return array
  
  
  
bands = []
  
def bandsmean(bands):
   result = sum(bands)/len(bands)
   return result
   
   
   
def saveRaster( outPath,Data, array ):
  gdalData = Data
  projection = gdalData.GetProjection()
  transform = gdalData.GetGeoTransform()
  xsize = gdalData.RasterXSize
  ysize = gdalData.RasterYSize
  gdalData = None
 
  format = "GTiff"
  driver = gdal.GetDriverByName( format )
  metadata = driver.GetMetadata()
  outRaster = driver.Create( outPath, xsize, ysize, 1, gdal.GDT_Float32 )
  outRaster.SetProjection( projection )
  outRaster.SetGeoTransform( transform )
  outRaster.GetRasterBand( 1 ).WriteArray( array )
  outRaster = None
  
result = []   
for f in files:
   bands = []
   for i in range(1, gdalData.RasterCount+1):
      bands.append(bandAsArray(f , i))
   result.append(bandsmean(bands))     

def rastrmean(rasters):
   result = sum(rasters)/len(rasters)
   return result
   
means = rastrmean(result)
 

saveRaster( outPath, gdalData, means )
      
    
    

