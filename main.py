import pandas as pd
import csv 
import plotly_express as px

with open("class1.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)

total_marks=0
total_entres=len(file_data)

for marks in file_data:
    total_marks+=float(marks[1])



mean=total_marks/total_entres

print("Mean (Average) is -> "+str(mean))

df=pd.read_csv("class1.csv")
fig=px.line(df,y="Marks",x="Student Number")
fig.update_layout(shapes=[
    dict(
        type="line",
        y0= mean, y1= mean,
        x0= 0, x1= total_entres
    )
])
fig.show()  