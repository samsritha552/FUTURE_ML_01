import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv(
    "datasets/Sample - Superstore.csv",
    encoding='latin1'
)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sort values
df = df.sort_values('Order Date')

# Group sales by date
sales_data = df.groupby('Order Date')['Sales'].sum().reset_index()

# Convert dates into numbers
sales_data['DateOrdinal'] = sales_data['Order Date'].map(
    pd.Timestamp.toordinal)

# Features and target
X = sales_data[['DateOrdinal']]
y = sales_data['Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Calculate error
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

# Plot actual vs predicted
plt.figure(figsize=(12, 5))

plt.plot(y_test.values, label='Actual Sales')
plt.plot(predictions, label='Predicted Sales')

plt.title("Actual vs Predicted Sales")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.legend()

# Save graph
plt.savefig("visuals/predicted_sales.png")

# Show graph
plt.show()
# Predict future 30 days

future_dates = pd.date_range(
    start=sales_data['Order Date'].max(),
    periods=30
)

future_ordinal = future_dates.map(pd.Timestamp.toordinal)

future_predictions = model.predict(
    pd.DataFrame({'DateOrdinal': future_ordinal})
)

# Future forecast graph
plt.figure(figsize=(12, 5))

plt.plot(
    future_dates,
    future_predictions
)

plt.title("Future Sales Forecast")
plt.xlabel("Future Dates")
plt.ylabel("Predicted Sales")

# Save forecast graph
plt.savefig("visuals/future_forecast.png")

plt.show()
