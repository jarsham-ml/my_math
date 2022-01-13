import cmath
print("Enter complex number. e.g 1+2j") #-1-5j
complx = complex(input())
# polar coordinates
print('absolute value(modulus) of complex number')
print(abs(complx))
print('phase of complex number')
print(cmath.phase(complx))
