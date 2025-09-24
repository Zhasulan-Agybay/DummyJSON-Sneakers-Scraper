import requests
import csv
from pathlib import Path
from typing import List, Dict

# DummyJSON API Base URL
BASE_URL = "https://dummyjson.com"

# Request headers (it is better to specify a custom User-Agent)
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

def get_categories() -> List[Dict]:
    """
    Get a list of all product categories.
    Returns a list of dictionaries containing category data.
    """
    url = f"{BASE_URL}/products/categories"
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()  # will throw an error if the request fails
    return resp.json()

def get_products_by_category(slug: str) -> List[Dict]:
    """
    Get a list of products in a specific category (slug).
    """
    url = f"{BASE_URL}/products/category/{slug}"
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    return resp.json().get("products", [])

def filter_shoes(products: List[Dict]) -> List[Dict]:
    """
    Filter products to include only those related to footwear.
    The product name, description, and category are checked.
    """
    shoes = []
    for p in products:
        title = (p.get("title") or "").lower()
        category = (p.get("category") or "").lower()
        desc = (p.get("description") or "").lower()
        if "shoe" in title or "shoe" in desc or "shoe" in category:
            shoes.append(p)
    return shoes

def save_csv(data: List[Dict], path: Path) -> None:
    """
    Save the product list to a CSV file.
    The CSV file will include: title, price, category, brand, rating, and description.
    """
    path.parent.mkdir(parents=True, exist_ok=True)  # create a folder if it doesn't exist
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # CSV Headers
        writer.writerow(["Title", "Price", "Category", "Brand", "Rating", "Description"])
        # Data lines
        for p in data:
            writer.writerow([
                p.get("title", ""),
                p.get("price", ""),
                p.get("category", ""),
                p.get("brand", ""),
                p.get("rating", ""),
                p.get("description", "").replace("\n", " ").strip()
            ])

def main():
    # We get all categories
    categories = get_categories()

    # Searching for categories related to footwear
    shoe_categories = [c["slug"] for c in categories if "shoe" in c["slug"].lower()]
    if not shoe_categories:
        print("No shoe-related categories found.")
        return

    # We collect all products from the found categories
    all_products: List[Dict] = []
    for slug in shoe_categories:
        prods = get_products_by_category(slug)
        all_products.extend(prods)

    # Additionally, we filter products
    sneakers = filter_shoes(all_products)

    # Save the result in CSV
    out_path = Path("output/sneakers_dummyjson.csv")
    save_csv(sneakers, out_path)
    print(f"Saved {len(sneakers)} products to {out_path}")

if __name__ == "__main__":
    main()
