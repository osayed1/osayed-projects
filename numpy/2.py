import numpy as np
array = np.random.default_rng(seed=1)
array = array.integers(0, 255, size=30000)
array = array.reshape(100, 100, 3)
chanle2 = array[40:60, 40:60, :]
print(chanle2)
transpose = np.transpose(chanle2, (2,0,1))
print(transpose)