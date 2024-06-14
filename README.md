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

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/ab30fb65-c9dd-4f5e-ae2f-789fc11a52ed">

There are 11 numeric columns and 2 string columns

**Heat Map**

A heatmap is a visual representation of data where colors represent values in a matrix. It's useful for quickly identifying patterns, correlations, and variations in large datasets.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/94b061e5-64cf-4bc2-a88f-bd33e46e626d">



**Scatter plot**

Scatter plots' primary uses are to observe and show relationships between two numeric variables. 
The dots in a scatter plot not only report the values of individual data points, but also patterns when the data are taken as a whole. 
Identification of correlational relationships are common with scatter plots.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/28f59002-074d-4aa8-9b55-994a300a05f6">



**Bivariate Analysis**

The relation of energy and loudness is that the higher energy in music typically results in higher loudness. 
This is because energetic music often features stronger beats, faster tempos, and more intense dynamics, all contributing to its perceived loudness.


<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/5d0dad00-1b2c-4b98-ab49-f60da64ce959">

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/a777323b-3f40-42fe-b068-0bacf6e72722">



**Categorical Features**

1. Artist

We have 731 artists present in the dataset

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/ed97ed94-d467-42bc-8354-7854a0359adb">



**Measure of central Tendency**

Provides a summary statistic that represents the center point or typical value of a dataset. 
Here, we will explain the measures of central tendency—mean, median, and mode—using our dataset.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/12662a04-7785-424c-b81d-60e40612c9ec">



**Relative Frequency**

This involves grouping the variable into categories and counting the number of observations in each category. 
They are commonly represented with the help of histograms and help in determining the most common values and the range of values in the dataset. 
This gives us an overview of the spread and shape of the distribution, any extreme values can be spotted as well necessary preprocessing can be applied based on the model selected.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/cfb11bec-d29d-45a2-9793-45629d68e652">



**Box plot**

We have used box plots to get a summary of the distribution, central tendency, and variability of our numerical parameters. 
It allowed us to gauge the comparative range of each parameter, and their outliers, and detect skewness. 
Here we can see speechiness and liveness have long whiskers due to their skewed nature.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/3a1bee35-4ea9-42b1-af8a-9fcbd25183c8">


**Normalization**

From the above Box plots we can understand that our parameters have diverse ranges, this works for regression but will not help during KNN and other models. 
To ensure that we have a standard range for all our parameters we have to normalize them.

We have chosen Standard Scaler to normalize our data set.

It has a function where u is mean and s is standard deviation.

z = (x - u) / s

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/80728279-89e5-455a-afb9-93b45f258e90">

**Transformation**

We have used One-Hot encoding to handle categorical variables such as Genre, Artist and Year.
One-hot encoding transforms categorical variables into a binary format, where each category becomes a separate binary column. 
For each observation, only one column has a value of True, indicating the presence of that category, while all other columns are set to False.
True and False can also be represented in 0 and 1 and can thus be used in euclidean distance function for different models.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/aaaf4ef9-8246-4954-881b-c2225b7fff99">

**Train Test split**

The train–test split is a fundamental concept in machine learning used to evaluate the performance of a model. 
The key reasons why we use train-test split are:
1. Model Evaluation
2. Prevent Overfitting
3. Performance metrics
4. Model Selection
5. Hyperparameter Tuning
  - To perform a train – test split, we use ‘train_test_split’ function from the ‘sklearn.model_selection’ module.
  - After importing the ‘train_test_split’ from the module, we must load the data.
  - Then after, Define Features(X) and target(Y)
  - And use the ‘train_test_split’ function to split the data into training and testing sets.

**OLS Regression Results their uses?**

Ordinary Least Squares(OLS) regression is a method for estimating the unknown parameters in a linear regression model. 
It is a technique in which a straight line is used to estimate the relationship between two interval/ratio variables.

The key parameters and uses of OLS are:
- Coefficients(coef): Estimates of the regression coefficients for each predictor variable.

It indicates the relationship between each predictor variable and the response variable.
- Standard error (std err) : It shows the standard error of each coefficient.

Measures the accuracy of the coefficient estimates.

- t-statistics(t) : It is the ratio of the difference in a number’s estimated value from its assumed value to its standard error.

Used to test the null hypothesis that a given coefficient is equal to zero.

- P-value(p): It expresses the results of the hypothesis test as a significance level.

Determines the statistical significance of each coefficient.

- R-squared: It is the coefficient of determination indicating the goodness-of-fit of the regression.

A higher R-square value means a better fit.

- Adjusted R-squared: It is a slightly modified version of 𝑅2R-square, designed to penalize for the excess number of regressors that do not add to the explanatory power of the regression.

Provides a more accurate measure of goodness-of-fit when comparing models with different numbers of predictors.

- F-statistic and Prob(F-statistic): The F-statistic tests the overall significance of the model.

Determines whether at least one of the predictor variables has a non-zero coefficient.

## Model We are adopting

K Nearest Neighbours or KNN is an unsupervised learning algorithm used for regression, classification, and clustering of the data based on Euclidean distance. 
Our goal was to recommend songs that are similar to what the user already likes, and that meant finding a different approach. 
That's where K-Nearest Neighbors (KNN) comes in - it's perfect for finding close matches within our dataset. 
We chose not to use Regression or Classification models because they weren't the right fit for our recommendation system.

<img width="250" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/61a9549c-51fc-4448-88e6-3eefcc22cd85">

**How does KNN help in clustering?**

Unlabelled data: KNN is great for working with unlabeled data. It clusters data points based on their distances from each other and groups the data points nearer to each other in the same.

**Why are we using KNN?**

To recommend songs to a user, we use the K-Nearest Neighbors (KNN) algorithm, which finds similar songs based on Euclidean distance.

This approach:

- Recommends songs similar to the user's preferred choice, allows easy integration of new songs, and provides personalized recommendations.
KNN is a suitable solution for our use case, enabling us to find the closest matches and expand the user's musical horizons.
- **Non-linear relationships**: KNN can handle non-linear relationships between features and targets, making it a good choice for our datasets with complex interactions.
Our dataset has no linear relationship, a change in one variable doesn't result in a consistent straight-line change in the other variable.
- **Robust to noise**: KNN is robust to noisy data and outliers, as it focuses on the nearest neighbors rather than the entire dataset.
KNN is a model that can filter out the noise and focus on the main dataset (the nearest neighbors). It doesn't get distracted by the weird, one-off sounds (outliers) or the background noise (noisy data)
- **High-dimensional data**: KNN can handle high-dimensional data with a large number of features, this means if your dataset has a LOT of columns (features) - maybe 10, 20, 50 variables describing each data point.
Your dataset has high dimensions, making KNN suitable for datasets with many variables. This can make it hard for some algorithms to work with the data. Our dataset has 9 features making it a dataset with high dimensionality.
Store All Features: KNN stores all the features for each data point in the dataset.

**KNN steps**
1. First, we select k random centroids
2. Then we start assigning points to different centroid groups based on its distance from the centroids
3. Once all the points are exhausted, Then we calculate the variance of each cluster to calculate the total variance of the data set
4. Then we move the centroids to the center of their cluster by taking averages.
5. Then we reassign groups to these updated centroids and the cluster changes a little.
6. Then we jump back to step 3
7. We iterate steps 3-6 to reduce the variance calculated in step 3.
8. Once we see the variance is no longer reducing significantly, we have reached an elbow point and we can stop our iterations.

In Summary, KNN's ability to handle high-dimensional data means it can look at many characteristics at once, making it suitable for complex datasets with many variables

**Why We Didn't Choose Regression or Classification**

When building our recommendation system, we deliberately decided against using Regression or Classification models like Linear Regression or Decision Trees. 
Here's why:
- Labeling limitations: We didn't have labeled data to work with, and even if we did, genres are so diverse that it would be tough to categorize them effectively.
- The external song problem: These models need an external song to classify or predict a value, but we wanted to suggest songs from our own dataset.
It's like trying to find a matching puzzle piece from a different puzzle altogether!



## Model Building

We used the K-Means clustering for clustering the songs with similar features. 

There are 2 functions:

- optimize_k_clusters(data, max_clusters=10): Finds the optimal number of clusters for KMeans using the elbow method.
  It runs KMeans for various k values (1 to `max_clusters`) and returns lists of means (inertia) for each k.
- generate_elbow_plot(means, inertias): Creates a plot to visualize the elbow method (inertia vs. number of clusters).

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/84b0c173-a960-4f7b-90a5-886f9baa27b5">

The data is then fit to the KMeans model with n = 10 clusters.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/933bc02c-8d8d-47c1-b074-749b8bbda887">

The data after clustering



## To Do
- Evaluate the performance of the model
- Validation of the model
- Prediction

## References

Resources here helped us understand basic syntax for some code and also how these techniques worked, we used the titanic project as a reference to know about various steps in EDA and about various libraries out there.

Pandas documentation : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

Heat map: https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

Histogram: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/

Box plot: https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-visualization-exercise-18.php

One-hot encoding: https://www.geeksforgeeks.org/ml-one-hot-encoding/

Normalization: https://medium.com/@onersarpnalcin/standardscaler-vs-minmaxscaler-vs-robustscaler-which-one-to-use-for-your-next-ml-project-ae5b44f571b9

Different encoding techniques: https://medium.com/aiskunks/categorical-data-encoding-techniques-d6296697a40f#:~:text=It%20refers%20to%20the%20process,with%20text%20or%20categorical%20variables.

Train Test split: https://builtin.com/data-science/train-test-split

OLS Regression Results: https://www.geeksforgeeks.org/interpreting-the-results-of-linear-regression-using-ols-summary/

How KNN works: https://www.youtube.com/watch?v=mHl5P-qlnCQ&list=PLBv09BD7ez_6cgkSUAqBXENXEhCkb_2wl

Titanic Data set for reference of Basic EDA https://www.kaggle.com/c/titanic/data















































































