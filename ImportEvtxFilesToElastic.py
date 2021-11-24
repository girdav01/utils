#Import some Windows Event logs (in evtx files) to Elastic 7.2+
from evtxtoelk import EvtxToElk
import os
elastic = 'http://192.168.44.150:9200'
path_of_the_directory = 'C:\logs\evtx'
ext = ('.evtx') # filter the .evtx file only
for files in os.scandir(path_of_the_directory):
    if files.path.endswith(ext):
        print(files.path)
        EvtxToElk.evtx_to_elk(files.path,elastic)
