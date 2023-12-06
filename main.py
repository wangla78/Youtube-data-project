import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

# Replace 'your_data.csv' with the actual file path or URL of your dataset
path_to_file = "/Users/laurawang/Documents/Youtube Data analysis project with STEM/CAvideos.csv"
df = pd.read_csv(path_to_file)

# Display the first few rows of the DataFrame
print(df.head())

# Get basic statistics of the numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Univariate plots
sns.histplot(df['column_name'], bins=20, kde=True)
plt.show()

# Bivariate plots
sns.scatterplot(x='column1', y='column2', data=df)
plt.show()

# Pair plot for multiple variables
sns.pairplot(df)
plt.show()

# Compute correlation matrix
corr_matrix = df.corr()

# Heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Count plot for a categorical variable
sns.countplot(x='category', data=df)
plt.show()

# 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, x='x_axis', y='y_axis', z='z_axis', color='color_column')
fig.show()
