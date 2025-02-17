import matplotlib.pyplot as plt


languages = ['Python', 'JavaScript', 'C++', 'Java', 'Go']
popularity = [85, 75, 65, 70, 60]

# Use plt.barh to plot a horizontal graph
plt.bar(languages, popularity, color='teal')

plt.title('Programming Language Popularity')

plt.xlabel('Language')
plt.ylabel('Popularity (%)')

plt.show()