# ADK Shopping Assistant

A conversational shopping assistant built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/). It searches a local product catalog, helps a customer choose a seller and quantity, collects checkout details, and presents an order summary.

## Features

- Searches products by name, brand, category, seller, or description.
- Shows seller options, prices, and stock from a CSV catalog.
- Saves the selected item, seller, quantity, and total in the ADK session state.
- Collects customer contact and shipping details during the conversation.
- Produces an order summary from the details stored in session state.

## How it works

```text
Customer
   |
   v
E-commerce agent
   |
   +--> Catalog agent --> Product search and cart
                              |
                              v
                       Checkout agent
                              |
                              v
                    Order summary agent
```

The catalog is read from [`data/products.csv`](data/products.csv). It includes product IDs, names, categories, brands, sellers, prices, stock quantities, and descriptions. The sample catalog contains products from sellers such as Amazon, Flipkart, Croma, and Reliance Digital.

## Requirements

- Python 3.10 or later
- A Google Gemini API key

## Getting started

1. Clone the repository and open a terminal in its root directory.
2. Create and activate a virtual environment:

   **Windows (PowerShell)**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your Gemini API key in the terminal. For example, in PowerShell:

   ```powershell
   $env:GOOGLE_API_KEY = "your-api-key"
   ```

   Or set `GOOGLE_API_KEY` in a local `.env` file. Do not commit API keys or other secrets.

5. Start the ADK web interface from the repository root:

   ```bash
   adk web
   ```

   Open the local URL printed by ADK and select `ecommerce_agent` to try the assistant.

## Project structure

```text
catalog_agent/       Product search and cart handling
checkout_agent/      Shipping address collection
data/products.csv    Example product catalog
ecommerce_agent/     Root agent and customer information handling
order_summary_agent/ Order summary generation
requirements.txt     Python dependencies
```

## Current scope

This is a learning/demo project. The product catalog is local CSV data, and customer/cart details are kept in ADK session state rather than a persistent database. The root agent's instructions mention order tracking, but an order-tracking agent or tracking data source is not currently included.

## Dependencies

- `google-adk`
- `python-dotenv`

## Result

<img width="1901" height="935" alt="result" src="https://github.com/user-attachments/assets/d011d8bf-e09e-4337-80fc-bc4e36211412" />

