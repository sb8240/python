# bar-graphs-histograms respectively
import matplotlib.pyplot as plt
import numpy as np
languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y = np.arange(len(languages))
popularity = [10,8,6,4,2,1]
plt.bar(y, popularity, align='center', color='pink')
plt.xticks(y, languages)
plt.ylabel('Popularity')
plt.title('Most loved programming languages')
plt.show()
#===============================================================
data = [[10,30,25,40],
[35,30,20,30],
[20,38,40,29]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X+0.25, data[0], color = 'b', width = 0.25)
ax.bar(X+0.50, data[1], color = 'g', width = 0.25)
ax.bar(X+0.75, data[2], color = 'r', width = 0.25)
plt.show()