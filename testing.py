#%% 
# from matplotlib.pylab import *
# x = arange(0, 10)
# scatter(x, x, c=x, facecolors='none')





import matplotlib.pyplot as plt
import matplotlib as mpl
xs, ys = [1,2,3], [2,3,1]
fig, ax = plt.subplots(3)
ax[0].scatter(xs, ys, label='loc-tuple-arg')
ax[0].legend(loc=(1.1, .5, 1.1, "abc"))
plt.show()



# %%
