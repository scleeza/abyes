import abyes
import numpy


data = [np.random.binomial(1, 0.4, size=10000), np.random.binomial(1, 0.5, size=10000)]
exp = ab.AbExp(method='analytic', decision_var = 'lift', rule='rope', rope=(-0.01,0.01), plot=True)
exp.experiment(data)
