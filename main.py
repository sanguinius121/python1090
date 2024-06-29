from config1090 import config1090
from buffer import bufferClass
import numpy as np
import scipy.io
from scipy.signal import convolve
from packetSearch import packetSearch
from decode import decode
import time
import json



adsbParam = config1090()
#reading .mat file
matContents = scipy.io.loadmat('1090_caichien_5.mat')
iq_samples = matContents['iq_samples']


with open('data_caichien5.txt', 'w') as file:
    for dataSegment in range(4):
        epoch_time = float((time.time_ns())/1e9)
        z = np.ravel(iq_samples[dataSegment*adsbParam['SamplesPerFrame']:(dataSegment+1)*adsbParam['SamplesPerFrame']])
        zAbs = (np.abs(z))**2

        #fetching data into buffer
        bufferObj = bufferClass(adsbParam['SamplesPerFrame']*adsbParam['InterpolationFactor'],\
                                adsbParam['MaxPacketLength'])
        bufferObj.buffer(zAbs)
        xBuffDownSampled = bufferObj.xBuff[0::adsbParam['synchDownSampleFactor']]
        vectorxBuff = np.linspace(0,len(xBuffDownSampled),len(xBuffDownSampled))

        # # cross correlation the preamble and buffered signal
        crossCorr = convolve(np.array(xBuffDownSampled),np.array(adsbParam['synchFilter']),mode='full')

        pkt, packetCnt = packetSearch(crossCorr,bufferObj.xBuff,adsbParam,epoch_time)
        #print (pkt)
        for packet in pkt:
            decoded_message = decode(packet, dataSegment)
            if decoded_message is not None:
                json_message = json.dumps(decoded_message)
                file.writelines(json_message + '\n')

file.close()
# json_string = json.dumps(decoded)
# print(json_string)
'''
end here 
Status:
    - Have a list of decoded objects
    - Need to classify and process
'''

