import sys

import GaudiPython as GP
from GaudiConf import IOHelper
from Configurables import DaVinci

dv = DaVinci()
dv.DataType = '2011'

# Pass file to open as first command line argument
inputFiles = [sys.argv[-1]]
IOHelper('ROOT').inputFiles(inputFiles)

appMgr = GP.AppMgr()
evt = appMgr.evtsvc()

# start processing 
numberOfEvents = 1
for _ in range(numberOfEvents):
    appMgr.run(1)

    evtheader = evt['/Event/Gen/Header']
    tracks = evt['/Event/Rec/Track/Best']
    #MCParticles = evt['/Event/Sim/MCParticles']

    print(evtheader.runNumber(), evtheader.evtNumber())
    for t in tracks:
        print (t.p(), t.pt(), t.lhcbIDs().size())
        for i in t.lhcbIDs():
            print(i.lhcbID())
# end for loop
