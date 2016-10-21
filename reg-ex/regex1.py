#regex examples

import re

r = re.findall('a+', 'ojgaaoronm rhjraaaoire1oi3h21 3obn21o341nu 1948304738\/')
print(r)

r = re.split('[-]]', 'rwrewn : hihr \' jhirhr, KOk')
print(r)
print(len(r))

r = re.match('a', 'a ojgaaoronm a rhjraaaoire1oi3h21 3obn21o341nu 1948304738\/')
print(r)
print(r.group())
print(r.span())

r = re.search('rh', 'a ojgaaoronm a rhjraaaoire1oi3h21 3obn21o341nu 1948304738\/')
print(r)
print(r.group())
print(r.span())
