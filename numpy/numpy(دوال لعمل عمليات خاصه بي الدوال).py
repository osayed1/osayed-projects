import numpy as np
array = np.array([[1,2,3],
                  [4,5,6]])

print(np.sum(array)) # يجمعهم كلهم
print(np.mean(array)) # المتوسط الحسابي
print(np.min(array)) # اقل عدد
print(np.max(array)) # اعلى عدد
print(np.argmin(array)) # مكان اقل رقم
print(np.argmax(array)) # مكان اعلى رقم 

print(np.sum(array, axis=0)) # يجمع الاعمدة 
print(np.sum(array, axis=1)) # يجمع الصفوف

# يستخدم لي تحديد اما صف او اما عامود axis
