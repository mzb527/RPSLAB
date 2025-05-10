# Inventory Management System for Clothing Store
# Product Information Extraction System for E-commerce Listings
# Step 1: Sample Listings
listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6 Pro - 512GB @ $890",
    "Invalid Product Listing Without Price"
]

# Step 2: Extracting Information
def extract_product_info(listings):
    """Extract product information (name, price, brand) from listings."""
    results = []  # List to store extracted information

    for listing in listings:
        product_info = {}  # Dictionary to store individual product details
        
        try:
            # Step 3: Handling Variations (Conditional Statements)
            if "-" in listing:
                # Extract name and brand
                name_brand_split = listing.split("-")[0].strip()
                if "(" in name_brand_split:  # Check for additional details
                    product_info["name"] = name_brand_split.split("(")[0].strip()
                    product_info["brand"] = name_brand_split.split()[0]
                else:
                    product_info["name"] = name_brand_split.strip()
                    product_info["brand"] = name_brand_split.split()[0]

                # Extract price
                price_index = listing.find("$")
                if price_index == -1:
                    raise ValueError("Price symbol ($) not found.")
                price_str = listing[price_index+1:]
                product_info["price"] = float(price_str.split()[0])

            elif "@" in listing:
                # Extract name and brand
                name_brand_split = listing.split("-")[0].strip()
                product_info["name"] = name_brand_split.split()[1:].strip()
                product_info["brand"] = name_brand_split.split()[0]

                # Extract price
                price_index = listing.find("$")
                if price_index == -1:
                    raise ValueError("Price symbol ($) not found.")
                price_str = listing[price_index+1:]
                product_info["price"] = float(price_str.split()[0])

            else:
                raise ValueError("Unrecognized format.")

        except ValueError as e:
            print(f"Error processing listing: '{listing}'. Reason: {e}")
            continue  # Skip this listing and move to the next

        except Exception as e:
            print(f"Unexpected error occurred for listing: '{listing}'. Reason: {e}")
            continue

        # Step 4: Storing Results
        results.append(product_info)

    return results

# Call the function and print results
extracted_data = extract_product_info(listings)

print("\nExtracted Product Information:")
for product in extracted_data:
    print(product)