
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext

from checkout_agent.agent import checkout_agent
from catalog_agent.product_catalog import search_products


def save_cart(
    tool_context: ToolContext,
    product_id: str,
    item: str,
    seller: str,
    quantity: int,
    price: float
):
    """
    Save selected product and seller details into session state.
    """

    if quantity < 1:
        return {"status": "error", "message": "Quantity must be at least 1."}

    if price < 0:
        return {"status": "error", "message": "Invalid product price."}

    tool_context.state["product_id"] = product_id
    tool_context.state["item"] = item
    tool_context.state["seller"] = seller
    tool_context.state["quantity"] = quantity
    tool_context.state["price"] = price
    tool_context.state["total_price"] = price * quantity

    return {
        "status": "success",
        "message": f"{item} added to cart."
    }


catalog_agent = LlmAgent(
    name="catalog_agent",
    description="A shopping catalogue agent that searches products from CSV",

    model="gemini-3.8-flash",

    instruction="""
    You are a professional shopping catalogue assistant.

    PRODUCT SOURCE:
    - All products must come from the search_products tool.
    - Never invent product names, sellers, availability or prices.
    - Never use hardcoded product information.

    WORKFLOW:

    1. Understand what the customer wants.
    2. Use search_products to retrieve matching products.
    3. Display product name, category, brand and available sellers.
    4. If multiple sellers offer the same product, compare their prices.
    5. Recommend the lowest-priced available seller.
    6. Ask the customer which seller they prefer.
    7. Ask for the required quantity.
    8. Before saving, ensure the selected product, seller and price
       match the search results and sufficient stock is available.
    9. Use save_cart to save the selected product details.
    10. Ask whether the customer wants to checkout.
    11. If yes, transfer control to checkout_agent.

    IMPORTANT:
    - Use only actual results returned by search_products.
    - Do not claim that a product is available when stock is zero.
    - Do not change seller prices.
    - Show prices in Indian Rupees (₹).
    - Keep responses simple and friendly.
    """,

    tools=[
        search_products,
        save_cart
    ],

    sub_agents=[checkout_agent],

    output_key="catalog_output"
)
