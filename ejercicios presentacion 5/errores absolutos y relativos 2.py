from math import log10, floor

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

u = 0.14263;
v = 543.21;
x = 5/6;
y = 1/7;
xf = Fraction(5,6)
yf = Fraction(1,7)
n = 4;

print(round_sigfigs(u,n))
print(round_sigfigs(v,n))
print("----------------------------------------------------------------------")
print("u+v")
print('Resultado')
print(round_sigfigs(round_sigfigs(u,n)+round_sigfigs(v,n),n))
print('Valor correcto')
print((v+u))
print('Error absoluto')
print(math.fabs((u+v)-round_sigfigs(round_sigfigs(u,n)+round_sigfigs(v,n),n)))
print('Error relativo')
print(math.fabs((u+v)-round_sigfigs(round_sigfigs(u,n)+round_sigfigs(v,n),n))/math.fabs(u-v))
print("----------------------------------------------------------------------")
print("(y-u)/x")
print('Resultado')
print(round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))/round_sigfigs(x,n),n))
print('Valor correcto')
print((y-u)/x)
print('Error absoluto')
print(math.fabs(((y-u)/x)-round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))/round_sigfigs(x,n),n)))
print('Error relativo')
print(math.fabs(((y-u)/x)-round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))/round_sigfigs(x,n),n))/math.fabs(((y-u)/x))
print("----------------------------------------------------------------------")
print("(y-u)*v")
print('Resultado')
print(round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))+round_sigfigs(v,n),n))
print('Valor correcto')
print((y-u)*v)
print('Error absoluto')
print(math.fabs(((y-u)*v)-round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))*round_sigfigs(v,n),n)))
print('Error relativo')
print(math.fabs(((y-u)*v)-round_sigfigs((round_sigfigs(round_sigfigs(y,n)-round_sigfigs(u,n),n))*round_sigfigs(v,n),n))/math.fabs(((y-u)*v))
