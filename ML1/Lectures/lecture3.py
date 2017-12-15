import numpy
from numpy import random

from matplotlib import pyplot as plt
%matplotlib inline

print(numpy.random.uniform(0, 1, [10]))

print(numpy.random.normal(10, 0.01, [10]))

errstd = []
errstd2 = []

n = 10
d = 50
m = 1.0
std = 1

for i in range(100):
    # Sample from a distribution of mean vector 1 and standard
    # deviation 1
    X = numpy.random.normal(m, std, [n, d])

    # Empirical mean
    m_emp = X.mean(axis=0)

    # Some coefficient
    c = (1 - (d-2)*1.0 / n / (m_emp**2).sum())

    # James-Stein-Estimator
    m_js = c * m_emp

    # Error between the true mean and the standard estimator
    errstd += [((m - m_emp)**2).sum()]

    # Error between the true mean and the James-Stein-Estimator
    errstd2 += [((m - m_js)**2).sum()]

print(errstd)
print(errstd2)

plt.figure(figsize=(6, 6))
plt.scatter(errstd, errstd2)
l, h = min(errstd + errstd2), max(errstd + errstd2)
plt.plot([l, h], [l, h], color='red')
plt.xlabel("Error standard estimator")
plt.ylabel("Error James-Stein-Estimator")

plt.show()


fruits = ["watermelon", "apple", "grape", "grapefruit",
          "lemon", "banana", "cherry"]
