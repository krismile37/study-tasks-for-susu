# Библиотеки Bokeh
from bokeh.io import output_file
from bokeh.plotting import figure, show
# Рисунок будет отображен в статическом HTML-файле с именем output_file_test.html
output_file('output_file_test.html',
title='Empty Bokeh Figure')
# Настроить общий объект figure()
fig = figure()
# Посмотрите, как это выглядит
show(fig)
