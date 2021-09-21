import tensorflow as tf

x = tf.Variable(4)
x.assign_sub(3)
print("x:", x)  # 4-3=1
