import streamlit as st

st.title("💱 Currency Converter (Fixed Rates)")

st.write("Available currencies: USD, PKR, EUR")

from_currency = st.selectbox("From Currency", ["USD", "PKR", "EUR"])
to_currency = st.selectbox("To Currency", ["USD", "PKR", "EUR"])
amount = st.number_input("Enter Amount", min_value=0.0)

# Fixed rates
rates = {
    "USD": {"PKR": 280, "EUR": 0.9},
    "PKR": {"USD": 1/280, "EUR": 0.0032},
    "EUR": {"USD": 1.1, "PKR": 310}
}

if st.button("Convert"):
    if from_currency == to_currency:
        result = amount
    elif from_currency in rates and to_currency in rates[from_currency]:
        result = amount * rates[from_currency][to_currency]
    else:
        st.error("Conversion not available")
        result = None

    if result is not None:
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
