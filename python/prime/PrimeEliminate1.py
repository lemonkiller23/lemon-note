#coding=utf-8

import time;

max = 100000
primes = range(3, max + 1, 2)

st = time.time();
for v in primes:
        mp = 2;
        val = v * mp;
        while (v * mp) <= max: 
            try:
                primes.index(v * mp);
            except ValueError:
                pass;
            else : 
                del primes[primes.index(v * mp)];
            mp += 1;
print [2] + primes  
print time.time() - st;
