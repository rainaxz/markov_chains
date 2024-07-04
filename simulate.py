import markovChains as mc
import numpy as np


e = np.array([[0.1, 0.4, 0.5], [0.6, 0.2, 0.2], [0.2, 0, 0.8]])
a = np.array([[1, 0, 0, 0], [0.1, 0.2, 0.3, 0.4], [0.4, 0.1, 0.3, 0.2], [0, 0, 0, 1]])

mc.e_eigenvector(e)
mc.e_multiplication(e)
mc.e_simulation(e)
mc.a_ck(a)
mc.a_simulation(a)


