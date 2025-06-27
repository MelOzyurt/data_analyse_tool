import streamlit as st
from analysis_utils import *
from utils_text import *

st.title("🧠 Data Analysis Tool")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)

    option = st.selectbox("Select Analysis Type", [
        "Numeric Summary",
        "Correlation Matrix",
        "Chi-Square Test",
        "Custom Analysis"
    ])

    if option == "Numeric Summary":
        result = analyze_numeric(df)
        st.write(result)
        st.markdown("### Findings")
        st.write("Basic descriptive stats computed.")

    elif option == "Correlation Matrix":
        fig, corr_df = correlation_plot(df)
        st.plotly_chart(fig)
        st.markdown("### Findings")
        st.write(interpret_correlation(corr_df))

    elif option == "Chi-Square Test":
        result, p_val = chi_square_analysis(df)
        st.write(result)
        st.markdown("### Findings")
        st.write(interpret_chi_square(p_val))

    # More analysis options can go here
