import cmath
print("Enter complex number. e.g 1+2j") #-1-5j
real_prt, img_prt = input().split("+")
img_prt = int(img_prt.replace('j',''))
complx = complex(int(real_prt),img_prt)
# polar coordinates
print('absolute value(modulus) of complex number')
print(abs(complx))
print('phase of complex number')
print(cmath.phase(complx))
