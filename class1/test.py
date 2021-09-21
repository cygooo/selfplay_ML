import tensorflow as tf
import numpy as np
from tensorflow.python.ops.gen_math_ops import sqrt, square
from tensorflow.python.ops.math_ops import divide, matmul, multiply, subtract

x_0 = np.arange(0,5) 
x_1 = tf.convert_to_tensor(x_0,dtype=tf.int64) 
#数据转换为TF格式

x_2 = tf.zeros([2,3])  
#创建全为零的张量:2行3列

x_3 = tf.ones(4)  
#创建全为1的张量：一维直接填数字

x_4 = tf.fill([2,3],5)  
#创建全为5的2行3列的张量

x_5 = tf.fill([2,2,3,4,5],4)  
#创建多维张量，值全为4

x_6 = tf.random.normal([2,3],mean=1,stddev=2)  
#生成正态分布随机数，均值为1，标准差为2

x_7 = tf.random.truncated_normal([2,3],mean=1,stddev=2)  
#生成截断式正态分布随机数，均值为1，标准差为2

x_8 = tf.random.uniform([2,3],minval=0,maxval=10)  
#生成2行3列，在0~10之间均匀分布的随机数

x_9 = tf.cast(x_8,dtype=tf.int8)  
#强制Tensor的数据类型转换为tf.int8

x_10 = tf.reduce_min(x_8)  
#计算张量维度上元素的最小值

x_11 = tf.reduce_max(x_8)  
#计算张量维度上元素的最大值

x_12 = tf.reduce_mean(x_8,axis=0)  
#计算二维张量沿经度方向的平均值。axis=参数选择0或1确定计算方向。

x_13 = tf.reduce_sum(x_8,axis=1)  
#求和，如果不指定操作轴就默认对全部元素进行操作

w = tf.Variable(tf.random.normal([2,2],mean=0,stddev=1))  
#传入初始值。
#将变量标记为"可训练"，被标记的变量会在反向传播中记录梯度信息。
#神经网络中常用该函数标记待训练参数。

#常用计算函数(加减乘除)：tf.add(a,b), tf.subtract(a,b), tf.multiply, tf.divide
#常用计算函数(平方、次方、开方、矩阵乘)：tf.square, tf.pow, tf.sqrt, tf.matmul
#注意只有维度相同的张量才能进行四则运算。

print(x_8)
print(x_12) 
print(x_13)

#file = open("tensor.txt","w")
#file.write(str(f))
#file.close()
