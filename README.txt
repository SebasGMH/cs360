Giuliani Martinez Herrera
HW 3 - Parallel Program with mutli-core running
source: https://machinelearningmastery.com/multi-core-machine-learning-in-python/

To demonstrate the execution of a parallel program using different number of cores, I used a machine learning data algorithm from the library sklearn. 
The descision tree algorith, random forest model was used for the example.
A sample data set of 10,000 data points is used to train the model. 
The parameter (n_jobs) in the function RandomForestClassifier(), allows you to manually choose #  of cores.
My machine has 6 cores and 12 logical cores, so I looped through each amount, running and recording execution time.
Execution time was calculated by manually finding the difference (with time()) between times before and after the function was run

Observations
A set of results are:
    >cores=1: 12.431 seconds
    >cores=2: 6.364 seconds
    >cores=3: 4.340 seconds
    >cores=4: 3.352 seconds
    >cores=5: 2.726 seconds
    >cores=6: 2.381 seconds
    >cores=7: 2.095 seconds
    >cores=8: 1.951 seconds
    >cores=9: 1.763 seconds
    >cores=10: 1.648 seconds
    >cores=11: 1.599 seconds
    >cores=12: 1.478 seconds
There is variation of execution times each time I ran the program, however the results are consistant.
As the visualization shows, the relationship between # of cores and execution time is negatively asymptotic,
as cores increase, execution time decreases until the min, determined by Amdahls Law. 
To calculate such value, I would need the fraction that is sequential in the process.


code:
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

