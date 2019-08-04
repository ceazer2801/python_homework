import csv

month_count=0
largest_profit=0
largest_loss=0
total=0
profit_change=0
current_pl=0
last_pl=0

with open("budget_data.csv", 'r') as pl_data_file:
    reader = csv.reader(pl_data_file, delimiter=',')
    header = next(reader)
    
    for row in reader:
        pl_dict = {
            "date":row[0],
            "pl":int(row[1])
        }
   
        if  month_count == 0:
            month_count = 1
            last_pl = pl_dict["pl"]
            net_avg = 0
        else:
            month_count += 1
            current_pl = pl_dict["pl"]
            profit_change = (current_pl - last_pl)
            pl_dict["differance"] = profit_change
            last_pl = current_pl
 
            if pl_dict["differance"] > largest_profit:
                largest_profit = pl_dict["differance"]
                profit_date = pl_dict["date"]
            elif pl_dict["differance"] < largest_loss:
                largest_loss = pl_dict["differance"]
                loss_date = pl_dict["date"]
                
        total += pl_dict["pl"]
        net_avg += profit_change  
        
    avg_change = round(net_avg / (month_count-1), 2)    
            
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
print(f"Total:${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {profit_date} (${largest_profit})")
print(f"Greatest Decrease in Profits: {loss_date} (${largest_loss})")

with open("budget_date.txt", 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total:${total}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {profit_date} (${largest_profit})\n")
    file.write(f"Greatest Decrease in Profits: {loss_date} (${largest_loss})\n")