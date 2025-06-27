def interpret_chi_square(p_value):
    if p_value < 0.05:
        return "There is a statistically significant association between the variables (p < 0.05)."
    else:
        return "There is no statistically significant association (p > 0.05)."

def interpret_correlation(corr_df):
    high_corr = corr_df[(corr_df.abs() > 0.7) & (corr_df != 1.0)]
    if not high_corr.empty:
        return "Some variables are strongly correlated. Check heatmap."
    return "No strong correlations found."
