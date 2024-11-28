import streamlit as st
import pandas as pd

# Attempt to import matplotlib and seaborn
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    st.error(f"An import error occurred: {e}. Please ensure the required libraries are installed by running:")
    st.code("pip install matplotlib seaborn pandas", language="bash")
    st.stop()

# App Title
st.title("Visualization Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")
            st.stop()
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    # Display dataset overview
    st.write("### Dataset Overview")
    st.dataframe(df)

    # Visualization selection
    viz_type = st.selectbox("Choose a visualization type", ["Scatter Plot", "Heatmap", "Boxplot"])

    if viz_type == "Scatter Plot":
        st.write("### Scatter Plot")
        x_col = st.selectbox("Select X-axis column", df.columns)
        y_col = st.selectbox("Select Y-axis column", df.columns)
        try:
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error creating scatter plot: {e}")

    elif viz_type == "Heatmap":
        st.write("### Heatmap")
        index_col = st.selectbox("Select Index column", df.columns)
        columns_col = st.selectbox("Select Columns column", df.columns)
        values_col = st.selectbox("Select Values column", df.columns)
        try:
            if pd.api.types.is_numeric_dtype(df[values_col]):
                pivot_table = df.pivot(index=index_col, columns=columns_col, values=values_col)
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="RdBu", ax=ax)
                st.pyplot(fig)
            else:
                st.error("Heatmap requires numeric data for the Values column.")
        except Exception as e:
            st.error(f"Error creating heatmap: {e}")

    elif viz_type == "Boxplot":
        st.write("### Boxplot")
        x_col = st.selectbox("Select X-axis column", df.columns)
        y_col = st.selectbox("Select Y-axis column", df.columns)
        try:
            if pd.api.types.is_numeric_dtype(df[y_col]):
                fig, ax = plt.subplots()
                sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
                st.pyplot(fig)
            else:
                st.error("Boxplot requires numeric data for the Y-axis.")
        except Exception as e:
            st.error(f"Error creating boxplot: {e}")

else:
    st.info("Please upload a dataset to begin.")
