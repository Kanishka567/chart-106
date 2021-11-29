import plotly.express as px
import csv
with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.bar(df,x="Temperature",y="Cold drink sales( â‚¹ )")
    fig.show()