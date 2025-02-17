import matplotlib.pyplot as plt


labels = ['Python', 'JavaScript', 'C++', 'Java', 'Go']
sizes = [40, 25, 15, 10, 10] # sum of the slices are equal 100%

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgrey']
explode = (0.1, 0, 0, 0, 0)  # Explode the 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Programming Language Usage')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()