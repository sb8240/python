# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating dataset
cars = ['agreed and wants a solution', 'dont need a new solution']
data = [70,30]


# Creating explode data
explode = (0.1, 0.2)

# Creating color parameters
colors = ( "orange", "cyan")

# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "green" }

# Creating autocpt arguments
# def func(pct, allvalues):
# 	absolute = int(pct / 100.*np.sum(allvalues))
# 	return "{:.1f}%\n({:d} g)".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts = ax.pie(data,
								# autopct = lambda pct: func(pct, data),
								explode = explode,
								labels = cars,
								shadow = True,
								colors = colors,
								startangle = 90,
								wedgeprops = wp,
								textprops = dict(color ="magenta"))

# Adding legend
ax.legend(wedges, cars,
		title ="Cars",
		loc ="center left",
		bbox_to_anchor =(1, 0, 0.5, 1))

plt.setp(texts, size = 20, weight ="bold")
ax.set_title("Surveys Results")

# show plot
plt.show()

