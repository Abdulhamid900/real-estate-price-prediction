# Real-Estate-Price-Prediction


**Real Estate Price Prediction:** Is project to scrap 'immoweb.be' site to Obtain a data set consisting of information for thousands of properties in Belgium and use it to predict property prices using machine learning.

**First Step:**

 **'Data Acquisition'**
 Is use selenium to scrap 'immoweb.be' site and have my dataset as CSV file that contain information for thousands of properties in Belgium.

**Second Step:**

**'Data Analysis'**
Is use pandas library to clean the dataset from empty values ​​and incomplete information and then use matplotlib library to  make a visualization of data and design clear charts to present data information.

**Third Step:**

**'Model Training'**
 After I present data about the Belgian Real Estate market, I create a Machine Learning model by use "RandomForestRegression" to predict prices on Belgium's real estate sales.

**Fourth Step:**

**'Deployment'**
Is to save trained model with joblib library and load the model and test it , then prepare it to deploy create local api with use Flask and test locally.