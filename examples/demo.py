''' Example: Reduce number of samples'''
import smrd

filenameIn = 'test.h5'
filenameOut = 'out.h5'


try:
    remove(filenameOut) 
except:
    print('File did not exist. No need to delete it.')
    

fileIn = smrd.File(filenameIn)
datasetIn = fileIn['dataset']

number_of_samples = 0
acquisitions = []


for aqIn in datasetIn.acquisitions:
        
       
    aqOut = smrd.Acquisition.from_array(aqIn.data[0:16, 0:140])

    aqOut.idx = aqIn.idx       
    aqOut.position = aqIn.position    
    aqOut.read_dir = aqIn.read_dir   
    aqOut.phase_dir = aqIn.phase_dir   
    aqOut.slice_dir = aqIn.slice_dir   
    aqOut.flags = aqIn.flags
    
    acquisitions.append(aqOut)
    
header = datasetIn.header

# Create output file
with smrd.File(filenameOut) as file:
        dsetOut = file['dataset']
        dsetOut.header = header
        dsetOut.acquisitions = acquisitions
