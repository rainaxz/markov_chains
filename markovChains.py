import numpy as np
from numpy.linalg import matrix_power, inv
from numpy import transpose
import scipy as sc
import scipy.sparse.linalg as scl
import random as random


#helper function
def normalize(v):
    a = sum(v)
    if a == 0:
        return v
    return v/a

#ergodic eigenvector solution
def e_eigenvector(m):
    mT = m.transpose()
    w, v = scl.eigs(mT, k=1, sigma=1)
    v = v.real
    a = normalize(v)

    print("Eigenvector Solution\n------------------------")
    print(a, "\n")

#ergodic matrix multiplication solution
def e_multiplication(m):
    mT = m.transpose()
    for i in range(6):
        mT = matrix_power(mT, 2)

    print("Matrix Multiplication Solution:\n------------------------")
    print(mT, "\n")

#ergodic simulation solution
def e_simulation(m):


    for i in range(len(m)):
        for j in range(len(m[i])):
            if j > 0:
                m[i][j] = m[i][j - 1] + m[i][j]
            
    #print(m)
    cState = -1
    cProb = []
    final1 = [0] * len(m)
    final2 = []

    for x in range(10):
        for i in range(2000):

            if(i == 0):
                cState = random.randint(0, len(m) - 1)
                cProb = m[cState]
            else:
                rng = random.random()
                for j in range(len(cProb)):
                    if rng <= cProb[j]:
                        cState = j
                        cProb = m[cState]
                        break
                if i >= 1000:
                    final1[cState] += 1

    
        for i in range(len(final1)):
            final1[i] = float(final1[i]/1000)
        
        final2.append(final1)
        final1 = [0] * len(m)
    
    final = np.array(final2)
    final = final.sum(axis=0)
    for i in range(len(final)):
            final[i] = float(final[i]/10)
    
    print("Ergodic Simulation Results:\n------------------------")
    print(final, "\n------------------------\n")



#absorbing solution
def a_ck(m):
    tau = m[1:-1, :]
    #print(tau)
    m1 = [i[0] for i in tau]
    m4 = [i[3] for i in tau]

    #print(m1, m4)
    tau = tau[:, 1:-1]
    #print(tau)

    absorb1 = (inv(np.subtract(np.identity(2), tau))).dot(m1)
    absorb4 = (inv(np.subtract(np.identity(2), tau))).dot(m4)

    print("CK-Equation Solutions\n------------------------")
    print(absorb1, "\n", absorb4, "\n")

    return 0

#absorbing simulation solution
def a_simulation(m):

    print("Absorbing Simulation Result\n------------------------s")

    #convert to cumulative probability for i in range(len(m)):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j > 0:
                m[i][j] = m[i][j - 1] + m[i][j]
    
    #print(m)
    
    
    final2 = [0, 0]
    #start state 2
    for i in range(20000):
        currState2 = 1
        currProb2 = m[1]
        while currState2 != 0 and currState2 != 3:
            rng = random.random()
            for j in range(len(currProb2)):
                if rng <= currProb2[j]:
                    currState2 = j
                    currProb2 = m[currState2]
                    break
    
        if currState2 == 0: 
            final2[0] += 1

        else:
            final2[1] += 1
 
    for i in range(len(final2)):
        final2[i] = float(final2[i]/20000)
    
    print("Starting in state 2:", final2, "\n------------------------")

    final3 = [0, 0]
    #start state 2
    for i in range(20000):
        currState2 = 2
        currProb2 = m[2]
        while currState2 != 0 and currState2 != 3:
            rng = random.random()
            for j in range(len(currProb2)):
                if rng <= currProb2[j]:
                    currState2 = j
                    currProb2 = m[currState2]
                    break
    
        if currState2 == 0: 
            final3[0] += 1

        else:
            final3[1] += 1
 
    for i in range(len(final2)):
        final3[i] = float(final3[i]/20000)

    print("Starting in state 3:", final3, "\n------------------------")



