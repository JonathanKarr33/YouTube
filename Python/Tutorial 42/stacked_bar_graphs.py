# pip install myplotlib
import matplotlib.pyplot as plt
sample = [1,2,3]
windows = [64,23,34]
macs = [20,52,23]
plt.bar(sample,windows,0.5,label="Windows")
plt.bar(sample,macs,0.5,bottom=windows,label="macs")
plt.xlabel("Sample")
plt.ylabel("Count")
plt.title("Number of Windows and Macs")
plt.legend()
plt.show()