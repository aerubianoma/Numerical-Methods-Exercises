from fractions import Fraction
import math

def round_sigfigs(num, sig_figs):
    """Round to specified number of sigfigs.

    >>> round_sigfigs(0, sig_figs=4)
    0
    >>> int(round_sigfigs(12345, sig_figs=2))
    12000
    >>> int(round_sigfigs(-12345, sig_figs=2))
    -12000
    >>> int(round_sigfigs(1, sig_figs=2))
    1
    >>> '{0:.3}'.format(round_sigfigs(3.1415, sig_figs=2))
    '3.1'
    >>> '{0:.3}'.format(round_sigfigs(-3.1415, sig_figs=2))
    '-3.1'
    >>> '{0:.5}'.format(round_sigfigs(0.00098765, sig_figs=2))
    '0.00099'
    >>> '{0:.6}'.format(round_sigfigs(0.00098765, sig_figs=3))
    '0.000988'
    """
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0


x = 5/6;
y = 1/7;
n = 4;
print('Resultado redondeo')
print(round_sigfigs(x,n))
print(round_sigfigs(y,n))
print('Resultado operacion')
print(round_sigfigs(round_sigfigs(x,n)+round_sigfigs(y,n),n))

# Fraction
xf = Fraction(5,6)
yf = Fraction(1,7)
print('Valor correcto')
print(xf+yf)


print('Error absoluto')
print(math.fabs((xf+yf)-round_sigfigs(round_sigfigs(x,n)+round_sigfigs(y,n),n)))

print('Error relativo de la resta')
print((math.fabs((xf-yf)-round_sigfigs(round_sigfigs(x,n)-round_sigfigs(y,n),n)))/math.fabs((xf-yf))) #0.023

print('Error relativo de la multiplicacion')
print((math.fabs((xf*yf)-round_sigfigs(round_sigfigs(x,n)*round_sigfigs(y,n),n)))/math.fabs((xf*yf))) #0.0001

print('Error relativo de la division')
print((math.fabs((xf/yf)-round_sigfigs(round_sigfigs(x,n)/round_sigfigs(y,n),n)))/math.fabs((xf/yf))) #0.0004

print('Error relativo de la suma')
print((math.fabs((xf+yf)-round_sigfigs(round_sigfigs(x,n)+round_sigfigs(y,n),n)))/math.fabs((xf+yf))) #0.024

print("el mayor error absoluto es el de la resta")