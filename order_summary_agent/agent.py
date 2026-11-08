from google.adk.agents import LlmAgent

order_summary_agent = LlmAgent(
    name="order_summary_agent",
    description="An order summary agent that gives a summary of the complete order",
    model="gemini-3.8-flash",
    instruction="""
        Read the following information from SESSION STATE:

        {name}
        {email}
        {mobile}
        {item}
        {seller}
        {quantity}
        {price}
        {total_price}
        {shipping_address}

        Generate a professional order summary.

        Rules:
        - Read ONLY from session state.
        - Show the selected seller.
        - Show unit price and quantity.
        - Calculate nothing yourself; use total_price from state.
        - Never invent missing information.
        """
)