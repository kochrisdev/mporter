import streamlit as st

st.title("Michael Porter's Five Competitive Forces")

st.write("""
This app allows you to visualize the Five Competitive Forces model 
developed by Michael Porter. Adjust the sliders to see how the 
forces affect the competitive landscape of an industry.
""")

new_entrants = st.slider("Threat of New Entrants", 0, 5, 3)
supplier_power = st.slider("Bargaining Power of Suppliers", 0, 5, 3)
buyer_power = st.slider("Bargaining Power of Buyers", 0, 5, 3)
substitutes = st.slider("Threat of Substitute Products", 0, 5, 3)
rivalry = st.slider("Rivalry Among Existing Competitors", 0, 5, 3)

data = {
    'Force': ['Threat of New Entrants', 'Bargaining Power of Suppliers', 
              'Bargaining Power of Buyers', 'Threat of Substitute Products', 
              'Rivalry Among Existing Competitors'],
    'Strength': [new_entrants, supplier_power, buyer_power, substitutes, rivalry]
}

st.bar_chart(data, x='Force', y='Strength')

st.write("""
Interpretation:
- 0-1: Very low force
- 2-3: Moderate force
- 4-5: Strong force

A higher score indicates a stronger competitive force, 
which generally means a less attractive industry structure.
""")
