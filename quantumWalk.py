"""
Implementing a quantum walk on the line with the Hadamard Gate
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def probabilities(lattice):
    '''Computes the probability at each node'''
    return [sum([abs(amp) **2 for amp in node]) for node in lattice]

def normalize(lattice):
    '''Normalizes the probabilities in lattice'''
    normFactor = math.sqrt(sum(probabilities(lattice)))
    return [[amp/normFactor for amp in node] for node in lattice]

def coin(lattice,theta=np.pi/4):
    '''Does the coin transformation. For theta=pi/4 this is the Hadamard coin.'''
    return normalize([[np.cos(theta)*node[0] + np.sin(theta)*node[1],
                       np.sin(theta)*node[0] -np.cos(theta)*node[1]]
                      for node in lattice])

def shift(lattice):
    '''For each position, shift the left amplitude to the left,
       and the right amplitude to the right '''
    p = len(lattice)
    # Create a new array to hold new amplitudes
    newLattice = [[0,0] for i in range(p)]
    # Perform the shift
    for j in range(1,p-1):
        newLattice[j-1][0]+= lattice[j][0]
        newLattice[j+1][1]+= lattice[j][1]
    # Return the normalized lattice
    return normalize(newLattice)

def runWalk(theta=np.pi/4,n=100,T=100):
    '''Implement the quantum walk'''
    # Initialize the lattice
    p = 2*n + 1
    lattice = [[0,0] for i in range(p)]
    # Create the initial state Psi = |L,0>
    lattice[n] =  [1,0]
    # Loop performs the quantum walk for T steps
    for t in range(T):
        lattice = shift(coin(lattice,theta))
    # Plot the probability distribution
    visualize(lattice)
   
def visualize(lattice):
    '''Plots the probability distribution of the walker'''
    size = len(lattice)  
    n = (size-1)//2
    plt.plot(range(-n, n+1), probabilities(lattice), 'k')
    plt.xlabel('Position')
    plt.ylabel('Probability')
    plt.show()
   
if __name__ == "__main__":
    # Runs the Hadamard Walk
    runWalk(np.pi/4)
   
  
    


    


