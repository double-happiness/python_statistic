import numpy as np

# numpy 中的数组
arr1 = [1, 2, 3, 4, 5]
print('arr1:', arr1)
arr = np.array([1, 2, 3, 4, 5])
print('arr:', arr)

print("打印数组形状，几维及各维长度", arr.shape)

# 创建全0数组
my_new_array = np.zeros((5))
print(my_new_array)

# 创建全1数组
my_new_array = np.ones((5))
print(my_new_array)

# 创建随机值数组
my_random_array = np.random.random((5))
print(my_random_array)

# 创建随机二维数组
my_random_array = np.random.random((3, 5))
print(my_random_array)

# 创建随机三维数组
my_random_array = np.random.random((3, 4, 5))
print(my_random_array)
print(my_random_array.shape)

print("=======获取指定行列=======")
arr = np.array([[1, 2, 3, 4, 5], [4, 5, 7, 8, 9]])
print("获取二维数组第一列：", arr[:, 1])
print("获取二维数组第一行：", arr[1, :])
print("获取二维数组第一行：", arr[1])

print("=======数组四则运算=======")

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum = \n", sum)
print("Difference = \n", difference)
print("对应位置元素相乘矩阵结果  Product = \n", product)
print("Quotient = \n", quotient)
print("矩阵乘法结果：\n", a.dot(b))
