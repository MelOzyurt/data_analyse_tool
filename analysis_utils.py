import pandas as pd
import numpy as np
import plotly.express as px
import scipy.stats as stats

# ---------- 1. Numeric Summary ----------
def analyze_numeric(df):
    numeric_df = df.select_dtypes(include=np.number)
    summary = numeric_df.describe().transpose()
    return summary

# ---------- 2. Correlation Plot ----------
def correlation_plot(df):
    numeric_df = df.select_dtypes(include=np.number)
    corr = numeric_df.corr()

    fig = px.imshow(corr,
                    text_auto=True,
                    color_continuous_scale='RdBu_r',
                    title='Correlation Matrix')
    return fig, corr

# ---------- 3. Chi-Square Test ----------
def chi_square_analysis(df, col1=None, col2=None):
    if col1 is None or col2 is None:
        # Just return column names so user can pick
        return {"error": "You must specify two categorical columns."}, None

    contingency = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)

    results = pd.DataFrame({
        "Chi² Statistic": [chi2],
        "Degrees of Freedom": [dof],
        "P-Value": [p]
    })

    return results, p
def load_data(uploaded_file):
    if uploaded_file is None:
        return None
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file type")

import plotly.express as px
from scipy import stats

def plot_histogram(df, col):
    fig = px.histogram(df, x=col, nbins=30, title=f"Histogram of {col}")
    return fig

def plot_boxplot(df, col):
    fig = px.box(df, y=col, title=f"Boxplot of {col}")
    return fig

def t_test_analysis(df, num_col, cat_col):
    groups = df.groupby(cat_col)[num_col].apply(list)
    group1, group2 = groups.iloc[0], groups.iloc[1]
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
    return {"t-statistic": t_stat, "p-value": p_val}

