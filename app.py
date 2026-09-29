import streamlit as st

from menu import display_menu
from billing import calculate_bill, apply_discount
from utils import validate_cart

st.set_page_config(
    page_title="Canteen Food Ordering System",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Canteen / Food Ordering System")

st.write(
    "Select dishes from the menu, choose quantities, "
    "calculate your bill and place your order."
)

st.divider()

menu = display_menu()

st.header("📋 Menu")

for food, price in menu.items():
    st.write(f"**{food}** : ₹{price}")

st.divider()

st.header("🛒 Place Your Order")

selected_items = st.multiselect(
    "Please choose dishes from our menu:",
    list(menu.keys())
)

cart = []

for item in selected_items:

    quantity = st.number_input(
        f"Quantity of {item}",
        min_value=1,
        max_value=20,
        value=1,
        key=f"quantity_{item}"
    )

    for _ in range(quantity):
        cart.append(item)

st.divider()

if st.button(
    "💰 Calculate Bill",
    type="primary",
    use_container_width=True
):

    if not validate_cart(cart):

        st.error("Please select at least one dish.")

    else:

        total = calculate_bill(cart, menu)

        discount = 10

        after_discount = apply_discount(
            total,
            discount
        )

        final_amount = int(after_discount)

        st.success("Bill calculated successfully!")

        st.subheader("🧾 Order Summary")

        for item in selected_items:

            quantity = cart.count(item)

            item_total = menu[item] * quantity

            st.write(
                f"**{item}** × {quantity} "
                f"= ₹{item_total}"
            )

        st.divider()

        st.write(
            f"**Total Amount:** ₹{total}"
        )

        st.write(
            f"**Discount:** {discount}%"
        )

        st.write(
            f"**Final Amount:** ₹{final_amount}"
        )

        st.success(
            f"Thank you for ordering! "
            f"Your final payment amount is ₹{final_amount}."
        )