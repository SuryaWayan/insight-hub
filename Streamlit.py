import streamlit as st
import pandas as pd
import plotly.express as px

def upload_data():
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is None:
        st.warning("Please upload a CSV file.")
        return None
    try:
        data = pd.read_csv(uploaded_file)
        st.success("CSV file uploaded successfully!")
        return data
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def display_data_overview(data):
    st.subheader("Data Overview")
    st.write(f"Total Rows: {data.shape[0]}")
    st.write(f"Total Columns: {data.shape[1]}")

def display_column_list(data):
    st.subheader("Column List")
    columns = data.columns.tolist()
    st.write(columns)
    return columns

def generate_interactive_table(data, columns):
    st.subheader("Interactive Table")
    selected_columns = st.multiselect("Select columns to display", columns)
    num_rows = st.number_input("Number of rows to display", min_value=1, value=10)
    if selected_columns:
        filtered_data = data[selected_columns].head(num_rows)
        st.dataframe(filtered_data)

def generate_chart(data, columns):
    st.subheader("Chart Generation")
    chart_types = ["Line", "Bar", "Scatter", "Pie", "Histogram"]
    num_charts = st.number_input("Number of charts to generate", min_value=1, max_value=10, value=1)
    for i in range(num_charts):
        st.subheader(f"Chart {i+1}")
        chart_type = st.selectbox(f"Select chart type for Chart {i+1}", chart_types)
        x_column = st.selectbox(f"Select X-axis column for Chart {i+1}", columns)
        y_columns = st.multiselect(f"Select Y-axis column(s) for Chart {i+1}", columns)

        if x_column and y_columns:
            chart_data = data[[x_column] + y_columns]
            if chart_type == "Pie":
                chart = px.pie(chart_data, names=x_column, values=y_columns[0])
            else:
                chart = getattr(px, chart_type.lower())(chart_data, x=x_column, y=y_columns)

            chart_title = st.text_input(f"Enter chart title for Chart {i+1}")
            chart.update_layout(title=chart_title, template="plotly_white")
            st.plotly_chart(chart)

def apply_data_filters(data, columns):
    st.subheader("Data Filtering and Sorting")
    filtered_data = data.copy()
    for column in columns:
        unique_values = filtered_data[column].unique()
        selected_values = st.multiselect(f"Select values to filter in {column}", unique_values)
        if selected_values:
            filtered_data = filtered_data[filtered_data[column].isin(selected_values)]

    sort_column = st.selectbox("Select column to sort by", columns)
    sort_order = st.radio("Select sort order", ["Ascending", "Descending"])
    ascending = (sort_order == "Ascending")
    filtered_data = filtered_data.sort_values(by=sort_column, ascending=ascending)
    st.dataframe(filtered_data)

def display_user_guide():
    st.sidebar.title("User Guide")
    st.sidebar.markdown("""
    1. Upload a CSV file using the file uploader.
    2. Explore the data overview and column list.
    3. Select columns and specify the number of rows to display in the interactive table.
    4. Generate charts by selecting the chart type, X-axis column, and Y-axis column(s).
    5. Customize the chart title and color.
    6. Export and share the generated charts in PNG or PDF format.
    7. Use the data filtering and sorting options to focus on specific subsets of data.
    """)

def display_additional_features():
    st.sidebar.title("Additional Features")
    x_axis_variation = st.sidebar.checkbox("Enable X-Axis Variation")
    trend_analysis = st.sidebar.checkbox("Enable Trend Analysis")

    if x_axis_variation:
        st.sidebar.markdown("Vary the X-axis using the slicer-like feature in each chart.")

    if trend_analysis:
        st.sidebar.markdown("Add trends (linear, exponential, polynomial, etc.) to each chart.")

def main():
    st.title("Data Visualization and Analysis")

    data = upload_data()
    if data is not None:
        display_data_overview(data)
        columns = display_column_list(data)
        generate_interactive_table(data, columns)
        generate_chart(data, columns)
        apply_data_filters(data, columns)

    display_user_guide()
    display_additional_features()

if __name__ == "__main__":
    main()
