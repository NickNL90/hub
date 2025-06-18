import streamlit as st

st.title("Kalender en Afbeeldingen")

st.write("Selecteer een datum:")
selected_date = st.date_input("Datum")

st.write("## Gezin")
st.image("https://loremflickr.com/400/300/family", caption="Gezin")

st.write("## Moeder")
st.image("https://loremflickr.com/400/300/mother", caption="Moeder")

st.write("## Lover")
st.image("https://loremflickr.com/400/300/lovers", caption="Lover")
