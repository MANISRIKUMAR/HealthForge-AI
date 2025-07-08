import streamlit as st
from synthetic_data import generate_healthcare_data, generate_finance_data

st.title("🧠 Smart Synthetic Data Generator")

domain = st.selectbox("Choose Domain", ["Healthcare", "Finance"])
num_records = st.slider("Number of Records", 1, 100, 10)

if st.button("Generate"):
    if domain == "Healthcare":
        df = generate_healthcare_data(num_records)
    else:
        df = generate_finance_data(num_records)

    st.write(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name=f"{domain}_data.csv", mime="text/csv")
