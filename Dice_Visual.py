from plotly.graph_objs import Bar,Layout
from plotly import offline
from Dice import Dice
diceme=Dice()
results=[]
for roll_num in range(1000):
    result=diceme.roll()
    results.append(result)
#print(results)
frequencies=[]
for value in range(1,diceme.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)
#对结果进行可视化
x_value=list(range(1,diceme.num_sides+1))
data=[Bar(x=x_value,y=frequencies)]
x_axis_config={'title':'结果'}
y_axis_config={'title':'结果的频率'}
my_layout=Layout(title='掷一个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html'),