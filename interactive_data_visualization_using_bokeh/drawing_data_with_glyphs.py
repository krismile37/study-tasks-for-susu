# Библиотеки Bokeh
from bokeh.io import output_file
from bokeh.plotting import figure, show
# Данные о координатах x-y
x = [1, 2, 1]
y = [1, 1, 2]
# Рисунок будет отображен в статическом HTML-файле с именем output_file_test.html
output_file('output_file_test.html',
title='Empty Bokeh Figure')
# Настроить общий объект figure()
fig = figure(title='My Coordinates',
plot_height=300, plot_width=300,
x_range=(0, 3), y_range=(0, 3),
toolbar_location=None)
# Нарисуйте координаты в виде кругов
fig.circle(x=x, y=y,
color='green', size=10, alpha=0.5)
# Показать сюжет
show(fig)
