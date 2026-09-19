import numpy as np
clander = np.random.default_rng(seed=1)
clander = clander.integers(20,50, size=28)

print(clander)
# اجمالي المبيعات
print(clander.sum())
# الايام الي تكون فيها الارقام اكثر من المتوسط
clander_mean = clander.mean()
print(clander [clander > clander_mean])
# مضاعفت مخرجات يوم الجمعه 
print(clander [5] * 5)

clander = clander.reshape(7,4)
clander_mean4 = clander.mean(axis=1)
print(clander)
print(clander_mean4)