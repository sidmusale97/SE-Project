'''

------------------------------------------------------------------------------------
This function is used to compute the mean squared error of a given data set and also
to find the gradient descent of the theta values and minimize the costfunction.
------------------------------------------------------------------------------------
X="input parameters"
y="required output"
theta="parameters to minimize costfunction"
alpha = "Learning rate"
num_iters="Number of iterations to run"
'''
import numpy as np


def computecost(X, y, theta):
    m = y.size
    x = np.transpose(X)
    hypothesis = x.dot(theta)
    sub = np.subtract(hypothesis, y)
    cost = (0.5 / m) * np.sum(sub ** 2)
    return cost


def gradient(X, y, theta, alpha, num_iters):
    m = y.size
    x = np.transpose(X)
    cost_iter = np.zeros((num_iters, 1))
    for i in range(1, num_iters):
        hypothesis = x.dot(theta)
        theta = theta - ((alpha / m) * (np.dot(X, np.subtract(hypothesis, y))))
        cost = computecost(X, y, theta)
        cost_iter[i - 1] = cost
    return theta, cost_iter