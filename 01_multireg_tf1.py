import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
from pandas.io.parsers import read_csv

model = tf.global_variables_initializer();
data = read_csv('price data.csv', sep=',')
xy = np.array(data, dtype=np.float32)

# 4 variables
x_data = xy[:, 1:-1]

# receive prices
y_data = xy[:, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([4, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100001):
    cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 500 == 0:
        print("#", step, " Loss cost: ", cost_)
        print("- Price: ", hypo_[0])

# 학습된 모델을 저장합니다.
saver = tf.train.Saver()
save_path = saver.save(sess, "./saved.cpkt")
print('model is saved.')