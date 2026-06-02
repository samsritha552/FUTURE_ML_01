# Sales Forecasting Project 

## Overview

This project predicts future sales using Machine Learning based on historical sales data from a retail superstore dataset.

The goal is to help businesses analyze sales trends and make informed decisions regarding inventory management, revenue planning, and future demand forecasting.



## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn



## Features

* Data Cleaning and Preprocessing
* Time-Series Data Analysis
* Sales Trend Visualization
* Machine Learning Forecasting using Linear Regression
* Actual vs Predicted Sales Comparison
* Future Sales Forecasting
* Automated Graph Generation



## Dataset

Superstore Sales Dataset

The dataset contains:

* Order Dates
* Product Information
* Sales Values
* Profit Data
* Customer and Regional Information



## Project Workflow

1. Load the sales dataset
2. Clean and preprocess the data
3. Convert order dates into time-series format
4. Aggregate daily sales
5. Visualize sales trends
6. Train a Linear Regression model
7. Evaluate model performance using MAE
8. Forecast future sales
9. Generate forecast visualizations



## Generated Visualizations

The project creates:

* sales_trend.png
* predicted_sales.png
* future_forecast.png

These files are saved in the 'visuals' folder.



## Model Evaluation

Metric Used:

* Mean Absolute Error (MAE)

Example Result:

* MAE ≈ 1794.17



## Business Benefits

This forecasting system helps businesses:

* Forecast future demand
* Optimize inventory levels
* Reduce stock shortages
* Improve revenue planning
* Support data-driven decision making



## How to Run

Install required libraries:
pip install -r requirements.txt


Run the project:
python sales_forecast.py



## Project Structure

sales-forecasting-project
│
├── datasets
│   └── Sample - Superstore.csv
│
├── visuals
│   ├── sales_trend.png
│   ├── predicted_sales.png
│   └── future_forecast.png
│
├── sales_forecast.py
├── requirements.txt
└── README.md


 
## Author

Created as part of a Machine Learning Sales Forecasting Internship Project.
