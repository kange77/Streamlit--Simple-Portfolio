import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


def main():
    st.set_page_config(page_title="My Experience", page_icon=":rocket:", layout="wide")

    # Title and introduction
    st.title("Welcome to My Experience Showcase")
    st.write("This app showcases my experience in data analysis and visualization using Python and its libraries.")

    # Load data
    data = load_data()

    # Sidebar
    st.sidebar.title("Navigation")
    pages = {
        "Data Overview": page_data_overview,
        "Data Visualization": page_data_visualization,
        "Skills and Experience": page_skills_experience,
    }
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Call the selected page function
    pages[selection](data)


@st.cache_data
def load_data():
    return pd.read_csv("data.csv")


def page_data_overview(data):
    st.header("Data Overview")
    st.write("This section provides an overview of the dataset.")

    st.subheader("Dataset Dimensions")
    st.write(f"Rows: {data.shape[0]}")
    st.write(f"Columns: {data.shape[1]}")

    st.subheader("Data Sample")
    st.write(data.head())


def page_data_visualization(data):
    st.header("Data Visualization")
    st.write("This section visualizes the data using various charts and plots.")

    # Select columns for visualization
    columns = st.multiselect("Select columns to visualize", data.columns)

    # Display selected columns
    if columns:
        st.subheader("Selected Columns")
        st.write(data[columns])

        # Visualization options
        plot_type = st.selectbox("Select Plot Type", ["Line Plot", "Scatter Plot", "Bar Plot", "Histogram"])

        # Create plot
        if plot_type == "Line Plot":
            st.line_chart(data[columns])
        elif plot_type == "Scatter Plot":
            st.scatter_chart(data[columns])
        elif plot_type == "Bar Plot":
            st.bar_chart(data[columns])
        elif plot_type == "Histogram":
            fig, ax = plt.subplots()
            for col in columns:
                sns.histplot(data[col], ax=ax, kde=True)
            st.pyplot(fig)


def page_skills_experience(data):
    st.header("Skills and Experience")
    st.write("This section highlights my skills and experience.")

    st.subheader("Programming Languages")
    languages = ["Python", "SQL", "JavaScript", "Julia"]
    for lang in languages:
        st.write(f"- {lang}")

    st.subheader("Data Analysis Libraries")
    libraries = ["Pandas", "NumPy", "Matplotlib", "Seaborn"]
    for lib in libraries:
        st.write(f"- {lib}")

    st.subheader("Experience")
    experience = [
        "3+ years of experience in data analysis and visualization",
        "Proficient in Python and its data analysis libraries",
        "Experience working with SQL databases",
        "Skilled in creating interactive dashboards using Streamlit and Plotly",
        "Strong problem-solving and analytical skills",
    ]
    for exp in experience:
        st.write(f"- {exp}")


if __name__ == "__main__":
    main()
