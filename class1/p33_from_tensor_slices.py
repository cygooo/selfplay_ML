import tensorflow as tf


labels = tf.random.uniform([20,1],minval=0,maxval=3)  #生成2行3列，在0~10之间均匀分布的随机数
labels = tf.cast(labels,dtype=tf.int8)
features = tf.random.normal([20,4],mean=1,stddev=2)  #生成正态分布随机数，均值为1，标准差为2
#print(features)
#print(labels)
w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))
dataset = tf.data.Dataset.from_tensor_slices((features, labels)).batch(5)
print('=============================outcome===================================')
print('=============================outcome===================================')
print('=============================outcome===================================')
print('=============================outcome===================================')
for step, (x_train, y_train) in enumerate(dataset):
    print('step:',step)
    y = tf.matmul(x_train, w1) + b1
    y = tf.nn.softmax(y)
    y_ = tf.one_hot(y_train, depth=5)
    print(y_)
    print('=======================================================================')
