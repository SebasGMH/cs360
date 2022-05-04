# Giuliani Martinez Herrera
# HW 3 - Parallel Program with mutli-core running
# source: https://machinelearningmastery.com/multi-core-machine-learning-in-python/

# example of comparing number of cores used during training to execution speed
from time import time
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
#from matplotlib import pyplot
import matplotlib.pyplot as plt
# define dataset
X, y = make_classification(n_samples=10000, n_features=20, n_informative=15, n_redundant=5, random_state=3)
results = list()
# compare timing for number of cores
n_cores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for n in n_cores:
	# capture current time
	start = time()
	# define the model
	model = RandomForestClassifier(n_estimators=500, n_jobs=n)
	# fit the model
	model.fit(X, y)
	# capture current time
	end = time()
	# store execution time
	result = end - start
	print('>cores=%d: %.3f seconds' % (n, result))
	results.append(result)
plt.plot(n_cores, results)
plt.xlabel("cores")
plt.ylabel("Execution_time")
plt.savefig("MultiCore.png")
plt.show()