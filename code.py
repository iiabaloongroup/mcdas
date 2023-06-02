""" File:           Spectrograph control software
    Author:         agsreejith
    Last change:    2014/10/11

 
"""
count = 0

if __name__ == '__main__':

    import OceanOptics
    import numpy as np
    #from time import sleep
    import time
    from time import strftime
    from datetime import datetime 
    
    

    class DynamicPlotter():
 
            

        def __init__(self, sampleinterval=2, size=(600,350), raw=False):
	    
            self._interval = int(sampleinterval*1000)
	    #self._count= i
	    
            # self.spec = OceanOptics.Maya200pro()
            self.spec = OceanOptics.MAYA2000PRO()
	    self.spec.integration_time(50000)
	    self.wl, self.sp = self.spec.acquire_spectrum()
	    
	   
            self.raw = bool(raw)
	    print "inside"
	    print count
            wavl=np.array(self.wl)
	    spect=np.array(self.sp)
	    np.savetxt('spect_out.txt', np.vstack([wavl,spect]))
	    
        def updateplot(self):
	    print "update"
	    global count
            count += 1
	    print "full inside"
	    print count 
            if self.raw:

                self.sp = np.array(self.spec._request_spectrum())[10:]

            else:

                self.wl, self.sp = self.spec.acquire_spectrum()
            wavl=np.array(self.wl)
	    spect=np.array(self.sp)
	    DAT= np.column_stack((wavl,spect))
	    tm=m.get_time()
	    filename='spectrum_%s.txt'%(tm,)
	    print filename
	    np.savetxt(filename, DAT, delimiter="   ")
            return True

        def run(self):
            print " "


	def get_time(self):
    	    time = datetime.now().strftime('%H:%M:%S')
            # In time string we store the time in format Hours:Minutes:Seconds
            return time
    
    import sys
    if sys.argv[1:] == ['--raw']:
        raw=True
    else:
        raw=False
    m = DynamicPlotter(sampleinterval=0.5, raw=raw)
    
    #print(time.strftime("%H:%M:%S")
    #time.sleep(7200)
    #print(time.strftime("%H:%M:%S")
    while True:
	#tme=m.get_time() 
        #print tme
	m.updateplot()
	time.sleep(1)

