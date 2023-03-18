#%% 
# from matplotlib.pylab import *
# x = arange(0, 10)
# scatter(x, x, c=x, facecolors='none')







import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.arange(0, 10)
norm = plt.Normalize(0, 10)
cmap = mpl.colormaps['viridis']
cols = cmap(norm(x))
plt.scatter(x, x, facecolors='none', edgecolors=cols)






















# %%
