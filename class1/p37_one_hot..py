import tensorflow as tf
#特征工程：将特征转为one-hot标码
classes = 3
#labels = tf.constant([0,1,2,3,4,5,6])  # 输入的元素值最小为0，最大为2
labels = tf.random.uniform([1,20],minval=0,maxval=3)  #生成2行3列，在0~10之间均匀分布的随机数
labels = tf.cast(labels,dtype=tf.int8)
output = tf.one_hot(labels, depth=classes)
print('=============================outcome===================================')
print('=============================outcome===================================')
print('=============================outcome===================================')
print('=============================outcome===================================')
print("result of labels1:", output)
print("\n")
