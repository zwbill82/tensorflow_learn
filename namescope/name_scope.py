# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     name_scope
   Description :
   Author :       zwb
   date：          2019/9/16
-------------------------------------------------
   Change Activity:
                   2019/9/16:
-------------------------------------------------
"""
__author__ = 'zwb'
import tensorflow as tf

outdir="../outgraph/name_scope"
if __name__ == '__main__':
    with tf.name_scope("Scope_A"):
        a=tf.add(1,2,name='A_add')
        b=tf.multiply(a,3,name="A_mul")

    with tf.name_scope("Scope_B"):
        c=tf.add(4,5,name="B_add")
        d=tf.multiply(c,6,name='B_mul')

    e=tf.add(b,d,name="output")

    writer=tf.summary.FileWriter(outdir,graph=tf.get_default_graph())
    writer.close()