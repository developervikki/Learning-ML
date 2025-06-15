import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, classification_report, confusion_matrix

# Load Telco Customer Churn Dataset
df_telco = pd.read_csv('data.csv')

# Display dataset info and basic statistics
print(df_telco.info())
print(df_telco.describe())

# Handle missing values: 
# - Numeric columns -> Fill with mean
# - Categorical columns -> Fill with mode
for column in df_telco.columns:
    if df_telco[column].dtype == 'object':  # Categorical column
        df_telco[column].fillna(df_telco[column].mode()[0], inplace=True)
    else:  # Numeric column
        df_telco[column].fillna(df_telco[column].mean(), inplace=True)

# Encode categorical variables using Label Encoding
le = LabelEncoder()
for column in df_telco.select_dtypes(include=['object']).columns:
    df_telco[column] = le.fit_transform(df_telco[column])

# Define features (X) and target (y)
X = df_telco.drop(columns=['Churn'])  # Assuming 'Churn' is the target column
y = df_telco['Churn']

# Scale features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualize churn distribution
sns.countplot(x="Churn", data=df_telco)
plt.title("Churn Distribution")
plt.show()

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Make predictions
y_pred_lr = linear_model.predict(X_test)

# Evaluate Linear Regression Model
mse = mean_squared_error(y_test, y_pred_lr)
print("Linear Regression MSE:", mse)

# Train Logistic Regression Model
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)

# Make predictions
y_pred_logistic = logistic_model.predict(X_test)

# Evaluate Logistic Regression Model
print("\nLogistic Regression Model Evaluation:")
print(classification_report(y_test, y_pred_logistic))
print(confusion_matrix(y_test, y_pred_logistic))

# Train K-Nearest Neighbors (KNN) Classifier
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Make predictions
y_pred_knn = knn_model.predict(X_test)

# Evaluate KNN Model
print("\nKNN Model Evaluation:")
print(classification_report(y_test, y_pred_knn))
print(confusion_matrix(y_test, y_pred_knn))
