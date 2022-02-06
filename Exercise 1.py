import numpy as np
import matplotlib.pyplot as plt

def f(V,B,C,D):
    return B*(V*D)+C*(V*D)**2

length=100
array1=np.zeros(length)
array2=np.zeros(length)
array3=np.zeros(length)
maxv=7

i=0
while i<length:
    array1[i]=f(maxv*(i/length),0.00016,0.25,0.07)
    array2[i]=f(maxv*(i/length),0.0000,0.25,0.07)
    array3[i]=f(maxv*(i/length),0.00016,0.0,0.07)
    i=i+1

time=np.linspace(0,0.07*maxv,length)
#plt.plot(time,array1,color='red')
plt.plot(time,array2,color='#9B4F96',label=r'$f_{Quadratic}(V)$')
plt.plot(time,array3,color='#0038A8',label=r'$f_{Linear}(V)$')
plt.legend()
plt.xlabel(r'$D \times V$')
plt.ylabel(r'$f(V)$')
plt.suptitle(r'$f(V)$ vs $D \times V$')
plt.title(r'$D=0.07m$, $v_{max}=7m/s$ (Baseball)')
plt.savefig('Baseball.pdf')
plt.show()

maxv=10**-4
i=0
while i<length:
    array1[i]=f(maxv*(i/length),0.00016,0.25,1.5*(10**-6))
    array2[i]=f(maxv*(i/length),0.0000,0.25,1.5*(10**-6))
    array3[i]=f(maxv*(i/length),0.00016,0.0,1.5*(10**-6))
    i=i+1

time=np.linspace(0,1.5*(10**-6)*maxv,length)
#plt.plot(time,array1,color='red')
plt.plot(time,array2,color='#9B4F96',label=r'$f_{Quadratic}(V)$')
plt.plot(time,array3,color='#0038A8',label=r'$f_{Linear}(V)$')
plt.legend()
plt.xlabel(r'$D \times V$')
plt.ylabel(r'$f(V)$')
plt.suptitle(r'$f(V)$ vs $D \times V$',y=1.025)
plt.title(r'$D=1.5\times 10^{-6}m$, $v_{max}=5.0\times 10^{-5}m/s$ (Oil Drop)',y=1.025)
plt.savefig('OilDrop.pdf')
plt.show()

maxv=1
i=0
while i<length:
    array1[i]=f(maxv*(i/length),0.00016,0.25,(10**-3))
    array2[i]=f(maxv*(i/length),0.0000,0.25,(10**-3))
    array3[i]=f(maxv*(i/length),0.00016,0.0,(10**-3))
    i=i+1

time=np.linspace(0,(10**-3)*maxv,length)
plt.plot(time,array1,color='red',label=r'$f(V)$')
plt.plot(time,array2,color='#9B4F96',label=r'$f_{Quadratic}(V)$')
plt.plot(time,array3,color='#0038A8',label=r'$f_{Linear}(V)$')
plt.legend()
plt.xlabel(r'$D \times V$')
plt.ylabel(r'$f(V)$')
plt.suptitle(r'$f(V)$ vs $D \times V$',y=1.025)
plt.title(r'$D=0.001m$, $v_{max}=1m/s$ (Raindrop)',y=1.025)
plt.savefig('Raindrop.pdf')
plt.show()

def g(VD,B,C):
    return B*(VD)+C*(VD)**2

DV=0
dDV=1e-8
length=10000000
array1=[]
array2=[]
array3=[]
middle=[]
linear=[]
i=0
while i<length:
    array1.append(g(dDV*i,0.00016,0.25))
    array2.append(g(dDV*i,0.0,0.25))
    array3.append(g(dDV*i,0.00016,0.0))
    if array2[i]>9*array3[i]:
        quad=i*dDV
        print('Quadratic from:',i*dDV)
        break
    if array3[i]>9*array2[i]:
        linear.append(i*dDV)
    i+=1

print('Linear up to:',linear[-1])
print('Both:',max(linear),',',quad)