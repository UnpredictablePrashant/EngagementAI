# Import dependencies
from src.engine import reko
import glob
import os

# Get all the files in directory
rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "./")).replace("\\", "/")
directory = rootpath+ "/db/input/videos/OutputDump/*.jpg"
outputpath = rootpath+'/out/'

files = glob.glob(directory)

# Get emotions of all the files present in the folder
for i,file in enumerate(files):

    head, tail = os.path.split(file)

    savePath = outputpath + tail.split(".jpg")[0] + '/'

    reko(file,savePath)

    print(f"[info...] {tail} processed")