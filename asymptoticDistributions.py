"""
Implementing a quantum walk on the line with the Hadamard Gate
"""

import matplotlib.pyplot as plt
import numpy as np

def asymptotics(n,t):
    '''Calculates the asymptotic distribution for the one dimesnional Hadamard
       walk.'''
    
    # Define the variables a = alpha, k_a = k_alpha
    a = n/t
    k = np.arccos(-a/(1-a**2)**0.5)
    
    # Define the variable om = omega, and its first and second derivatives
    # om1 and om2
    om = np.arcsin(np.sin(k)/2**0.5)
    om1 = -a
    om2 = -np.sin(k)/(1+np.cos(k)**2)**0.5 + \
          np.sin(k)*np.cos(k)/(1+np.cos(k)**2)**1.5

    # Define the function phi
    phi = -om-a*k

    # Calculate the expression for the asymptotic distribution
    d = int((a+1)*t) # Exponent in the expression
    C = (1+(-1)**d)/(np.pi*t*abs(om2)) # The overall factor
    # The two cosine terms
    cosTerms = (1-a)**2 * np.cos(phi*t + np.pi/4)**2 \
               +(1-a**2) * np.cos(phi*t + k + np.pi/4)**2
    P = C*cosTerms # The asymptotic probability

    # Calculation of P_slow.
    P_slow = 2*(1-a)/(np.pi*t*abs(om2))
    
    return P, P_slow



    
    
    
  
    


    


