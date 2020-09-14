#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:54:54 2020

@author: caitlin
"""
import numpy as np
import math as math
import matplotlib as plt
import matplotlib.pyplot as plt

def op_gain(A,N,N_t, ep, P):
    G=A*(N-N_t)*(1-ep*P)
    return G
    
def rate_N(I,q,V,N,T_c, G):
    rate=(I/(q*V))-(N/T_c)-G*P
    return rate
    
def rate_P(G, P, T_p):
    rates=G*P-(P/T_p)
    return rates

T_c=4e-9 #s
T_p=1e-12 #s
A=2e-6 #cm**-3
ep=8e-17 #cm**3
V=(300e-6)*(3e-6)*(0.1e-6)*(100**3) #to cm^3
q=1.6e-19 #c
N_t=2e18 #cm**-3

P_l=40*1e-12  #pulse length
dt=P_l/10000 #s
t=np.arange(0,10*P_l,dt)
I_b=10e-3
I_p=50e-3
    
N_array=np.zeros(len(t))
P_array=np.zeros(len(t))
I_array=np.zeros(len(t))

N=2.5e18
P=6.94e14

for i in range(0, len(t)):    
    time=t[i]
    if 2*P_l <= time <= 3*P_l:
        I=I_p
    elif 7*P_l <= time <= 8*P_l:
        I=I_p
    else:
        I=I_b
    G=op_gain(A, N, N_t, ep, P)
    N=N+dt*rate_N(I, q, V, N, T_c, G)    
    P=P+dt*rate_P(G, P, T_p)
    I_array[i]=I
    P_array[i]=P
    N_array[i]=N

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('Intensity, mA', color=color)
ax1.plot(t*1e9, I_array*1000, color=color, linestyle="dashed")
plt.title("Photon Density, pulse length="+str(round(P_l*1e12))+"ps")
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx() 
color = 'tab:red'
ax2.set_ylabel(r'Photon Density ($\times 10^{15}cm^{-3}$)', color=color)
ax2.plot(t*1e9, P_array*1e-15, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout() 
plt.ylim([-0.2,3])
plt.show()

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('Intensity, mA', color=color)
ax1.plot(t*1e9, I_array*1000, color=color, linestyle="dashed")
plt.title("Carrier Density, pulse length="+str(round(P_l*1e12))+"ps")
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel(r'Carrier Density, ($\times 10^{18}cm^{-3}$)', color=color)  
ax2.plot(t*1e9, N_array*1e-18, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.ylim([2.49,2.67])
plt.show()

#%% All in one plot

P_l=1000*1e-12  #pulse length
dt=P_l/10000 #s
t=np.arange(0,8.5*P_l,dt)

N_array=np.zeros(len(t))
P_array=np.zeros(len(t))
I_array=np.zeros(len(t))

N=2.5e18
P=6.94e14

for i in range(0, len(t)):    
    time=t[i]
    if 2*P_l <= time <= 2*P_l+1e-9:
        I=I_p
    elif 5*P_l <= time <= 5*P_l+0.2e-9:
        I=I_p
    elif 7*P_l <= time <= 7*P_l+0.04e-9:
        I=I_p
    else:
        I=I_b
    G=op_gain(A, N, N_t, ep, P)
    N=N+dt*rate_N(I, q, V, N, T_c, G)    
    P=P+dt*rate_P(G, P, T_p)
    I_array[i]=I
    P_array[i]=P
    N_array[i]=N

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('Intensity, mA', color=color)
ax1.plot(t*1e9, I_array*1000, color=color, linestyle="dashed")
plt.title("Photon Density")
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel(r'Photon Density ($\times 10^{15}cm^{-3}$)', color=color)  # we already handled the x-label with ax1
ax2.plot(t*1e9, P_array*1e-15, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout() 
plt.ylim([-0.2,3])
plt.show()

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (ns)')
ax1.set_ylabel('Intensity, mA', color=color)
ax1.plot(t*1e9, I_array*1000, color=color, linestyle="dashed")
plt.title("Carrier Density")
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel(r'Carrier Density, ($\times 10^{18}cm^{-3}$)', color=color)  
ax2.plot(t*1e9, N_array*1e-18, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  
plt.ylim([2.49,2.67])
plt.show()
