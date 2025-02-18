Understanding JAX Through Linear Regression in Python
17-Feb-2025

https://medium.com/@ccpythonprogramming/understanding-jax-through-linear-regression-in-python-cc41d2761efb


Install manuall packages
pip install jaxlib


Gradient
represents teh rate of change of a function with respect to its variables
helps find the direction in which a function decreases or increases

jax.grad


Linear Regression
statistical method that models the relationship between an independent variable x
and a dependent variable y using a linear function

y = mx + c
y = wx + b

w = slope
b = y-intercept

Goal
find values of w and b that minimize the difference btwn predicted and actual values


MSE
Mean Squared Error
measures how well the predictions match the actual values


Other use cases for JAX include
Reinforcement Learning
JAX enables efficient policy gradient methods for training agents