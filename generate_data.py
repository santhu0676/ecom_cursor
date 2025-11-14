"""
Generate synthetic e-commerce data using Faker and Random modules.
Creates 5 CSV files with realistic fake data for customers, products, orders, order_items, and payments.
"""

import csv
import random
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_customers(num_customers=50):
    """Generate customer data: customer_id, name, email, city"""
    customers = []
    for i in range(1, num_customers + 1):
        customers.append({
            'customer_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'city': fake.city()
        })
    return customers

def generate_products(num_products=30):
    """Generate product data: product_id, product_name, price"""
    products = []
    product_types = [
        'Laptop', 'Smartphone', 'Headphones', 'Mouse', 'Keyboard',
        'Monitor', 'Tablet', 'Camera', 'Speaker', 'Watch',
        'Charger', 'Case', 'Stand', 'Cable', 'Adapter',
        'SSD', 'RAM', 'Hard Drive', 'USB Drive', 'Router'
    ]
    
    for i in range(1, num_products + 1):
        product_type = random.choice(product_types)
        product_name = f"{product_type} {fake.word().capitalize()} {fake.random_int(min=100, max=999)}"
        price = round(random.uniform(10.0, 2000.0), 2)
        products.append({
            'product_id': i,
            'product_name': product_name,
            'price': price
        })
    return products

def generate_orders(num_orders=40, num_customers=50):
    """Generate order data: order_id, customer_id, order_date"""
    orders = []
    for i in range(1, num_orders + 1):
        orders.append({
            'order_id': i,
            'customer_id': random.randint(1, num_customers),
            'order_date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        })
    return orders

def generate_order_items(num_items=60, num_orders=40, num_products=30):
    """Generate order items data: item_id, order_id, product_id, quantity"""
    order_items = []
    item_id = 1
    
    # Ensure each order has at least one item
    for order_id in range(1, num_orders + 1):
        num_items_in_order = random.randint(1, 5)
        for _ in range(num_items_in_order):
            order_items.append({
                'item_id': item_id,
                'order_id': order_id,
                'product_id': random.randint(1, num_products),
                'quantity': random.randint(1, 10)
            })
            item_id += 1
    
    # Add some additional items to reach target count
    while len(order_items) < num_items:
        order_items.append({
            'item_id': item_id,
            'order_id': random.randint(1, num_orders),
            'product_id': random.randint(1, num_products),
            'quantity': random.randint(1, 10)
        })
        item_id += 1
    
    return order_items[:num_items]  # Limit to num_items

def generate_payments(order_items, products, num_orders=40):
    """Generate payment data: payment_id, order_id, amount, status
    Amount is calculated from order_items and product prices"""
    payments = []
    payment_statuses = ['completed', 'pending', 'failed', 'refunded']
    status_weights = [0.7, 0.15, 0.1, 0.05]  # Most payments are completed
    
    # Create a dictionary to store product prices
    product_prices = {p['product_id']: p['price'] for p in products}
    
    # Calculate order totals from order_items
    order_totals = {}
    for item in order_items:
        order_id = item['order_id']
        product_id = item['product_id']
        quantity = item['quantity']
        price = product_prices.get(product_id, 0)
        
        if order_id not in order_totals:
            order_totals[order_id] = 0
        order_totals[order_id] += quantity * price
    
    # Create a payment for each order
    payment_id = 1
    for order_id in range(1, num_orders + 1):
        # Get order total, or use a default if no items
        amount = order_totals.get(order_id, round(random.uniform(50.0, 500.0), 2))
        amount = round(amount, 2)
        status = random.choices(payment_statuses, weights=status_weights)[0]
        
        payments.append({
            'payment_id': payment_id,
            'order_id': order_id,
            'amount': amount,
            'status': status
        })
        payment_id += 1
    
    return payments

def write_csv(filename, data, fieldnames):
    """Write data to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    """Main function to generate all synthetic data"""
    print("Generating synthetic e-commerce data...")
    
    # Generate data
    num_customers = random.randint(20, 60)
    num_products = random.randint(20, 60)
    num_orders = random.randint(20, 60)
    num_order_items = random.randint(20, 60)
    # Payments will match the number of orders
    
    customers = generate_customers(num_customers)
    products = generate_products(num_products)
    orders = generate_orders(num_orders, num_customers)
    order_items = generate_order_items(num_order_items, num_orders, num_products)
    payments = generate_payments(order_items, products, num_orders)
    
    # Write to CSV files
    write_csv('customers.csv', customers, ['customer_id', 'name', 'email', 'city'])
    write_csv('products.csv', products, ['product_id', 'product_name', 'price'])
    write_csv('orders.csv', orders, ['order_id', 'customer_id', 'order_date'])
    write_csv('order_items.csv', order_items, ['item_id', 'order_id', 'product_id', 'quantity'])
    write_csv('payments.csv', payments, ['payment_id', 'order_id', 'amount', 'status'])
    
    print(f"Generated {len(customers)} customers")
    print(f"Generated {len(products)} products")
    print(f"Generated {len(orders)} orders")
    print(f"Generated {len(order_items)} order items")
    print(f"Generated {len(payments)} payments")
    print("✅ Synthetic data generated successfully")

if __name__ == "__main__":
    main()

