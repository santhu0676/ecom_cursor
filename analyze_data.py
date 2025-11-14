"""
Run SQL query joining all tables and display results.
Joins: customers → orders → order_items → products → payments
Outputs: customer_name, product_name, total_quantity, total_value, payment_status
Sorts by total_value DESC and shows top 10 rows.
Also generates visualization of total sales by city.
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_data():
    """Run SQL query joining all tables and display results"""
    print("Analyzing data from SQLite database...")
    
    # Database name
    db_name = 'ecom.db'
    
    if not os.path.exists(db_name):
        print(f"Error: Database {db_name} not found. Please run ingest_data.py first.")
        return
    
    # Create connection to SQLite database
    conn = sqlite3.connect(db_name)
    
    # SQL query to join all tables
    query = """
    SELECT 
        c.name AS customer_name,
        pr.product_name,
        SUM(oi.quantity) AS total_quantity,
        SUM(oi.quantity * pr.price) AS total_value,
        pay.status AS payment_status
    FROM 
        customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products pr ON oi.product_id = pr.product_id
    INNER JOIN payments pay ON o.order_id = pay.order_id
    GROUP BY 
        c.name, pr.product_name, pay.status
    ORDER BY 
        total_value DESC
    LIMIT 10
    """
    
    try:
        # Execute query and load into DataFrame
        df = pd.read_sql_query(query, conn)
        
        # Display results
        print("\n" + "="*80)
        print("TOP 10 SALES BY TOTAL VALUE")
        print("="*80)
        print(df.to_string(index=False))
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.close()
        return
    
    # Generate visualization: Total sales by city
    try:
        print("Generating visualization: Total sales by city...")
        
        # Query for sales by city
        city_query = """
        SELECT 
            c.city,
            SUM(oi.quantity * pr.price) AS total_sales
        FROM 
            customers c
        INNER JOIN orders o ON c.customer_id = o.customer_id
        INNER JOIN order_items oi ON o.order_id = oi.order_id
        INNER JOIN products pr ON oi.product_id = pr.product_id
        INNER JOIN payments pay ON o.order_id = pay.order_id
        WHERE 
            pay.status = 'completed'
        GROUP BY 
            c.city
        ORDER BY 
            total_sales DESC
        """
        
        city_df = pd.read_sql_query(city_query, conn)
        
        # Create visualization
        plt.figure(figsize=(12, 6))
        sns.barplot(data=city_df, x='city', y='total_sales', hue='city', palette='viridis', legend=False)
        plt.title('Total Sales by City', fontsize=16, fontweight='bold')
        plt.xlabel('City', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save the chart
        plt.savefig('sales_by_city.png', dpi=300, bbox_inches='tight')
        print("✅ Visualization saved as sales_by_city.png")
        plt.close()
        
    except Exception as e:
        print(f"Error generating visualization: {e}")
    
    # Close connection
    conn.close()
    print("✅ Data analysis completed successfully")

if __name__ == "__main__":
    analyze_data()

