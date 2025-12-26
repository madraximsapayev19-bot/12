data = """T-Shirt,Clothing,20.00,5
Laptop,Electronics,1000.00,1
Toaster,Home,30.00,2
Jeans,Clothing,50.00,2
TV,Electronics,600.00,2
BadLine,NoNumbers,Here
Blender,Home,40.00,1
Sneakers,Clothing,120.00,1"""

with open('sales_data.txt','w') as file:
    file.write(data)

def process_sales_data(filename):
    with open('sales_data.txt','r') as filename:
        total_revenue = {}
        list_revenue = []
        for line in filename:
            try:
                product,category,price,quantity = line.split(',')
                revenue = float(price) * int(quantity)  
                if category in total_revenue:
                    total_revenue[category] += revenue
                else:
                    total_revenue[category] = revenue
                if revenue > 500:
                    list_revenue.append(f"{product}: ${revenue:.2f}")
            except ValueError:
                continue
        return total_revenue,list_revenue

def save_revenue_report(category_totals, high_value_items):
    with open('revenue_report.txt','w') as file:
        file.write('CATEGORY REVENUE SUMMARY\n')
        file.write('------------------------\n')
        for category,total in category_totals.items():
            file.write(f'{category}: ${total:.2f}\n')
        file.write('\n')
        file.write('HIGH VALUE TRANSACTIONS (> $500)\n')
        file.write('--------------------------------\n')
        for item in high_value_items:
            file.write(f'{item}\n')

category_totals, high_value_items = process_sales_data('sales_data.txt')
save_revenue_report(category_totals,high_value_items)
