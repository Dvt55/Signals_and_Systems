#Bibliotecas importadas

from numpy import *
from pylab import *
 

# Caracterizando nosso impulso unitario com seu início e a altura do impulso

def delta(n):
    return where(n==0, 1, 0)

# x[n]
def x(n):
    
    return 0.5*delta(n) + 2*delta(n - 1)

# h[n]

def h(n):
    return 2*delta(n) + 2*delta(n - 1) + 1*delta(n-2)
 

n = arange(-5, 6, 1)
y = h(n) + h(n - 1) + h(n-2)
# Plotando o gráfico
# Na linha horizontal temos os valores de n e na vertical os valores de x[n]

fig = figure(1)
fig.set_size_inches((10., 8.))
 
var = fig.add_subplot(3, 2, 1)
var.stem(n, x(n), "k-", "ko", "k-")
var.set_xlim([ -2, 6 ])
var.set_ylim([ 0, 6 ])
var.set_title("$x[n]$")
var.set_xticks(arange(-1, 10, 1))
var.set_xticklabels(arange(-1, 10, 1))


savefig("signal1-1.png", bbox_inches='tight')