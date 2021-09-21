import tensorflow as tf

with tf.GradientTape() as tape:  #with结构记录计算过程
    x = tf.Variable(tf.constant(3.0))  #初始值为3.0
    y = tf.pow(x, 2)
grad = tape.gradient(y, x)  #将函数y对x进行求导
print(grad)