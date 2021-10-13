
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1.) How many negative numbers are there?

negative = a < 0
negative

print("This is how many negative numbers there are: ",len(a[negative]))

# 2.) How many positive numbers are there?

positive = a > 0
positive

print("This is how many negative numbers there are: ",len(a[positive]))

# 3.) How many even positive numbers are there?

positive_even = a[(a>0) & (a%2 == 0)]
positive_even

print("This is how many positive even numbers there are: ", len(positive_even))

# 4.) If you were to add 3 to each data point, how many positive numbers would there be?

a2 = a + 3
a2

positive2 = a2 > 0
positive2
print("This is how many positive numbers there are when you add 3 to the array: ", len(a[positive2]))

# 5.) If you squared each number, what would the new mean and standard deviation be?

a3 = a**2
a3


print("This is the new standard deviationg: ",np.std(a))
print("This is the new mean: ",np.mean(a))


print("\n\nThis is the new standard deviationg: ",np.std(a3))
print("This is the new mean: ",np.mean(a3))

# 6.) A common statistical operation on a dataset is centering.
# This means to adjust the data such that the mean of the data is 0. 
#This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

a_is_mean = np.mean(a)

centering = a - a_is_mean
centering

print(np.mean(centering))

# 7.) Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = x − μ σ

z =  a - np.average(a)

z_score = z / np.std(a)

print(z_score)

# 8.) Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.