import csv
from pathlib import Path
import json

menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')
output_path = Path("sales_report.txt")

menu = []
sales = []
report = {}
quantity = 0
price = 0
cost = 0

with open(menu_filepath, 'r') as menu_data:
    reader = csv.reader(menu_data, delimiter=',')
    header = next(reader)
    
    for row in reader:
        menu.append(row)

with open(sales_filepath, 'r') as sales_data:
    reader = csv.reader(sales_data)
    header = next(reader)
    
    for row in reader:
        sales.append(row)
    
    for row in sales:
        quantity = int(row[3])
        menu_item = str(row[4])
        if menu_item not in report:
            report[row[4]]= {
                "01-count": 0,
                "02-revenue":0,
                "03-cogs":0,
                "04-profit":0,
            }
        for line in menu:
            item, cat, description, price, cost = line[0:5]
            price = float(price)
            cost = float(cost)
            if menu_item == item:
                report[menu_item]["01-count"] += quantity
                report[menu_item]["02-revenue"] += price * quantity
                report[menu_item]["03-cogs"] += cost * quantity
                report[menu_item]["04-profit"] += (price - cost) * quantity

    with open(output_path, "w") as file:
        json.dump(report, file, indent=2)


