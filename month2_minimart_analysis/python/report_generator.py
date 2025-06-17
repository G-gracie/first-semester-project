# Code to generate dictionary summary reports
import json
from collections import Counter

def process_orders(orders, products, exchange_rate=1800, discount_threshold=100, discount_rate=0.10):
    total_sold = Counter()
    revenue_per_customer = {}

    print("\n🔍 Processing Orders...\n")

    for customer, product_id, qty in orders:
        product = products[product_id]
        price_usd = product["price"]
        total_price = price_usd * qty

        # Flag large orders
        if total_price > discount_threshold:
            print(f"🚨 Large order flagged! {customer} ordered {qty}x {product['name']} (${total_price:.2f})")

        # discount
        if total_price > discount_threshold:
            total_price *= (1 - discount_rate)

        # Convert to NGN 
        total_price_ngn = total_price * exchange_rate

        # Aggregate
        total_sold[product["name"]] += qty
        revenue_per_customer[customer] = revenue_per_customer.get(customer, 0) + total_price

    return total_sold, revenue_per_customer


def generate_report(total_sold, revenue_per_customer):
    most_popular = total_sold.most_common(1)[0]
    report = {
        "total_products_sold": sum(total_sold.values()),
        "most_popular_product": {
            "name": most_popular[0],
            "quantity_sold": most_popular[1]
        },
        "revenue_per_customer": revenue_per_customer
    }
    return report


def save_report_to_json(report, filename="sales_report.json"):
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    print(f"\n✅ Report saved to {filename}")


def print_summary(report):
    print("\n📊 Sales Summary Report")
    print("-" * 30)
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"Most Popular Product: {report['most_popular_product']['name']} "
          f"({report['most_popular_product']['quantity_sold']} units)")
    print("\n💰 Revenue by Customer:")
    for customer, revenue in report["revenue_per_customer"].items():
        print(f"  - {customer}: ${revenue:.2f}")
