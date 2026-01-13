import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,5,20)
y1 = np.cos(x)
y2 = np.cos(x + 0.2)
y3 = np.cos(x + 0.4)
y4 = np.cos(x + 0.6)
y5 = np.cos(x + 0.8)
y6 = np.cos(x + 1)

# now we decide the actual figure size in inches
fig = plt.figure(figsize=(14,7))

# plt.suptitle('cos without shift',fontweight='bold', fontsize='x-large')
plt.subplots_adjust(hspace=0.3, top=0.8) 
# create subplots 231 means make a 2x3 grid and this is the first plot
plt.subplot(231)
#these are here to show that you can do the same here as for a single plot
plt.title('cos without shift',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y1,color='r')

plt.subplot(232)
plt.title('cos shifted by 0.2',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y2,color='g')
plt.subplot(233)
plt.title('cos shifted by 0.4',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y3,color='b')
plt.subplot(234)
plt.title('cos shifted by 0.6',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y4,color='y')
plt.subplot(235)
plt.title('cos shifted by 0.8',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y5,color='c')
plt.subplot(236)
plt.title('cos shifted by 1',fontsize = 'x-large', fontweight='bold')
plt.ylabel('This is the $y$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.xlabel('This is the $x$ axis',fontsize = 'x-large', fontweight = 'bold')
plt.plot(x,y6,color='m')
# removed extra white space
plt.tight_layout()
plt.show()
