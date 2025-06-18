import streamlit as st

st.title("Kalender en Afbeeldingen")

# Eerst de drie hoofdthema's naast elkaar
col1, col2, col3 = st.columns(3)

with col1:
    st.write("## Gezin")
    st.image("https://loremflickr.com/400/300/family", caption="Gezin")

with col2:
    st.write("## Moeder")
    st.image("https://loremflickr.com/400/300/mother", caption="Moeder")

with col3:
    st.write("## Lover")
    st.image("https://loremflickr.com/400/300/lovers", caption="Lover")

# Daaronder de kalender
st.write("Selecteer een datum:")
selected_date = st.date_input("Datum")
