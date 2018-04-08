from __future__ import print_function
#                            #
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
# %matplotlib inline

#import training data
T1 = io.imread('characters/T1.GIF')
T2 = io.imread('characters/T2.GIF')
T3 = io.imread('characters/T3.GIF')
T4 = io.imread('characters/T4.GIF')
T5 = io.imread('characters/T5.GIF')
T6 = io.imread('characters/T6.GIF')
T7 = io.imread('characters/T7.GIF')
T8 = io.imread('characters/T8.GIF')
T9 = io.imread('characters/T9.GIF')
T10 = io.imread('characters/T10.GIF')
Ts = [T1,T2,T3,T4,T5,T6,T7,T8,T9,T10]

S1 = io.imread('characters/S1.GIF')
S2 = io.imread('characters/S2.GIF')
S3 = io.imread('characters/S3.GIF')
S4 = io.imread('characters/S4.GIF')
S5 = io.imread('characters/S5.GIF')
S6 = io.imread('characters/S6.GIF')
S7 = io.imread('characters/S7.GIF')
S8 = io.imread('characters/S8.GIF')
S9 = io.imread('characters/S9.GIF')
S10 = io.imread('characters/S10.GIF')
Ss = [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10]

V1 = io.imread('characters/V1.GIF')
V2 = io.imread('characters/V2.GIF')
V3 = io.imread('characters/V3.GIF')
V4 = io.imread('characters/V4.GIF')
V5 = io.imread('characters/V5.GIF')
V6 = io.imread('characters/V6.GIF')
V7 = io.imread('characters/V7.GIF')
V8 = io.imread('characters/V8.GIF')
V9 = io.imread('characters/V9.GIF')
V10 = io.imread('characters/V10.GIF')
Vs = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10]

#do fourier transforms and put values in arrays
MagsT = []
MagsS = []
MagsV = [] #empty arrays for magnitude spectra

#put magnitude values of fourier transform in three arrays
for i in range(10):
    f_f = np.array(Ts[i], dtype=float)
    z = np.fft.fft2(f_f)           # do fourier transform
    q = np.fft.fftshift(z)         # puts u=0,v=0 in the centre
    Magq =  np.absolute(q)
    MagsT.append(Magq)

for i in range(10):
    f_f = np.array(Ss[i], dtype=float)
    z = np.fft.fft2(f_f)           # do fourier transform
    q = np.fft.fftshift(z)         # puts u=0,v=0 in the centre
    Magq =  np.absolute(q)
    MagsS.append(Magq)

for i in range(10):
    f_f = np.array(Vs[i], dtype=float)
    z = np.fft.fft2(f_f)           # do fourier transform
    q = np.fft.fftshift(z)         # puts u=0,v=0 in the centre
    Magq =  np.absolute(q)
    MagsV.append(Magq)
#^that could be a for in a for

#train
#sum central row of data
midT = []
midS = []
midV = []

for i in range(10):
    midT.append((sum(MagsT[i][200,:])/640))
    midS.append((sum(MagsS[i][200,:])/640))
    midV.append((sum(MagsV[i][200,:])/640))

Tavg = np.mean(midT)
Savg = np.mean(midS)
Vavg = np.mean(midV)

print(Tavg,Savg,Vavg)
