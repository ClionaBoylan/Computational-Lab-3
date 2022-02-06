import numpy as np
import matplotlib.pyplot as plt
import time as tittymilk

starttime=tittymilk.time()
D=10**-(3.8)
m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
length=3000
g=9.8
B=1.6*(10**-4)
b=B*D
dt=0.001
vy=[0.7]
vyquad=[vy[0]]
vx=[0.7]
vxquad=[vx[0]]
sy=[0.0]
syquad=[sy[0]]
sx=[0.0]
sxquad=[sx[0]]

def dvy(v):
    return -g*dt-(b/m)*v*dt

def dvx(v):
    return -(b/m)*v*dt
i=0
while i<length-1:
    vy.append(vy[i]+dvy(vy[i]))
    vx.append(vx[i]+dvx(vx[i]))
    vyquad.append(vyquad[i]-g*dt)
    vxquad.append(vxquad[0])
    sy.append(sy[i]+vy[i]*dt)
    sx.append(sx[i]+vx[i]*dt)
    syquad.append(syquad[i]+vyquad[i]*dt)
    sxquad.append(sxquad[i]+vxquad[i]*dt)
    if syquad[i]<0:
        break
    i+=1

plt.scatter(sx,sy,c=sy, cmap='Greens',s=0.5)
plt.scatter(sxquad,syquad, c=syquad,cmap='Blues',s=0.5)
plt.scatter(0,0,label='Vacuum',c='blue',s=1e-9)
plt.scatter(0,0,label='Linear Air Resistance',c='green',s=1e-9)
plt.legend(markerscale=200000.0)
plt.ylim(0,1.1*max(syquad))
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$y$ (m)')
plt.savefig('Pointless.pdf')
plt.show()

# runno=101
# thetaarray=np.linspace(0,np.pi/2,runno)
# v=1
# R=[]
# j=0
# while j<runno:
#     vx=[np.cos(thetaarray[j])*v]
#     vy=[np.sin(thetaarray[j])*v]
#     sx=[0.0]
#     sy=[0.0]
#     i=0
#     while i<length-1:
#         vy.append(vy[i]+dvy(vy[i]))
#         vx.append(vx[i]+dvx(vx[i]))
#         sy.append(sy[i]+vy[i]*dt)
#         sx.append(sx[i]+vx[i]*dt)
#         if sy[i]<0:
#             time=i
#             break
#         i+=1
#     R.append(sx[time])
#     if R[j]<R[j-1]:
#         maxrange=R[j-1]
#         thetamax=thetaarray[j-1]
#         break
#     j+=1

# number=2001
# powers=np.linspace(-5.4,-3,number)
# i=0
# diameters=[]
# while i<number:
#     diameters.append(10**powers[i])
#     i+=1

# i=0
# masses=[]
# while i<number:
#     masses.append((2*10**3)*(4.0/3.0)*np.pi*((diameters[i])/2)**3)
#     i+=1


# runno=1000
# length=3000000
# thetaarray=np.linspace(0,np.pi/2,runno)
# v=1
# dt=0.0001
# ranges=[]
# angles=[]
# k=0
# while k<number:
#     R=[]
#     D=diameters[k]
#     m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
#     b=B*D
#     def dvy(v):
#         return -g*dt-(b/m)*v*dt
#     def dvx(v):
#         return -(b/m)*v*dt
#     j=0
#     while j<runno:
#         vx=[np.cos(thetaarray[j])*v]
#         vy=[np.sin(thetaarray[j])*v]
#         sx=[0.0]
#         sy=[0.0]
#         i=0
#         while i<length-1:
#             vy.append(vy[i]+dvy(vy[i]))
#             vx.append(vx[i]+dvx(vx[i]))
#             sy.append(sy[i]+vy[i]*dt)
#             sx.append(sx[i]+vx[i]*dt)
#             if sy[i]<0:
#                 time=i
#                 break
#             i+=1
#         R.append(sx[time])
#         if R[j]<R[j-1] and j!=0:
#             ranges.append(R[j-1])
#             angles.append(thetaarray[j-1])
#             break
#         j+=1
#     print('Overall:',((k+1)/number)*100)
#     k+=1

# endtime=tittymilk.time()-starttime
# print(endtime/60,'mins')


# plt.scatter(masses,angles,c=angles,s=0.5,cmap='rainbow')
# plt.xscale('log')
# plt.savefig('BigGay.pdf')