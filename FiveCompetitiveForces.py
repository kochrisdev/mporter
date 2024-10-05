import streamlit as st

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError as e:
    st.error(f"Failed to import required modules: {e}")
    st.stop()

def create_radar_chart(values):
    try:
        categories = ['Threat of New Entrants', 'Bargaining Power of Suppliers',
                      'Bargaining Power of Buyers', 'Threat of Substitute Products',
                      'Rivalry Among Existing Competitors']
        
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
        values = np.concatenate((values, [values[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)
        ax.set_thetagrids(angles[:-1] * 180/np.pi, categories)
        ax.set_ylim(0, 5)
        ax.set_yticks(np.arange(1, 6))
        ax.set_yticklabels(['1', '2', '3', '4', '5'])
        ax.set_rlabel_position(0)
        
        return fig
    except Exception as e:
        st.error(f"Error in create_radar_chart: {e}")
        return None

st.title("Michael Porter's Five Competitive Forces")

st.write("""
This app allows you to visualize the Five Competitive Forces model 
developed by Michael Porter. Adjust the sliders to see how the 
forces affect the competitive landscape of an industry.
""")

try:
    new_entrants = st.slider("Threat of New Entrants", 0, 5, 3)
    supplier_power = st.slider("Bargaining Power of Suppliers", 0, 5, 3)
    buyer_power = st.slider("Bargaining Power of Buyers", 0, 5, 3)
    substitutes = st.slider("Threat of Substitute Products", 0, 5, 3)
    rivalry = st.slider("Rivalry Among Existing Competitors", 0, 5, 3)

    values = [new_entrants, supplier_power, buyer_power, substitutes, rivalry]

    fig = create_radar_chart(values)
    if fig:
        st.pyplot(fig)
    else:
        st.error("Failed to create the chart.")

    st.write("""
    Interpretation:
    - 0-1: Very low force
    - 2-3: Moderate force
    - 4-5: Strong force

    A higher score indicates a stronger competitive force, 
    which generally means a less attractive industry structure.
    """)
except Exception as e:
    st.error(f"An error occurred: {e}")
