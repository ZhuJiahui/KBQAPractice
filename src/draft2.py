import tensorflow as tf
import numpy as np

num = np.reshape(np.array(range(5)), [5, 1])

num=tf.reshape(num,[5,1,1])
new_num = tf.concat([num] * 5, axis=-2)
# new_num = tf.reshape(new_num, [5, 5,1])

extra_num = np.zeros(shape=[5, 5,1])
extra_num=tf.convert_to_tensor(extra_num,dtype=tf.int32)

final_num=tf.concat([new_num,extra_num],axis=-1)

with tf.Session() as sess:
  tf.global_variables_initializer().run()
  new_num_ = sess.run(new_num)
  print(new_num_.shape)
  print(sess.run(extra_num).shape)
  print(sess.run(final_num).shape)

  # print(sess.run(final_num))
