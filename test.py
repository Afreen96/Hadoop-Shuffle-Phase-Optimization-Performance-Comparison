import matplotlib.pyplot as plt
import pandas
import numpy
url = "final_result.csv"
names = ['dataset_size', 'io.sort.mb', 'io.sort.spill.percent', 'io.sort.factor', 'Execution_time']
ylabel = ['size', 'sortmb', 'spillpercent', 'sortfactor', 'exectime']
data = pandas.read_csv(url, names=names, header=1)
correlations = data.astype('float').corr()
print correlations
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=0, vmax=1)
print cax
fig.colorbar(cax)
ticks = numpy.arange(0,5,1)
print(ticks)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(ylabel)
ax.set_yticklabels(ylabel)
plt.show()