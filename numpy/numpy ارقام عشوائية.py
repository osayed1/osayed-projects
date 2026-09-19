import numpy as np

rng = np.random.default_rng(seed=1) # السيد يحفض الارقام الي تطلع 

print(rng.integers(1,111 ,size=(2,2))) # يطبع ارقام عشوائية من 1 الى 111
#ال size ذا عدد الصفوف و اذا حطيت اقواس يقوم يصير صفوف و اعمدة

np.random.seed(seed=1)
print(np.random.uniform(0.3, 0.7, size=(2,3))) # ذا يخلي الارقام عشوائية لاكن ارقام بي الفواصل

rng1 = np.random.default_rng()
array = np.array([1,2,5])
rng1.shuffle(array)
print(array)
# يخلي العشوائية داخل اللسته
# 1 اول شي يقله ترا عشوائي 3 شي هو الي يقله لخبط داخل اللسته
