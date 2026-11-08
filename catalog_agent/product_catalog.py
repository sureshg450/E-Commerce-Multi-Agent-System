
import csv
from pathlib import Path


# Resolve CSV path relative to this Python file
CSV_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "products.csv"
)


def search_products(
    keyword: str = "",
    category: str = "",
    max_results: int = 10
) -> dict:
    """
    Search products from the CSV catalogue.

    Supports product name, brand, category and seller searches.
    """

    if not CSV_FILE.exists():
        return {"error": "Product catalogue CSV file not found."}

    products = []

    try:
        with open(
            CSV_FILE,
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                search_text = " ".join([
                    row.get("product_name", ""),
                    row.get("brand", ""),
                    row.get("category", ""),
                    row.get("seller", ""),
                    row.get("description", "")
                ]).lower()

                if keyword.lower() not in search_text:
                    continue

                if category and (
                    row.get("category", "").lower()
                    != category.lower()
                ):
                    continue

                try:
                    price = float(row["price"])
                    stock = int(row["stock"])
                except (ValueError, TypeError, KeyError):
                    continue

                if price < 0 or stock < 0:
                    continue

                products.append({
                    "product_id": row["product_id"],
                    "product_name": row["product_name"],
                    "category": row["category"],
                    "brand": row["brand"],
                    "seller": row["seller"],
                    "price": price,
                    "stock": stock,
                    "description": row["description"]
                })

        return {
            "total_results": len(products),
            "products": products[:max_results]
        }

    except (OSError, csv.Error) as error:
        return {"error": f"Unable to read catalogue: {error}"}
