# app/models.py

TABLE_SCHEMA = '''
platform: string
category: string
product_id: string
product_name: string
brand: string
price: float
currency: string
rating: float
reviews_count: integer
specs: object
availability: string
platform_url: string
'''

SCHEMA_DESCRIPTION = '''
This collection contains detailed product information scraped from e-commerce platforms.
Each field represents:
1. platform: The e-commerce platform selling the product
2. category: Product category (e.g., Smartphone)
3. product_id: Unique identifier for the product
4. product_name: Name of the product
5. brand: Product brand
6. price: Price of the product
7. currency: Currency code for the price
8. rating: Average user rating
9. reviews_count: Total number of reviews
10. specs: Product specifications as a nested object, including fields like RAM, storage, processor, display, battery
11. availability: Stock status
12. platform_url: URL link to the product on the platform
'''