# Step 1: Define the product information
products = [
    {
        "name": "Smartphone X",
        "description": "Experience the future with Smartphone X, the ultimate device for connectivity and productivity.",
        "image_url": "http://example.com/smartphone_x.jpg",
        "price": "$999"
    },
    {
        "name": "Eco-Friendly Water Bottle",
        "description": "Stay hydrated and save the planet with our eco-friendly, reusable water bottle.",
        "image_url": "http://example.com/water_bottle.jpg",
        "price": "$25"
    },
    {
        "name": "Noise-Cancelling Headphones",
        "description": "Immerse yourself in music and block out the world with our state-of-the-art headphones.",
        "image_url": "http://example.com/headphones.jpg",
        "price": "$199"
    }
]

# Step 2: Function to print product information
def print_product_info(product):
    print("Product Name:", product["name"])
    print("Description:", product["description"])
    print("Image URL:", product["image_url"])
    print("Price:", product["price"])
    print("-" * 50)

# Step 3: Function to print posts by platform
def print_post_by_platform(product, platform):
    platforms = {
        "facebook": f"Check out our latest product: {product['name']}! {product['description']} For only {product['price']}. See more here: {product['image_url']}",
        "twitter": f"{product['name']} is here! {product['description']} Only {product['price']}! {product['image_url']}",
        "instagram": f"📣 {product['name']} 📣\n{product['description']}\nPrice: {product['price']}\n🛒 {product['image_url']}\n#NewArrival"
    }

    if platform.lower() in platforms:
        print(f"Posting to {platform.title()}:\n{platforms[platform.lower()]}")
    else:
        print(f"Platform {platform} not supported.")
    print("-" * 50)

# Step 4: Loop through products and create posts
print("Generating Posts...\n")
for product in products:
    print_product_info(product)
    for platform in ["facebook", "twitter", "instagram"]:
        print_post_by_platform(product, platform)