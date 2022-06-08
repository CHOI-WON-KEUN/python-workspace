import numpy as np
import matplotlib.pyplot as plt

Ka1 = np.exp(-3.6)
Ka2 = np.exp(-10.32)

pH = np.arange(1, 14, 0.001)
a_H2A = ((np.exp(-pH))**2) / (((np.exp(-pH))**2) + (np.exp(-pH)*Ka1) + (Ka1*Ka2))
a_HA = (np.exp(-pH)*Ka1) / (((np.exp(-pH))**2) + (np.exp(-pH)*Ka1) + (Ka1*Ka2))
a_A = (Ka1*Ka2) / (((np.exp(-pH))**2) + (np.exp(-pH)*Ka1) + (Ka1*Ka2))

plt.title("H2CO3")
plt.legend()
plt.xlabel("pH")
plt.ylabel("mole fraction")
plt.plot(pH, a_H2A, 'r', pH, a_HA, 'b', pH, a_A, 'g')
plt.show()