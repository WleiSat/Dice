from plotly.graph_objs import Bar,Layout
from plotly import offline
from Dice import Dice
diceme=Dice()
diceme2=Dice()

results=[]
for roll_num in range(1000):
    result=diceme.roll()+diceme2.roll()
    results.append(result)
#print(results)
frequencies=[]
max_result=diceme.num_sides+diceme2.num_sides
for value in range(2,max_result+1):  #因为最小和是2
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)
#对结果进行可视化
x_value=list(range(2,max_result+1))
data=[Bar(x=x_value,y=frequencies)]
x_axis_config={'title':'结果'}
y_axis_config={'title':'结果的频率'}
my_layout=Layout(title='掷两个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d12.html'),