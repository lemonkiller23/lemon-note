#coding=utf-8
#

import time;

max = 100000;
primes = [];

st = time.time();
for v in xrange(2, max):  
   for x in xrange(2, v): 
      if v % x == 0:     
         break            
   else:   
        primes.append(v); 
print primes;
print time.time() - st;  