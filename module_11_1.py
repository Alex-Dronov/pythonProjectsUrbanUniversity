import matplotlib.pyplot as plt

students = ['Двоечники', 'Троечники', 'Хорошисты', 'Отличники']
counts = [1, 2, 3, 30]
bar_labels = ['Двоечники', 'Троечники', 'Хорошисты', 'Отличники']
bar_colors = ['k', 'tab:red', 'tab:blue', 'tab:orange']

fig, ax = plt.subplots(1, 2, figsize=(12, 5), facecolor='0.8', sharey=True)

ax[0].bar(students, counts, label=bar_labels, color=bar_colors)
ax[0].set_ylabel('Количество человек')
ax[1].plot(students, counts, color='tab:green', marker='o', ls='-.', mfc='b', ms=7.0)
fig.suptitle('Успеваемость по группе \"ABC\"')
ax[0].legend(title='Цвета успехов и неудач')

plt.show()