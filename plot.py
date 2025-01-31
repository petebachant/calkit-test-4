import matplotlib.pyplot as plt
import os

plt.plot(range(5))

os.makedirs("figs", exist_ok=True)

plt.savefig("figs/plot1.png")
plt.savefig("figs/plot2.png")
