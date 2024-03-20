# https://www.guru99.com/tensor-tensorflow.html
# 01-Jan-2019

import tensorflow as tf
import numpy as np

# Default name
r1 = tf.constant(1, tf.int16)
print(r1)

# Named my_scalar
r2 = tf.constant(1, tf.int16, name = "my_scalar")
print(r2)

# Decimal
r1_decimal = tf.constant(1.12345, tf.float32)
print(r1_decimal)
# String
r1_string = tf.constant("Guru99", tf.string)
print(r1_string)


## Rank 1
r1_vector = tf.constant([1,3,5], tf.int16)
print(r1_vector)
r2_boolean = tf.constant([True, True, False], tf.bool)
print(r2_boolean)

## Rank 2
r2_matrix = tf.constant([ [1, 2],
                          [3, 4] ],tf.int16)
print(r2_matrix)

## Rank 3
r3_matrix = tf.constant([ [[1, 2],
                           [3, 4],
                           [5, 6]] ], tf.int16)
print(r3_matrix)


# Shape of tensor
m_shape = tf.constant([ [10, 11],
                        [12, 13],
                        [14, 15] ]
                     )
m_shape.shape

## Rank 3
r3_matrix = tf.constant([ [[1, 2],
                           [3, 4],
                           [5, 6]] ], tf.int16)
print(r3_matrix)


# Shape of tensor
m_shape = tf.constant([ [10, 11],
                        [12, 13],
                        [14, 15] ]
                     )
m_shape.shape


# Create a vector of 0
print(tf.zeros(10))

# Create a vector of 1
print(tf.ones([10, 10]))

# Create a vector of ones with the same number of rows as m_shape
print(tf.ones(m_shape.shape[0]))

# Create a vector of ones with the same number of column as m_shape
print(tf.ones(m_shape.shape[1]))

print(tf.ones(m_shape.shape))



# Change type of data
type_float = tf.constant(3.123456789, tf.float32)
type_int = tf.cast(type_float, dtype=tf.int32)
print(type_float.dtype)
print(type_int.dtype)
