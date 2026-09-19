from decimal import *

a = Decimal("5.123")
b = Decimal("-0.2")
print(a+b)               # 4.923
print(a.sqrt())          # 2.26
print(b.as_tuple())
# DecimalTuple(sign=1, 
#              digits=(2,), 
#              exponent=-1)
print(b.as_tuple().sign) # 1
print(a.quantize(Decimal('0.1')))
                         # 5.1
print(getcontext().prec) # 28
getcontext().prec = 3
print(a+b)               # 4.92

