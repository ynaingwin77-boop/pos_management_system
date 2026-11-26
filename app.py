import database as db 

import sqlite3

def add_category(category_name):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            conn.execute(
                "INSERT INTO CATEGORIES (category_name) VALUES (?)",
                (category_name,)
            )
        print(f"Category '{category_name}' added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def view_all_categories():
    conn = sqlite3.connect(db.DB_PATH)
    try:
        cur = conn.execute("SELECT categor_id, category_name FROM CATEGORIES")
        rows = cur.fetchall()
        if not rows:
            print("No categories found.")
            return
        print("\n--- All Categories ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def search_category(category_id):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        cur = conn.execute("SELECT categor_id, category_name FROM CATEGORIES WHERE categor_id = ?", (category_id,))
        row = cur.fetchone()
        if row:
            print(f"Category found: ID: {row[0]}, Name: {row[1]}")
        else:
            print(f"No category found with ID {category_id}.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def update_category(category_id, new_name):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            cur = conn.execute(
                "UPDATE CATEGORIES SET category_name = ? WHERE categor_id = ?",
                (new_name, category_id)
            )
            if cur.rowcount == 0:
                print(f"No category found with ID {category_id}.")
            else:
                print(f"Category ID {category_id} updated successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def delete_category(category_id):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            cur = conn.execute("DELETE FROM CATEGORIES WHERE categor_id = ?", (category_id,))
            
            if cur.rowcount == 0:
                print(f"No category found with ID {category_id}.")
            else:
                #fixed 
                conn.execute("DELETE FROM PRODUCTS WHERE category_id = ?", (category_id,))
                print(f"Category ID {category_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
         
def add_product(product_name , price , category_id , quantity = 0):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            conn.execute(
                "INSERT INTO PRODUCTS (product_name, price, category_id, quantity) VALUES (?, ?, ?, ?)",
                (product_name, price, category_id, quantity)
            )
        print(f"Product '{product_name}' added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def view_all_products():
    conn = sqlite3.connect(db.DB_PATH)
    try:
        cur = conn.execute("SELECT product_id,product_name , price ,category_id, quantity FROM PRODUCTS")
        rows = cur.fetchall()
        if not rows:
            print("No products found.")
            return
        print("\n--- All Products ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Category ID: {row[3]}, Quantity: {row[4]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def search_by_category(category_id):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        cur = conn.execute("SELECT product_id, product_name, price, quantity FROM PRODUCTS WHERE category_id = ?", (category_id,))
        rows = cur.fetchall()
        if not rows:
            print(f"No products found for category ID {category_id}.")
            return
        print(f"\n--- Products in Category ID {category_id} ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def update_product(product_id, new_name, new_price, new_category_id, new_quantity):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            cur = conn.execute(
                "UPDATE PRODUCTS SET product_name = ?, price = ?, category_id = ?, quantity = ? WHERE product_id = ?",
                (new_name, new_price, new_category_id, new_quantity, product_id)
            )
            if cur.rowcount == 0:
                print(f"No product found with ID {product_id}.")
            else:
                print(f"Product ID {product_id} updated successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def delete_product(product_id):
    conn = sqlite3.connect(db.DB_PATH)
    try:
        with conn:
            cur = conn.execute("DELETE FROM PRODUCTS WHERE product_id = ?", (product_id,))
            if cur.rowcount == 0:
                print(f"No product found with ID {product_id}.")
            else:
                print(f"Product ID {product_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        
def main():
    db.create_table()
    while True:
        print("\n--- POS Management System ---")
        print("\n========Category Management========")
        print("1. Add Category")
        print("2. View All Categories")
        print("3. Search Category by ID")
        print("4. Update Category")
        print("5. Delete Category")
        print("\n========Product Management========")
        print("6. Add Product")
        print("7. View All Products")
        print("8. Search Products by Category ID")
        print("9. Update Product")
        print("10. Delete Product")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter category name: ")
            #fixed 
            if category_name == db.get_category_name(category_name):
                print(f"Category '{category_name}' already exists.")
                return
            add_category(category_name)
        elif choice == "2":
            view_all_categories()
        elif choice == "3":
            category_id = int(input("Enter category ID to search: "))
            search_category(category_id)
        elif choice == "4":
            category_id = int(input("Enter category ID to update: "))
            new_name = input("Enter new category name: ")
            update_category(category_id, new_name)
        elif choice == "5":
            category_id = int(input("Enter category ID to delete: "))
            delete_category(category_id)
        elif choice == "6":
            product_name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category_id = int(input("Enter category ID for the product: "))
            quantity = int(input("Enter product quantity: "))
            add_product(product_name, price, category_id, quantity)
        elif choice == "7":
            view_all_products()
        elif choice == "8":
            category_id = int(input("Enter category ID to search products: "))
            search_by_category(category_id)
        elif choice == "9":
            product_id = int(input("Enter product ID to update: "))
            new_name = input("Enter new product name: ")
            new_price = float(input("Enter new product price: "))
            new_category_id = int(input("Enter new category ID for the product: "))
            new_quantity = int(input("Enter new product quantity: "))
            update_product(product_id, new_name, new_price, new_category_id, new_quantity)
        elif choice == "10":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == "11":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()