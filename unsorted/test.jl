using Plots

z = [x^2 for x in 1:0.1:10]
p = Plots.plot(z)
Plots.display(p)