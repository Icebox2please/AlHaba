import matplotlib.pyplot as plt
x = [3, 3]
y = [5, 1]
x1 = [3, 2.75, 3]
y1 = [5, 4, 3]
x2 = [3, 2.75]
y2 = [3, 1]
x3 = [5, 5]
y3 = [5, 1]
x4 = [5, 5.75, 5]
y4 = [5, 4, 3]
x5 = [6, 6.75, 6]
y5 = [5, 4, 3]
x6 = [6, 6]
y6 = [5, 1]
plt.plot(x,y)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.show()