using MLJ
using XGBoost
using Plots
using DataFrames
using MLJXGBoostInterface  # Interface to use XGBoost with MLJ

# Load the Iris dataset with MLJ's built-in function
X, y = @load_iris;  # Load features and target separately

# Convert the features to a DataFrame, specifying column names directly
data = DataFrame(X, ["sepal_length", "sepal_width", "petal_length", "petal_width"])
target = y  # This is the target variable (species) as a vector


using CSV
using DataFrames

# Load a CSV version of the Iris dataset, if available
data = CSV.File("iris.csv") |> DataFrame
target = data.species  # Assuming 'species' is the column name for the target
select!(data, Not(:species))  # Drop the target column from the feature DataFrame
