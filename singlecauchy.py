#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

fig, ax = plt.subplots(figsize=(8, 7))

ax.set_xlim([0.4,0.68])
ax.set_ylim([0,9.5])

mean,var,skew,kurt = cauchy.stats(moments='mvsk')

x = np.linspace(cauchy.ppf(0.01),cauchy.ppf(0.99),1000000)
y = np.linspace(0,6.6,100)
ons = np.ones(100)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fsize = 18

#2c0032
ax.plot(x, cauchy.pdf(x, loc=0.53432, scale=0.0382 ), color='#6ca6cd', lw=3)#, label='$\Delta=0.0382, \sigma=0.0079$')
#ax.plot(x, cauchy.pdf(x, loc=0.55334, scale=0.0102 ), color='#8c07ee', lw=3, label='$\Delta=0.0102$')
#ax.plot(x, cauchy.pdf(x, loc=0.54545, scale=0.0024 ), color='#ad1927', lw=3, label='$\Delta=0.0024$')
#ax.plot(x, cauchy.pdf(x, loc=0.59613, scale=0.0988 ), color='#f5ce00', lw=3, label='$\Delta=0.0988$')
#ax.plot(x, cauchy.pdf(x, loc=0.53622, scale=0.0349 ), color='#ff6600', lw=3, label='$\Delta=0.0349$')

midp = 0.5*(0.488+0.580)

ax.plot(0.580*ons,y,'-',lw=1,color='#474747')
ax.plot(0.488*ons,y,'-',lw=1,color='#474747')
ax.plot(0.588*ons,y,'--',lw=1,color='#474747')
ax.plot(0.480*ons,y,'--',lw=1,color='#474747')
ax.plot(0.596*ons,y,':',lw=1,color='#7f7f7f')
ax.plot(0.472*ons,y,':',lw=1,color='#7f7f7f')
x1 = np.linspace(0.488,0.580,100)
x2 = np.linspace(0.480,0.588,100)
x3 = np.linspace(0.472,0.596,100)
textoffset = 0.2

ax.plot(x1,4.8*ons,'-',color='r')#, label='$[\\tilde{y}+(\Delta_y+\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+\sigma_{\Delta_y})]$')
ax.plot(x2,2.8*ons,'--',color='r')#, label='$[\\tilde{y}+(\Delta_y+2\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+2\sigma_{\Delta_y})]$')
ax.plot(x3,0.8*ons,':',color='r')#, label='$[\\tilde{y}+(\Delta_y+3\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+3\sigma_{\Delta_y})]$')

# ax.text(0.405, 7.8, '$\Delta=0.0382, \sigma=0.0079$', fontsize=15, bbox=dict(facecolor='None', edgecolor='#6ca6cd', linestyle='-', linewidth=3))
# ax.text(0.405, 8.5, '$[\\tilde{y}+(\Delta_y+\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+\sigma_{\Delta_y})]$', fontsize=15, bbox=dict(facecolor='None', edgecolor='r', linestyle='-', linewidth=3))
# ax.text(0.551, 8.5, '$[\\tilde{y}+(\Delta_y+2\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+2\sigma_{\Delta_y})]$', fontsize=15, bbox=dict(facecolor='None', edgecolor='r', linestyle='--', linewidth=3))
# ax.text(0.551, 7.8, '$[\\tilde{y}+(\Delta_y+3\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+3\sigma_{\Delta_y})]$', fontsize=15, bbox=dict(facecolor='None', edgecolor='r', linestyle=':', linewidth=3))

# ax.text(0.405, 9.5, '$\Delta=0.0382, \sigma=0.0079$', fontsize=fsize,
#         bbox=dict(facecolor='None', edgecolor='#6ca6cd', linestyle='-', linewidth=3))
# ax.text(0.54, 9.5, '$[\\tilde{y}+(\Delta_y+\phantom{1}\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+\phantom{1}\sigma_{\Delta_y})]$', fontsize=fsize,
#         bbox=dict(facecolor='None', edgecolor='r', linestyle='-', linewidth=2))
# ax.text(0.54, 8.75, '$[\\tilde{y}+(\Delta_y+2\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+2\sigma_{\Delta_y})]$', fontsize=fsize,
#         bbox=dict(facecolor='None', edgecolor='r', linestyle='--', linewidth=2))
# ax.text(0.405, 8.75, '$[\\tilde{y}+(\Delta_y+3\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+3\sigma_{\Delta_y})]$', fontsize=fsize,
#         bbox=dict(facecolor='None', edgecolor='r', linestyle=':', linewidth=2))

ax.text(0.405, 9, '$\Delta=0.0382, \sigma=0.0079$', fontsize=fsize,
        bbox=dict(facecolor='None', edgecolor='#6ca6cd', linestyle='-', linewidth=3))
ax.text(0.513, 8.925, '$[\\tilde{y}+(\Delta_y+k\cdot\sigma_{\Delta_y}),\\tilde{y}-(\Delta_y+k\cdot\sigma_{\Delta_y})]$', fontsize=fsize,
        bbox=dict(facecolor='None', edgecolor='#474747', linestyle='-', linewidth=2))
ax.text(0.6, 4.7, '$k=1$', fontsize=fsize,
        bbox=dict(facecolor='None', edgecolor='r', linestyle='-', linewidth=2))
ax.text(0.6, 2.7, '$k=2$', fontsize=fsize,
        bbox=dict(facecolor='None', edgecolor='r', linestyle='--', linewidth=2))
ax.text(0.6, 0.7, '$k=3$', fontsize=fsize,
        bbox=dict(facecolor='None', edgecolor='r', linestyle=':', linewidth=2))

#ax.plot(x2,5.*ons,lw=1,'r--')
#ax.plot(x3,4.*ons,lw=1,'r--')

#ax.legend(loc='best', frameon=False, prop={'size':15})

plt.text(midp,5, '$1-\sigma$ Interval', color='red', fontsize=fsize, horizontalalignment='center')
plt.text(midp,3, '$2-\sigma$ Interval', color='red', fontsize=fsize, horizontalalignment='center')
plt.text(midp,1, '$3-\sigma$ Interval', color='red', fontsize=fsize, horizontalalignment='center')

plt.text(midp, 4.3, '$68.3\%$', color='red', fontsize=fsize, horizontalalignment='center')
plt.text(midp, 2.3, '$95.5\%$', color='red', fontsize=fsize, horizontalalignment='center')
plt.text(midp, 0.3, '$99.7\%$', color='red', fontsize=fsize, horizontalalignment='center')
#ax.set_title('Cauchy PDF')

#plt.text(-2.0,0.2,'$\Delta=0.53$',fontsize=12)
#plt.text(-0.4,0.27,'$\Delta=0.55$',fontsize=12)
#plt.text(0.5,0.3,'$\Delta=0.54$',fontsize=12)
#plt.text(1.7,0.25,'$\Delta=0.59$',fontsize=12)

#plt.text(-11,0.0,'$f(z) = \\frac{\Delta}{\pi(z^2 + \Delta^2)}$', fontsize=20)

plt.xlabel('$y$')
plt.ylabel('$\\rho(y)$')

plt.tight_layout()

fig.savefig('cauchy2_v6.eps',format='eps')
plt.show()
