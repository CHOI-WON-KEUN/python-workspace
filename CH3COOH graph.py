import numpy as np
import matplotlib.pyplot as plt

Ka = 1.8*10**(-5)
C_b = np.arange(0, 0.2, 0.0000001)       # C_b : concentration of conjugated base
H = 0.5 * ((-C_b-Ka) + np.sqrt((C_b+Ka)**2 + 0.4*Ka))

plt.xlim([0, 0.2])
plt.yscale("log")
plt.axhline(10**(-5), 0, 1, color="gray", linestyle="--")
plt.axhline(10**(-4), 0, 1, color="gray", linestyle="--")
plt.axhline(10**(-3), 0, 1, color="gray", linestyle="--")
plt.tick_params(axis="y", which="minor", width=0)
plt.plot(C_b, H)
plt.show()