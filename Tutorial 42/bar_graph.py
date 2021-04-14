# pip install myplotlib
import matplotlib.pyplot as plt
x = ["java","javascript","python"]
h = [100,200,300]
c = ["green","red","blue"]
b = [10,20,30]
plt.bar(x,h,width=-0.5,align="edge",color = c,bottom=b,linewidth = 4, edgecolor="black")
plt.xlabel("Computer Language")
plt.ylabel("Value")
plt.title("Sample Bar Graph")
plt.show()