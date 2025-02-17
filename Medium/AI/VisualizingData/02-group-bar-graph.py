import numpy as np
import matplotlib.pyplot as plt


languages = ['Python', 'JavaScript', 'C++']
men_usage = [40, 35, 30]
women_usage = [45, 30, 25]

# Position of bars on x-axis
x = np.arange(len(languages))
width = 0.35

plt.bar(x - width/2, men_usage, width, label='Men')
plt.bar(x + width/2, women_usage, width, label='Women')

plt.title('Programming Language Usage by Gender')

plt.xlabel('Language')
plt.ylabel('Usage (%)')

plt.xticks(x, languages)
plt.legend()

plt.show()