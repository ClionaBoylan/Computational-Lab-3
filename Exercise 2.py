import numpy as np
import matplotlib.pyplot as plt

D=10**-4
diameters=[9.847450218426972e-05,0.000984745021842697,9.847450218426973e-06,9.847450218426974e-07]
masses=[1e-9,1e-6,1e-12,1e-15]
density=2*10**(3)
V=(4.0/3.0)*np.pi*((D)/2)**3
m=V*density
length=3000000
g=-9.8
B=1.6*(10**-4)
b=B*D
dt=0.0001
dts=[0.0001,0.0005,0.00001,0.0000001]
tols=[0.00001,0.00001,0.000001,0.00000002]
vy=[0.0]

def dvy(v):
    return -g*dt-(b/m)*v*dt

def anal(t):
    return ((m*g)/b)*(np.exp((-b*t)/m)-1)

k=0
while k<1:
    dt=dts[k]
    D=diameters[k]
    m=masses[k]
    b=B*D
    vy=[0.0]
    i=0
    t=0
    vyanal=[0.0]
    diff=[]
    while i<length-1:
        vy.append(vy[i]+dvy(vy[i]))
        vyanal.append(anal(t))
        diff.append(abs(vy[i]-vyanal[i+1]))
        # if vy[i+1]-vy[i]<tols[k]:
        #     break
        if vy[i+1]-vy[i]<0.0000001:
            break
        t=t+dt
        i=i+1
    
    time=np.linspace(0,dt*length,length)
    
    plt.scatter(time[:len(vy)],vy,c=time[:len(vy)],cmap='plasma',s=0.5)
    plt.title(r'm=%skg' %(masses[k]))
    plt.xlabel(r'$t$ (s)')
    plt.ylabel(r'$v_y$ (m/s)')
    plt.xlim(0,len(vy)*dt)
    plt.ylim(0)
    plt.savefig('%s.pdf' %(k))
    plt.show()
    k+=1

# plt.plot(time,vyanal)
# plt.title('Anal')
# plt.xlabel(r'$t$')
# plt.ylabel(r'$v_y$')
# plt.show()

plt.scatter(time[:(len(diff))],diff,s=1,c=time[:len(diff)], cmap='hsv')
plt.xlabel(r'$t$ (s)')
plt.ylabel('Error (m)')
plt.ylim(0)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
# plt.savefig('SkinnyPenis.pdf')
plt.show()

# length=100000000
# h=5
# number=100
# powers=np.linspace(-5,-3,number)
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

# dt=0.0001
# times=[]
# j=0
# while j<number:
#     D=diameters[j]
#     m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
#     b=B*D
#     def dvy(v):
#         return -g*dt-(b/m)*v*dt
#     vy=[0.0]
#     sy=[0.0]
#     i=0
#     while i<length-1:
#         vy.append(vy[i]+dvy(vy[i]))
#         sy.append(sy[i]+vy[i]*dt)
#         if sy[i]>h:
#             times.append((i-1)*dt)
#             break
#         i+=1
#     print(((j+1)/number)*100)
#     j+=1

# plt.scatter(masses,times,s=1.2,c=times,cmap='gist_rainbow')
# plt.xlabel('Mass (kg)')
# plt.ylabel('Time Taken to Fall 5m (s)')
# plt.yscale('log')
# plt.xscale('log')
# plt.show()
