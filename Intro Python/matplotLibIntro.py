import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-2,2,1000)
y1 = np.cosh(x1)
y2 = 1 + (x1**2)/2
plt.figure()
plt.plot(x1,y1,"r--")
plt.plot(x1,y2,"m")
plt.xlim([-2,2])
plt.ylim([1,4])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["cosh(x)","1+(x^2)/2"], loc="upper right")
plt.title("cosh(x) vs. Parabolic Estimation")
plt.text(-2.0,1.3,"Parabolic estimation")
plt.text(-1.8,3.5,"cosh(x)")

plt.figure()
birth_rate = np.array([16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0])
life_expectancy = np.array([73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7])
capita_gdp = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])
plt.scatter(birth_rate, life_expectancy, s = capita_gdp/10, color="b")
plt.xlim([5,40])
plt.ylim([60,85])
plt.xlabel("Birth rate per 1000")
plt.ylabel("Life expectancy (years)")
