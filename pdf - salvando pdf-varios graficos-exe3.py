import numpy             as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x  = np.linspace(-3,3,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = 1/(1+np.exp(-x))
y4 = np.exp(x)

def retFig(x, y):
    fig = plt.figure()
    a   = plt.plot(x, y)
    return fig

fig1 = retFig(x, y1)
fig2 = retFig(x, y2)
fig3 = retFig(x, y3)
fig4 = retFig(x, y4)

pp = PdfPages('Save multiple plots as PDF.pdf')
pp.savefig(fig1)
pp.savefig(fig2)
pp.savefig(fig3)
pp.savefig(fig4)
pp.close()