import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
ds_salaries = pd.read_csv('salaries_cyber.csv')

# Mapping of experience levels to their full forms
experience_level_full_form = {
    'EN': 'Entry-level',
    'MI': 'Mid-level',
    'SE': 'Senior-level',
    'EX': 'Executive'
}

# Applying the full form mapping to the dataset
ds_salaries['experience_level_full'] = ds_salaries['experience_level'].map(experience_level_full_form)

# Function to create a box plot with full form experience levels
def create_box_plot_with_full_experience(df, x, y, title, xlabel, ylabel, color='skyblue'):
    plt.figure(figsize=(10, 6))
    plt.boxplot(df.groupby(x)[y].apply(list), labels=df[x].unique(), showfliers=False, patch_artist=True, boxprops=dict(facecolor=color))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.show()

# Function to create a scatter plot with a specified color and legend
def create_scatter_plot(df, x, y, title, xlabel, ylabel, color='coral'):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], color=color, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Function to create a histogram with title and labels
def create_histogram(df, column, title, xlabel, ylabel, bins=30, color='lightgreen'):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=bins, color=color, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Function to create a line plot for trends over time with title and labels
def create_trend_line_plot(df, x, y, title, xlabel, ylabel, marker_style='o', color='blue'):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x], df[y], marker=marker_style, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Create the box plot with full form experience levels
create_box_plot_with_full_experience(
    df=ds_salaries,
    x='experience_level_full',
    y='salary_in_usd',
    title='Salary Distribution Across Different Experience Levels',
    xlabel='Experience Level',
    ylabel='Salary in USD',
    color='lightblue'
)

# Create the scatter plot with a specified color and legend
create_scatter_plot(
    df=ds_salaries,
    x='experience_level',  # Replace with the correct column name
    y='salary_in_usd',
    title='Salary vs. Numeric Experience Level',
    xlabel='Numeric Experience Level',
    ylabel='Salary in USD',
    color='orange'
)

# Create the histogram with title and labels
create_histogram(
    df=ds_salaries,
    column='salary_in_usd',
    title='Distribution of Salaries in Cyber Security',
    xlabel='Salary in USD',
    ylabel='Frequency',
    bins=30,
    color='lightgreen'
)

# Calculate the average salary by work year
average_salary_by_year = ds_salaries.groupby('work_year')['salary_in_usd'].mean().reset_index()

# Create the line plot for the average salary trend over the years with title and labels
create_trend_line_plot(
    df=average_salary_by_year,
    x='work_year',
    y='salary_in_usd',
    title='Average Salary Trend in Cyber Security (2020-2022)',
    xlabel='Year',
    ylabel='Average Salary in USD',
    marker_style='o',
    color='purple'
)
