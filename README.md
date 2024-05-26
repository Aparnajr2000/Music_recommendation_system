# Music_recommendation_system
**Project Overview:**

A music recommendation project that uses clustering to categorize music genres based on audio characteristics. 
We're using a Kaggle dataset that includes popular Spotify songs as well as audio feature information for each one.

**Goals:** To identify similarities between these audio features and categorize music genres based on those similarities. 
This way, we can recommend music that users are likely to like!"

**Data Source:**

https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset/data 

## Solution Flow
### Dimensionality

<img width="962" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/aec25237-89b0-48db-b987-0000c8b16dea">

First thing after importing the data is to check how many rows and columns exist. The info command gives us an overview of the columns, their data types as well as if they have any null values.

Once we have an idea of the number of rows and columns we have we can determine if we can drop any rows, or we might need to repopulate them in case of null or extreme values.

<img width="298" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/3fab6515-b7ca-481d-b1dd-2b4818800c30">

## Data Management
### Data cleaning
**Feature Selection**

Based on examining the features, some of them require considerable thought concerning being included in the final model, as their relevance, correlation, or impact on the model's performance needs to be assessed.

**Index:** This feature has 1994 unique values having an identifiable attribute associated with every track, doesn't offer any relevant data for the model and therefore will be removed from the analysis.

**Title:** This feature, consisting of 1958 category data that is unnecessary in our view, would cause difficulties with the model, so we are removing it to simplify things.

**Artist:** This feature consists of 731 categorical features which will help to identify patterns related to specific artists.

**Year:** This feature has 63 unique values so we would select it as a feature for the model.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/593e24ce-60f3-456c-9d11-38267ac85851">

**Feature Dropping**

It is done to:
- **Improve Model Performance:** Reduce overfitting and enhance generalization.
- **Reduce Complexity:** Simplifies the model for better interpretability.
- **Increase Efficiency:** Speeds up training and prediction times.
- **Enhance Data Quality:** Mitigates the impact of noisy or irrelevant data.
- **Address Multicollinearity:** Eliminates highly correlated features to improve model
accuracy.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/3e61fdac-b3dd-4f03-8a5c-46d1449213ef">

**Duplicate And Null Value**

When sampling is done, certain data points are left blank, and this leads to null values in our dataset. We can't just skip those null value entries, they must be encoded in some way

**Duplicate**

Our dataset has a 0 null value.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/523ffc37-0ba4-4bec-af50-80d28ae84e8d">

**Null value**
We use isnull() to check the null values in a dataset. 
This returns a Boolean value true if there are null values in the dataset and returns False if there are no null values in the dataset.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/f4a19113-e25d-4b6e-8d89-7c071e112c98">

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is the process of examining and visualizing data to uncover patterns, trends, anomalies, and relationships, helping to understand the dataset before applying any modeling techniques

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/f2b273f2-2b4e-4606-97f0-19c600e26818">

There are 10 numeric columns and 3 string columns

**Heat Map**

A heatmap is a visual representation of data where colors represent values in a matrix. It's useful for quickly identifying patterns, correlations, and variations in large datasets.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/17dd4a7e-5675-4cc9-b8ef-1f3a95d92057">

**Scatter plot**

Scatter plots' primary uses are to observe and show relationships between two numeric variables. 
The dots in a scatter plot not only report the values of individual data points, but also patterns when the data are taken as a whole. 
Identification of correlational relationships are common with scatter plots.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/72e27552-3691-4d62-baa4-13d0f41edc2f">

**Categorical Features**

1. Artist

We have 731 artists present in the dataset

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/ed97ed94-d467-42bc-8354-7854a0359adb">










































































































