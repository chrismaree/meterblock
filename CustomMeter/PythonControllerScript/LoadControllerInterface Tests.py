import loadControllerInterface as lci
from time import sleep

#turn load on
lci.powerOn()

#take 20 samples, every 0.5 seconds
for x in range(0,19):
    print(lci.queryPower())
    print('isConsuming: ' + str(lci.isConsuming())+'\n')
    sleep(0.5)
lci.powerOff()