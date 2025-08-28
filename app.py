import pandas as pd
import streamlit as st
import io

st.set_page_config(page_title="Health Data Transposer")
st.title("Health Data Transposer")

file = st.file_uploader("Upload your CSV", type="csv")
if file:
    df = pd.read_csv(file, encoding="utf-8")
    pivot_df = df.pivot_table(
        index=['booking_id','booking__customer_age','booking__customer_gender','booking__collection_date','booking__customer_address','booking__client_refid'
'booking__customer_name'],
        columns='test_values__test_parameter__test_name',
        values='test_values__value',
        aggfunc='first'
    ).reset_index()

    st.success("Done! Preview below:")
    st.dataframe(pivot_df.head(20), use_container_width=True)

    csv_bytes = pivot_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download transposed_health_data.csv",
        data=csv_bytes,
        file_name="transposed_health_data.csv",
        mime="text/csv",
    )
