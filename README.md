# Music Recommendation System
**Project Overview:**

A music recommendation project that uses clustering to categorize music genres based on audio characteristics. We're using a Kaggle dataset that includes popular Spotify songs as well as audio feature information for each one.

**Goals:** To identify similarities between these audio features and categorize music genres based on those similarities. This way, we can recommend music that users are likely to listen!

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

For our dataset we have decided to drop the features **Index** and **Title** as it did not seem to
provide relevant input in creating our model and predicting the cluster in which the selected
song would appear

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

**Calculation of Skew**

Skewness is a statistical measure that tells us the degree of asymmetry of the data points
around its mean. It tells us if the majority of our data points are concentrated on one end of our
distribution mean or the other. Calculating the skewness gives us an idea of how the parameter
is distributed. We have calculated the skewness of each numeric column as shown below,

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b1edafe0-3ede-44f9-b2cf-7a4c78e968e7">

We were able to come up with a conclusion that the parameters year, energy, loudnessdB,and
Popularity are negatively skewed. Which means that more data points are concentrated on the
right side of the mean.
Whereas liveness and speechiness has a evident positive value which tells us that more data
points are concentrated on the left side of the mean.
And for the rest of the parameters which show values close to 0 we can say that the data points
are somewhat distributed symmetrically around the mean.

## Data Visualization

**Relative Frequency**

This involves grouping the variable into categories and counting the number of observations in each category. 
They are commonly represented with the help of histograms and help in determining the most common values and the range of values in the dataset. 
This gives us an overview of the spread and shape of the distribution, any extreme values can be spotted as well necessary preprocessing can be applied based on the model selected.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/8ce32113-8860-4c31-b136-cc1e40716f25">

**Heat Map**

A heatmap is a visual representation of data where colors represent values in a matrix. It's useful for quickly identifying patterns, correlations, and variations in large datasets.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/94b061e5-64cf-4bc2-a88f-bd33e46e626d">

We have plotted a heatmap for the numeric parameters. And was able to find positive
correlation of 0.74 between the parameters energy and loudness. And a correlation of 0.51
between valence and danceability. We have set a threshold of above 0.75 to deal with
correlation in our model hence we do not remove any correlated parameters.

**Scatter plot**

Scatter plots' primary uses are to observe and show relationships between two numeric variables. 
The dots in a scatter plot not only report the values of individual data points, but also patterns when the data are taken as a whole. 
Identification of correlational relationships are common with scatter plots.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/28f59002-074d-4aa8-9b55-994a300a05f6">

We have created a scatter plot for the numerical parameters using pairplot which gives us the
pairwise relationship between the parameters of our dataset. From the above we were able to
observe patterns between loudness and energy, and valence and danceability as they are
positively correlated. We have plotted them separately for further clarity

**Bivariate Analysis**

The relation of energy and loudness is that the higher energy in music typically results in higher loudness. 
This is because energetic music often features stronger beats, faster tempos, and more intense dynamics, all contributing to its perceived loudness.


<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/5d0dad00-1b2c-4b98-ab49-f60da64ce959">

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/a777323b-3f40-42fe-b068-0bacf6e72722">

There is a positive correlation between danceability and valence. This means that songs with
higher danceability scores tend to also have higher valence scores. Such songs could be
uplifting, making them suitable for dancing and conveying positive emotions simultaneously.

**Categorical Features**

1. Artist

We have 731 artists present in the dataset

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/ed97ed94-d467-42bc-8354-7854a0359adb">

We have plotted a bar graph for 20 most popular artists for better understanding of the dataset

<img width="500" alt="image" src="https://github.com/user-attachments/assets/86284e41-b5c0-480c-a4a0-12e3c2ffc524">

We have also plotted a bar graph for artists with more than 10 tracks for better understanding of the dataset.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/c7d6aaa2-70c4-443d-a28e-600ba25e43bc">


**Measure of central Tendency**

Provides a summary statistic that represents the center point or typical value of a dataset. 
Here, we will explain the measures of central tendency—mean, median, and mode—using our dataset.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/12662a04-7785-424c-b81d-60e40612c9ec">

**Box Plot**

We have used box plots to get a summary of the distribution, central tendency, and variability of our
numerical parameters. It allowed us to gauge the comparative range of each parameter, and their
outliers, and detect skewness. Here we can see speechiness and liveness have long whiskers due to
their skewed nature.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/37533aee-8bf0-4d59-98cc-21b6aaa9d411">

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


## Model We are adopting

We chose K-means clustering because it is simple, efficient, and versatile. It is easy to set up and
computationally efficient, making it ideal for grouping large datasets. The algorithm iteratively
allocates data points to the closest cluster centroid and updates centroids depending on the mean of
the given points.

Our goal was to recommend songs similar to what the user already likes, which meant finding a
different approach. That's where K Means comes in - it's perfect for finding close matches within our
dataset. We chose not to use Regression or Classification models because they weren't the right fit
for our recommendation system.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/922daf9e-1277-4863-89d5-1bdc861fe06e">


**How does K Means help in clustering?**

K Means is one of the most popular Unsupervised Machine Learning Algorithms used for solving
classification problems in data science, it segregates unlabeled data into various groups, known as
clusters, by identifying similar features and common patterns within the dataset.

**Why We Didn't Choose Regression or Classification**

When building our recommendation system, we deliberately decided against using Regression or
Classification models like Linear Regression or Decision Trees. Here's why:

- Labelling limitations: We didn't have labelled data to work with, and even if we did, genres
are so diverse that it would be tough to categorize them effectively.
- The external song problem: These models need an external song to classify or predict a
value, but we wanted to suggest songs from our dataset. It's like trying to find a matching
puzzle piece from a different puzzle altogether!

## Model Building

We used the K-Means clustering for clustering the songs with similar features.

There are 2 functions:

- optimize_k_clusters(data, max_clusters=10): Finds the optimal number of clusters for
KMeans using the elbow method. It runs KMeans for various k values (1 to max_clusters)
and returns lists of means (inertia) for each k.
- generate_elbow_plot(means, inertias): Creates a plot to visualize the elbow method (inertia
vs. number of clusters).

<img width="500" alt="image" src="https://github.com/user-attachments/assets/2153a30d-52e3-4003-8601-cf1ce6c735f9">

The data is then fit to the KMeans model with n = 10 clusters.

<img width="500" alt="image" src="https://github.com/Aparnajr2000/Music_recommendation_system/assets/84074591/da123dbd-68d3-4af5-906a-06fb52aefae4">

The data after clustering

## Dashboarding

We have used streamlit for creating the application of music recommendation system.

What is streamlit?

Streamlit is a popular framework for building data-centric web applications in Python.

Why streamlit?

1) Simplicity: Streamlit is designed to be intuitive and easy to use.
2) Fast prototyping: It allows for rapid prototyping of data applications.
3) Focus on data: Streamlit is optimized for data science and machine learning workflows.
4) Reactivity: Streamlit apps are reactive, meaning they automatically update when inputs
are changed.
5) Documentation and Support: Streamlit offers comprehensive documentation and tutorials,
making it easy to get started and troubleshoot issues.

Create a new environment in anaconda navigation named ‘streamlitenv’.

Then install streamlit on your device

<img width="500" alt="image" src="https://github.com/user-attachments/assets/fd5a07c0-32d1-448e-a4c3-15d63bd21347">

.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/3ba6fcf4-b537-4a55-b601-2a5c5073e168">

Libraries Imported:
- streamlit as st: Streamlit for creating the web app.
- pandas as pd: Pandas for data manipulation and reading CSV files.
- NearestNeighbors from sklearn.neighbors: For implementing the k-Nearest Neighbors algorithm.

This Python script creates a music recommendation system using Streamlit and the k-Nearest
Neighbors algorithm. It reads song data from a CSV file, and based on user-selected song features,
recommends similar songs. The script includes:

Loading Data: The load_data function reads the CSV file containing song data and caches it for
efficiency.

Recommendation Model: The recommend_songs function takes a song name and the number of
recommendations as inputs. It finds the nearest neighbors based on the features provided (assumed
to be 'Feature1' and 'Feature2') and returns a list of recommended songs.

Streamlit Interface: The Streamlit app interface includes a title and a select box for users to choose
a song. Upon clicking the 'Recommend' button, it displays the recommended songs based on the
user's selection

**User Interface of Application**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/cca7a6e2-f675-4f49-98c5-d00fd1e3a2f9">
Shows the app interface with a song selected and the 'Recommend' button


<img width="500" alt="image" src="https://github.com/user-attachments/assets/acc232ae-ef7f-40b5-88bc-91389d90ccab">
Shows the app interface where model has recommended songs related to the Genre of selected song



**Streamlit Interface:**
- The application uses Streamlit to create a user-friendly interface.
- Users can select a song from a dropdown menu and click the 'Recommend' button to get
recommendations.
- The recommended songs are displayed below the button.
Functionality
- User Input: The user selects a song they like from the dropdown menu.
- Recommendation: When the user clicks the 'Recommend' button, the application finds and
displays similar songs based on the selected song

**Visualization**
- First Image: Shows the app interface with a song selected and the 'Recommend' button.
- Second Image: Shows the app interface where model has recommended songs related to
the Genre of selected song.

**Running the App**
To run this Streamlit app, use the command:

<img width="250" alt="image" src="https://github.com/user-attachments/assets/101ee177-fef4-4902-a0a2-2c3641a37c54">

This will start a local server, and we can interact with the application in the web browser.

**Code Review/Versioning and Modular Structure**

A project repository(private) was created in Github to ensure version control.
- Each section of the code is split properly with proper headings.
- The code is documented with comments wherever necessary.
- The code was versioned automatically as the coding was done in Google Colaboratory.
- To allow members to contribute code, monitor changes, and take part in conversations, all
team members were added as collaborators.
- The code works in the exact flow that was needed, proper EDA to the model building.
- The evaluation of the model is yet to be done.
- The code was committed to the GitHub repository to ensure proper versioning.
- Analysis of the code was done by multiple members to ensure that the code follows the
proper conventions and has an understandable structure.
- The model must be improved to accommodate live data.
- The code is well structured and easy to understand.
- Code was reviewed periodically to ensure the quality.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/98afd8fd-b53b-4551-a94d-c341a7a37d60">


## References

Resources here helped us understand basic syntax for some code and also how these techniques
worked, we used the titanic project as a reference to know about various steps in EDA and about
various libraries out there.

Pandas documentation :

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

Heat map:

https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

Histogram: 

https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/

Box plot:

https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-visualization-exercise-18.php

One-hot encoding: 

https://www.geeksforgeeks.org/ml-one-hot-encoding/

Normalization:

https://medium.com/@onersarpnalcin/standardscaler-vs-minmaxscaler-vs-robustscaler-which-one-to-use-for-your-next-ml-project-ae5b44f571b9

Different encoding techniques:

https://medium.com/aiskunks/categorical-data-encoding-techniques-d6296697a40f#:~:text=It%20refers%20to%20the%20process,with%20text%20or%20categorical%20variables.

Titanic Data set for reference of Basic EDA: 

https://www.kaggle.com/c/titanic/data













































































