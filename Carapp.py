import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Display a scatter plot
def scatter_plot(data, x_column, y_column):
    st.write(f"Scatter plot: {x_column} vs {y_column}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)

# Display a heatmap
def heatmap(data, pivot_index, pivot_columns, pivot_values, cmap='RdBu'):
    st.write("Heatmap")
    grouped_pivot = data.pivot(index=pivot_index, columns=pivot_columns, values=pivot_values)
    fig, ax = plt.subplots()
    sns.heatmap(grouped_pivot, cmap=cmap, ax=ax)
    st.pyplot(fig)

# Display a boxplot
def boxplot(data, x_column, y_column):
    st.write(f"Boxplot: {x_column} vs {y_column}")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)

# Example Streamlit app layout
st.title("Visualization Dashboard")

uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx"])
if uploaded_file:
    import pandas as pd
    # Assume CSV or Excel data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Dataset Overview")
    st.write(df.head())

    # User chooses visualization type
    viz_type = st.selectbox("Select visualization type", ["Scatter Plot", "Heatmap", "Boxplot"])
    if viz_type == "Scatter Plot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        scatter_plot(df, x_col, y_col)

    elif viz_type == "Heatmap":
        index_col = st.selectbox("Select Index Column", df.columns)
        columns_col = st.selectbox("Select Columns", df.columns)
        values_col = st.selectbox("Select Values Column", df.columns)
        heatmap(df, index_col, columns_col, values_col)

    elif viz_type == "Boxplot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        boxplot(df, x_col, y_col)
