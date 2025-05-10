# Inventory Management System for Clothing Store    
# Step 1: Creating the Inventory Dictionary
inventory = {}

# Step 2: Adding Items
def add_item(item_id, name, quantity):
    """Add a new item to the inventory."""
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
    print(f"Item '{name}' added with ID '{item_id}' and quantity {quantity}.")

# Step 3: Checking Stock
def check_stock(item_id):
    """Check the stock of a specific item."""
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Item with ID '{item_id}' not found in inventory.")

# Step 4: Updating Stock
def update_stock(item_id, delta):
    """Update the stock quantity of a specific item."""
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item '{item_id}' updated. New quantity: {inventory[item_id]['quantity']}.")
    else:
        print(f"Item with ID '{item_id}' not found in inventory. Update failed.")

# Testing the System

# Adding sample items
add_item("T001", "T-shirt", 50)
add_item("J002", "Jeans", 30)
add_item("S003", "Sneakers", 20)

# Checking stock for existing and non-existing items
print("\nChecking Stock:")
check_stock("T001")
check_stock("X999")  # Non-existent item

# Updating stock quantities
print("\nUpdating Stock:")
update_stock("T001", 10)  # Increase by 10
update_stock("J002", -5)  # Decrease by 5
update_stock("X999", 5)  # Non-existent item

# Checking stock again
print("\nRechecking Stock:")
check_stock("T001")
check_stock("J002")
check_stock("S003")