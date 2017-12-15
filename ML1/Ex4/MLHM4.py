#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:02:42 2017

@author: sisihuang
"""

import utils,numpy,time
%matplotlib inline
# Load the characters "O" and "I" from the handwritten characters dataset
X = utils.load()
print('dataset size: %s'%str(X.shape))
# Plot some statistics of the data using the scatterplot function
utils.scatterplot(X[:,:392].mean(axis=1),X[:,392:].mean(axis=1),
                  xlabel='Average value of pixels 1...392',
                  ylabel='Average value of pixels 393...784')
utils.scatterplot(X[:,::2].mean(axis=1),X[:,1::2].mean(axis=1),
                  xlabel='Average value of even pixels',
                  ylabel='Average value of odd pixels')
# Render some randomly selected examples
R=numpy.random.randint(0,len(X),[25])
utils.render(X[R])

#Ex1.1
Xc = X - numpy.mean(X,axis =0)
t1 = time.time()
U, s, V = numpy.linalg.svd(Xc)
t2 = time.time()
print("time:",(t2-t1)/60, 'min')
#Ex1.2
Xv=Xc.dot(V.transpose())
utils.scatterplot(Xv[:,0], Xv[:,1], xlabel='pca1', ylabel='pca2')
utils.render(V[:25]*s[:25, numpy.newaxis])

#Ex2
S=numpy.dot(Xc.transpose(),Xc)
def J(w): 
    return w.transpose().dot(S).dot(w)

#n,d = X.shape
#x = numpy.ones(d)
#w = x/numpy.linalg.norm(x)
w=numpy.random.rand(784)-.5 
w=w/numpy.linalg.norm(w)

diff = 1
i=0
j_curr = J(w) 
time0 = time.time()

#start iteration process
while diff >= 0.01:
    
    print('iteration'+str(i)+' J(w)='+str(j_curr))
    sw = S.dot(w)
    w = sw/(numpy.linalg.norm(sw))
    j_new = J(w)
    diff = abs(j_new - j_curr) 
    j_curr = j_new
    i += 1
    
time1=time.time()
print('stopping criterion satisfied')
print('Time:'+str(time1-time0)+' seconds')

utils.render(numpy.array([w]))
