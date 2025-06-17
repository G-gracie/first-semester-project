# Entry point for the MiniMart data reporting system
from report_generator import process_orders, generate_report, save_report_to_json, print_summary


products = {
    1: {"name": "Wireless Mouse", "price": 25.99},
    2: {"name": "Bluetooth Headphones", "price": 79.50},
    3: {"name": "Water Bottle", "price": 12.00},
    4: {"name": "Notebook", "price": 4.99},
    5: {"name": "Smartphone Stand", "price": 9.75}
}

orders = [
    ("Grace", 1, 2),
    ("Samuel", 2, 1),
    ("Linda", 3, 5),
    ("Grace", 2, 1),
    ("Ibrahim", 4, 10),
    ("Ngozi", 5, 3),
    ("Grace", 3, 4),
    ("Samuel", 5, 2)
]


total_sold, revenue_per_customer = process_orders(orders, products)
report = generate_report(total_sold, revenue_per_customer)
print_summary(report)
save_report_to_json(report)
