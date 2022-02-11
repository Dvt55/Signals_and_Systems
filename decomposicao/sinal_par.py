from math  import *
from numpy import *
from pylab import *

# sinal x[n]
def x(n):
    return n**3 - 5
 
fig = figure(1)
fig.set_size_inches((8., 8.))

# Formulas de decomposição de par e ímpar
n = arange(-4., 5.)
par = 0.5 * (x(n) + x(-n))
impar = 0.5 * (x(n) - x(-n))

# Plot do gráfico
var =  fig.add_subplot(2, 1, 1)
var.stem(n, par, "k-", "ko", "k-")
var.set_xlim([ -4., 4. ])
var.set_ylim([ -10, 10 ])
var.set_title("Sinal original $n^3-5$")
var.set_xticks(n)
savefig("sinal-par.png", bbox_inches='tight')
