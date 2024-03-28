# App README

## Introduction

This README provides an overview of the functionality and structure of the app.

## App Overview

The app is designed to provide various functionalities for working with data, including data loading, visualization, and showcasing skills and experience.

## Features

### 1. Setup and Introduction

The app sets up the page configuration, including the title, icon, and layout. It displays a title and introduction text to provide context for users.

### 2. Data Loading

The `load_data` function reads a CSV file named "data.csv" attached alongside the code and caches the data for better performance.

### 3. Sidebar Navigation

The app creates a sidebar with navigation options for different pages: "Data Overview", "Data Visualization", and "Skills and Experience". The user can select a page from the radio buttons.

### 4. Page Functions

#### a. Page Data Overview

This function displays an overview of the dataset, including the number of rows and columns, and a sample of the data.

#### b. Page Data Visualization

This function allows the user to select columns from the dataset for visualization. The App user can choose from different plot types (line plot, scatter plot, bar plot, and histogram), and the app displays the selected plot.

#### c. Page Skills and Experience

This function showcases My skills and experience, including programming languages, data analysis libraries, and a list of experience points.

### 5. Main Function

The main function orchestrates the app's logic. It loads the data, creates the sidebar navigation, and calls the selected page function based on the user's choice.

## Installation

To run this app, you'll need to have the following Python libraries installed: Streamlit, Pandas, Matplotlib, and Seaborn. You can install them using pip:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Running the App

After installing the required libraries, you can run the app using the following command:

```bash
streamlit run app.py
```

This command will start the app and open it in your default web browser.

## Additional Information

For additional information or support, please refer to the app documentation or contact me.
