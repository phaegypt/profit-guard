import streamlit as st

# Set up the main page configuration
st.set_page_config(page_title="Profit Guard | Professional Financial Tool", 
                   layout="centered",
                   page_icon=":money_with_wings:")

# Stylish header
st.markdown(
    """
    <style>
    .main {background-color: #f5f7fa;}
    .block-container {padding-top: 2rem;}
    .headline {font-family: 'Roboto', sans-serif; font-size: 2.5rem; color: #264653; font-weight: 700;}
    .subheader {font-size:1.3rem; color:#6c757d;}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="headline">Profit Guard</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Protect your margins. Maximize your earnings. Built for serious online hustlers.</div>', unsafe_allow_html=True)
st.write("---")

# Sidebar for platform selection
platforms = ["Amazon FBA", "eBay", "Shopify", "Etsy"]
with st.sidebar:
    st.header("Platform Configuration")
    platform = st.selectbox("Choose Selling Platform", platforms)
    st.markdown("---")

    st.subheader("Input Parameters")
    # User input for revenue and costs
    sale_price = st.number_input("Sale Price ($)", min_value=0.01, value=100.00, step=0.01, format="%.2f")
    cost_of_goods = st.number_input("Cost of Goods Sold ($)", min_value=0.00, value=50.00, step=0.01, format="%.2f")
    shipping_cost = st.number_input("Shipping Cost ($)", min_value=0.00, value=10.00, step=0.01, format="%.2f")
    other_costs = st.number_input("Other Costs ($)", min_value=0.00, value=5.00, step=0.01, format="%.2f")

    # Platform Fees preset based on the platform
    fees = {
        "Amazon FBA": 0.15,
        "eBay": 0.13,
        "Shopify": 0.029 + 0.3/sale_price if sale_price else 0.029,
        "Etsy": 0.05,
    }
    fee_rate = fees.get(platform, 0.0)
    fee_label = {
        "Amazon FBA": "15% Final Fee",
        "eBay": "13% Final Fee",
        "Shopify": f"2.9% + $0.30 per sale",
        "Etsy": "5% Final Fee"
    }
    st.info(f"Platform Fee: {fee_label.get(platform)}", icon="🧾")

# Begin main profit calculation logic
if sale_price > 0:
    if platform == "Shopify":
        total_platform_fee = sale_price * 0.029 + 0.30
    else:
        total_platform_fee = sale_price * fee_rate
    total_costs = (
        cost_of_goods +
        shipping_cost +
        other_costs +
        total_platform_fee
    )
    profit = sale_price - total_costs
    margin = (profit / sale_price) * 100 if sale_price else 0

    # Results at the bottom in "high-end" metric layout
    st.markdown("### Results")
    cols = st.columns(3)
    cols[0].metric(
        label="**Final Profit**",
        value=f"${profit:,.2f}",
        delta=None,
        help="Net profit after all costs and fees."
    )
    cols[1].metric(
        label="**Profit Margin**",
        value=f"{margin:.2f}%",
        delta=None,
        help="Profit as a percentage of revenue."
    )
    cols[2].metric(
        label="**Total Costs**",
        value=f"${total_costs:,.2f}",
        help="Sum of COGS, shipping, other costs, and platform fees."
    )

    with st.expander("**Detailed Breakdown**"):
        st.write(f"**Sale Price:** ${sale_price:,.2f}")
        st.write(f"**COGS:** ${cost_of_goods:,.2f}")
        st.write(f"**Shipping Cost:** ${shipping_cost:,.2f}")
        st.write(f"**Other Costs:** ${other_costs:,.2f}")
        st.write(f"**Platform Fee:** ${total_platform_fee:,.2f} ({fee_label.get(platform)})")
        st.write(f"**Total Costs:** ${total_costs:,.2f}")
        st.write(f"**Profit:** ${profit:,.2f}")
        st.write(f"**Profit Margin:** {margin:.2f}%")
else:
    st.warning("Please enter a sale price greater than $0 to calculate your profit.", icon="⚠️")