import matplotlib.pyplot as plt
labels = ['hocky', 'Basketball', 'Cricket', 'tennis']
sizes = [25, 30, 20, 20]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.05, 0.05, 0, 0)
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('sports level pie chart')
plt.axis('equal')
plt.show()

