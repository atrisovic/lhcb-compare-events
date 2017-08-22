import sys

import GaudiPython as GP
from GaudiConf import IOHelper
from Configurables import DaVinci

dv = DaVinci()
dv.DataType = '2011'
dv.Simulation = True

# Pass file to open as first command line argument
inputFiles = [sys.argv[-1]]
IOHelper('ROOT').inputFiles(inputFiles)

appMgr = GP.AppMgr()
evt = appMgr.evtsvc()

f = open('event_list.txt', 'w')
# start processing 
numberOfEvents = 1
for _ in range(numberOfEvents):
    appMgr.run(1)

    evtheader = evt['/Event/Gen/Header']
    tracks = evt['/Event/Rec/Track/Best']
    #MCParticles = evt['/Event/Sim/MCParticles']

    f.write("Run number Event number " + ' '.join([str(evtheader.runNumber()), str(evtheader.evtNumber())]))
    for t in tracks:
        f.write(' '.join([str(t.p()), str(t.pt()), str(t.lhcbIDs().size())]))
        f.write('\n'.join([str(i.lhcbID()) for i in t.lhcbIDs()]))
# end for loop
f.close()

