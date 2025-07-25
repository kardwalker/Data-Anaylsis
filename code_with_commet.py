import pandas as pd

# Create a sample dictionary of people with their work and subject
people = {
    "name": ["walk", "warn", "tread"],
    "work": ["poet", "codeup", "locklong"],
    "sub": ["dsa", "dl", "gen+rag"]
}
# Convert dictionary to DataFrame
df = pd.DataFrame(people)
print(df)

# Accessing a column as a Series
p = df['name']
print(p)
print(type(p))  # <class 'pandas.core.series.Series'>

# Accessing multiple columns as a DataFrame
o = df[['name', 'work']]
print(type(o))  # <class 'pandas.core.frame.DataFrame'>

# Display first few rows
print(df.head())

# Get column names
df.columns

# We can also access columns using dot notation
print(df.columns)

# Accessing rows using iloc (integer location)
q = df.iloc[0]
print(q)
print("lovers")

# Access multiple rows
r = df.iloc[[0, 1]]
print(r)
# Accessing specific rows and columns
p = df.iloc[[0, 1], 2]
print("p : ", p)

# Accessing with loc (label-based, here labels are integers for rows)
g = df.loc[[0, 1], "sub"]
print(g)
j = df.loc[[0, 1], ["sub", "name"]]
print(j)

# Reading survey data from CSV files
file_path = "C:\\Users\\Acer\\Downloads\\stack-overflow-developer-survey-2023\survey_results_public.csv"
fg = pd.read_csv(file_path)
print("\n")
print("\n")
filepath = "C:\\Users\\Acer\\Downloads\\stack-overflow-developer-survey-2023\\survey_results_schema.csv"
schema_df = pd.read_csv(filepath, index_col="qname")
print("fg :\n", fg)
l = fg.columns
print(l[1:])
print(fg["DatabaseHaveWorkedWith"].value_counts())

""" part 4
Filtering"""

print(df)
# Boolean filtering: find rows where 'work' == "poet"
v = df['work'] == "poet"
print(v)
print(df[v])  # returns rows where condition is True
g = df.loc[v]
print("g :", g)
# Combine conditions using & (and), | (or)
j = (df["work"] == "poet") & (df["sub"] == "dsa")
print("j : \n", j)
# ~ operator for negation
print("~v \n", ~v)
f = df.loc[~v]
print(f)

# Slicing rows
t = fg.loc[0:100]
print(t.head(100))
u = fg.loc[1:, "ResponseId":"CompTotal"]  # last value is inclusive
print(u)  # first argument: rows, second: columns
k = fg.loc[1:1000, ["ResponseId", "CompTotal", "ConvertedCompYearly"]]
print(k)  # select specific columns

# Boolean filtering for high salary
high_salary = (fg["ConvertedCompYearly"] > 70000,)
print(high_salary)  # tuple of bool series
y = fg.loc[high_salary]
print(y)
print(y.head(10))

""" now, if we want to see few countries have high salaries """
countries = [" United States", "India", "United Kingdom", "Germany"]
filt = fg['Country'].isin(countries)
print("filt\n", filt)

# Uncomment to try accessing with multiple filters (was causing error in original code)
# q = fg.loc[high_salary, ["Country", "LanguageHaveWorkedWith", "ProfessionalTech", "Industry", "ConvertedCompYearly"]]

"""setting the index"""
df.set_index("name", inplace=True)
df.index
df.reset_index(inplace=True)  # reverse the change
print("schemna_df\n", schema_df.head(40))

# Sorting by index in descending order
schema_df.sort_index(ascending=False, inplace=True)
print(schema_df)

# Optionally set display options for DataFrame
# pd.set_option('display.max_columns', 85)
# pd.set_option('display.max_rows', 85)

""" Filtering rows containing 'Python' in a column """
filt1 = fg['LanguageHaveWorkedWith'].str.contains('Python', na=False)
#print(filt1) # returns boolean mask
print("return the data where python is present\n")
print(fg.loc[filt1])
print(fg.loc[filt1].columns)  # columns in filtered DataFrame
print(type(fg.loc[filt1]))  # <class 'pandas.core.frame.DataFrame'>
print(fg.loc[filt1].shape)  # shape of filtered DataFrame

"""
      python debugger 
"""
import pdb
#  pdb.set_trace() # Uncomment to enable debugger

# Multiple filter simultaneously
print(fg.loc[filt1]['ConvertedCompYearly'][filt])

""" Part 5
Manipulation on rows and columns
"""
# Rename columns by assigning new column names
df.columns = ["name less", " work cup", "soc cor"]

# Uppercase all column names
df.columns = [x.upper() for x in df.columns]
print(df)

# Replace spaces in columns with "- "
df.columns = df.columns.str.replace(" ", "- ")
print(df)

# Rename specific index and columns
df.rename(index={"0": "aplha", "1": " beta", "2": " gamma"},
          columns={"NAME LESS": "gni - ir", "WORK CUP": "ond opl", "SOC COR": "qw lmn"})
print(df)

""" changes in rows """
# If index exists, it will replace the row; else, it will add a new row
print("\n")
df.loc[3] = ["quint", "cluster", "llms"]
print(df)

# Specify changes in a single row & column
df.loc[3, ["NAME- LESS"]] = "nigth"
print(df)

# Add new column by assignment
df.loc[3, "NEW-COLUMN"] = "NEW-VALUE"
print("we add new columns also \n")
print(df)

# Set a single value using .at
df.at[3, "NAME- LESS"] = "night"
print("\n")
fir = (df['NEW-COLUMN'] == "NEW-VALUE")
# Example of improper assignment commented out
# df[fir]["NEW-COLUMN"]) = "FMDMDFVK" 

# Convert columns to lowercase
df.columns = df.columns.str.lower()

"""
apply, map, applymap, replace
"""
# Remove a column
df.drop(columns=["new-column"], inplace=True)
print(df)

# Apply a function along DataFrame axis
print(df.apply(len, axis="columns"))
print(type(df["name- less"].apply(len)))

# Apply minimum function to each column
print(df.apply(pd.Series.min))
print("\n")
# Example using map (would only work on Series, not DataFrame)
print(df.map(len))
df.map(str.lower)
# Note: Would error if numerical data, as str methods can't be run on numbers

# Map values in a specific column according to dict
print(df["soc- cor"].map({"dsa": "scipy", "dl": "sns"}))
print(df)
df["soc- cor"] = df["soc- cor"].replace({"dsa": "scipy", "dl": "sns"})
print(df["soc- cor"])

# Combine columns into a new column
df["long"] = df["name- less"] + " " + df["- work- cup"]

# Remove a column
df.drop(columns=["name- less"], inplace=True)
print("\n")

# Rename columns
df.rename(columns={"- work- cup": "flind"}, inplace=True)
print(df)

# Split a string column into two columns
df["long"].str.split(" ", expand=True)
df[["low ", "higf"]] = df["long"].str.split(" ", expand=True)
print("\n")
print(df)
print("\n")

# Drop rows where a column matches a value
df.drop(index=df[df["higf"] == "codeup"].index, inplace=True)
print(df)

"""
 sorting
"""
# Sort by a column
df.sort_values(by="flind", ascending=False, inplace=True)
# In case of duplicates, pass a list of columns to sort by: by=["flind", "long"]
df.sort_index()
print(fg[["Country", "ConvertedCompYearly"]].head(50))

# Sort DataFrame by multiple columns
print(fg.sort_values(by=["Country", "ConvertedCompYearly"], ascending=False))
print(fg["ConvertedCompYearly"].nlargest(15))
print(fg["ConvertedCompYearly"].nsmallest(5))
print("\n")
# print(df.nlargest[10, "ConvertedCompYearly"])  # This line would error

"""
TypeError: 'method' object is not subscriptable
The error "method object is not subscriptable" typically occurs when you try to use square brackets [] with a method instead of calling the method.
"""
print(fg.nlargest(10, "ConvertedCompYearly"))

"""
Groupby and Aggregation
"""
print("\n")
print("Groupby and Aggregation\n")
print("\n")
print(fg["ConvertedCompYearly"].describe())
print(fg.describe())
# count is the number of non NaN value
print(fg.columns)
print("\n")
print(fg["EdLevel"].value_counts())
print("\n")
print(fg["EdLevel"].value_counts(normalize=True))
print(fg["Country"].value_counts())
print("\n")

# Group by Country column
print(fg.groupby(["Country"]))
country_grp = fg.groupby(["Country"])
# To retrieve group for a specific country
#print(country_grp.get_group("India"))
print("print(country_grp.get_group(India))")
print(country_grp.get_group(("India",))["EdLevel"].value_counts())

print("\n")
print("The method value_counts() is used to count unique occurrences of values in a Series. When you use country_grp.get_group((India,)), it returns a DataFrame, and value_counts() cannot be directly applied to a DataFrame.")

# Equivalent filtering
filt_India = fg["Country"] == "India"
print(fg.loc[filt_India]["EdLevel"].value_counts())

print("\n")
print("\n")
# Normalized value counts per country (proportion in each country)
print(country_grp["EdLevel"].value_counts(normalize=True).unstack().head(20))
# .unstack() transforms the multi-index series into a DataFrame for better readability.

print("\n")
Indian_EdLevel = country_grp["EdLevel"].value_counts(normalize=True).loc["India"]
print("Indian_EdLevel\n", Indian_EdLevel)

"""
agg method
"""
print("\n")
print("agg method\n")
# Aggregate functions per group
print(country_grp["EdLevel"].agg(["count", "nunique"]).head(10))
country_grp["ConvertedCompYearly"].agg(["mean", "median"])
# Show mean and median salary for specific countries
print(country_grp["ConvertedCompYearly"].agg(["mean", "median"]).loc[["India", "Germany"]])
print("\n")
print(fg.loc[filt_India]["LanguageHaveWorkedWith"].str.contains("Python"))
# Number of people in India who know Python
print(fg.loc[filt_India]["LanguageHaveWorkedWith"].str.contains("Python").sum())

# Number of people from each country who know Python
#print(country_grp["LanguageHaveWorkedWith"].str.contains("Python").sum())  # Would error
# Use apply instead
print(country_grp["LanguageHaveWorkedWith"].apply(lambda x: x.str.contains("Python").sum()))
print(country_grp["LanguageHaveWorkedWith"].apply(lambda x: x.str.contains("Python").value_counts(normalize=True)))

# Create DataFrame with respondents and Python knowledge by country
country_respondent = fg["Country"].value_counts()
country_uses_python = (country_grp["LanguageHaveWorkedWith"].apply(lambda x: x.str.contains("Python").sum()))
python_df = pd.concat([country_respondent, country_uses_python], axis="columns", sort=False)
print("python_df")

# Rename columns for clarity
python_df.rename(columns={"count": "Numrespondents", "LanguageHaveWorkedWith": "Numknowspython"}, inplace=True)
print("\n")
print(python_df.columns)
print(python_df)
# To calculate Python knowledge percentage:
# python_df["knowpython"] = (python_df["NumKnowspython"]/python_df["Numrespondents"]) * 100

""" Cleaning data """
print("Cleaning data\n")
import numpy as np

# Example DataFrame with missing values
ple = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
pl = pd.DataFrame(ple)
print(pl)

# Drop all rows with any missing value
print(pl.dropna())
# Drop rows with any NaN in default axis/index
pl.dropna(axis="index", how="any")
# how argument: 'any' drops row if any NaN, 'all' drops only if all are NaN

# Remove rows where email is missing
pl.dropna(axis="index", how="any", subset=["email"])

# Handle custom missing values
pl.replace("NA", np.nan, inplace=True)
pl.replace("Missing", np.nan, inplace=True)

# Check for NaN values
print(pl.isna())

# Fill NaN values with a placeholder
pl.fillna('miss')
print(pl.dtypes)

# Convert 'age' column to float (will error if there are non-numeric values)
pl["age"] = pl["age"].astype(float)
# Note: this will fail if there are still missing/invalid values

# End of code
