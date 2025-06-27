import streamlit as st
from analysis_utils import *
from utils_text import *

st.title("🧠 Data Analysis Tool")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    analysis_options = [
        "Numeric Summary",
        "Correlation Matrix",
        "Chi-Square Test",
        "Custom Analysis",
        "Histogram",
        "Boxplot",
        "T-Test"
    ]

    option = st.selectbox("Select Analysis Type", analysis_options)

    if option == "Numeric Summary":
        result = analyze_numeric(df)
        st.write(result)
        st.markdown("### Findings")
        st.write("Basic descriptive statistics computed.")

    elif option == "Correlation Matrix":
        fig, corr_df = correlation_plot(df)
        st.plotly_chart(fig)
        st.markdown("### Findings")
        st.write(interpret_correlation(corr_df))

    elif option == "Chi-Square Test":
        # Categorical columns detection
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        st.write("Select two categorical columns for Chi-Square test")
        col1 = st.selectbox("First categorical variable", cat_cols)
        col2 = st.selectbox("Second categorical variable", [c for c in cat_cols if c != col1])

        if st.button("Run Chi-Square Test"):
            if col1 and col2:
                result, p_val = chi_square_analysis(df, col1, col2)
                st.write(result)
                st.markdown("### Findings")
                st.write(interpret_chi_square(p_val))
            else:
                st.error("Please select two different categorical columns.")

    elif option == "Histogram":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        selected_col = st.selectbox("Select numeric column for histogram", num_cols)
        if st.button("Show Histogram"):
            fig = plot_histogram(df, selected_col)
            st.plotly_chart(fig)
            st.markdown("### Findings")
            st.write(f"Histogram of {selected_col} displayed.")

    elif option == "Boxplot":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        selected_col = st.selectbox("Select numeric column for boxplot", num_cols)
        if st.button("Show Boxplot"):
            fig = plot_boxplot(df, selected_col)
            st.plotly_chart(fig)
            st.markdown("### Findings")
            st.write(f"Boxplot of {selected_col} displayed.")

    elif option == "T-Test":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        st.write("Select numeric column and binary categorical column for T-Test")
        num_col = st.selectbox("Numeric variable", num_cols)
        cat_col = st.selectbox("Binary categorical variable", [c for c in cat_cols if df[c].nunique() == 2])
        if st.button("Run T-Test"):
            if num_col and cat_col:
                result = t_test_analysis(df, num_col, cat_col)
                st.write(result)
                st.markdown("### Findings")
                st.write(interpret_t_test(result))
            else:
                st.error("Please select appropriate columns.")

    elif option == "Custom Analysis":
        st.info("Custom analysis options will be added soon.")

else:
    st.info("Please upload a dataset to start analysis.")
