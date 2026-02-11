import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# Load dataset
try:
    df = pd.read_csv("california.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: california.csv not found.")
    exit()

# EDA
print("\n--- EDA ---")
print(df.info())
print("\nMissing values before imputation:")
print(df.isnull().sum())

# Correlation Matrix
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
# plt.show() # Uncomment to show plot

# Preprocessing
print("\n--- Preprocessing ---")
# Impute missing values with median
median_bedrooms = df['total_bedrooms'].median()
df['total_bedrooms'] = df['total_bedrooms'].fillna(median_bedrooms)
print(f"Imputed 'total_bedrooms' with median: {median_bedrooms}")
print("\nMissing values after imputation:")
print(df.isnull().sum())

# Label Encoding for ocean_proximity
le = LabelEncoder()
df['ocean_proximity'] = le.fit_transform(df['ocean_proximity'])
print("Encoded 'ocean_proximity' using LabelEncoder.")

# Split data
X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Data split into Train ({X_train.shape[0]}) and Test ({X_test.shape[0]}) sets.")

# Modeling
print("\n--- Modeling ---")
train_scores = []
test_scores = []
depths = range(1, 21)

best_score = -float('inf')
best_depth = 0

for depth in depths:
    model = DecisionTreeRegressor(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    
    y_train_pred = model.predict(X_train)
    train_r2 = r2_score(y_train, y_train_pred)
    train_scores.append(train_r2)
    
    y_test_pred = model.predict(X_test)
    test_r2 = r2_score(y_test, y_test_pred)
    test_scores.append(test_r2)
    
    if test_r2 > best_score:
        best_score = test_r2
        best_depth = depth


# Plotting results for Max Depth (Demonstrating Overfitting)
plt.figure(figsize=(10, 6))
plt.plot(depths, train_scores, marker='o', label='Train R2 Score', color='blue')
plt.plot(depths, test_scores, marker='o', label='Test R2 Score', color='red')
plt.xlabel('Max Depth')
plt.ylabel('R2 Score')
plt.title('Overfitting Demonstration: Train vs Test R2 Score by Max Depth')
plt.legend()
plt.grid(True)
plt.savefig('overfitting_plot.png')
print("Overfitting plot saved as 'overfitting_plot.png'")

print(f"\nBest Max Depth from simple tuning: {best_depth}")
print(f"Best Test R2 Score from simple tuning: {best_score}")

# --- Pruning (Cost Complexity Pruning) ---
print("\n--- Pruning ---")
# Using the fully grown tree (max_depth=None or large) to find pruning path
clf = DecisionTreeRegressor(random_state=42)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

print(f"Found {len(ccp_alphas)} impurities / ccp_alphas.")

# Train models for each alpha (filtering out very small alphas to save time/memory if too many)
# For demonstration, we'll take a subset if there are too many, or just run all
# Since this is a regression tree on continuous data, allow some time.
clfs = []
# Using a subset of alphas to speed up if needed, or all if reasonable size
selected_alphas = ccp_alphas[::max(1, len(ccp_alphas)//20)] # Sample 20 alphas

print(f"Training models for {len(selected_alphas)} selected alphas...")

train_scores_prune = []
test_scores_prune = []

for ccp_alpha in selected_alphas:
    clf = DecisionTreeRegressor(random_state=42, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    
    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)
    
    train_scores_prune.append(r2_score(y_train, y_train_pred))
    test_scores_prune.append(r2_score(y_test, y_test_pred))

# Plotting Pruning Results
plt.figure(figsize=(10, 6))
plt.plot(selected_alphas, train_scores_prune, marker='o', label='Train R2', drawstyle="steps-post")
plt.plot(selected_alphas, test_scores_prune, marker='o', label='Test R2', drawstyle="steps-post")
plt.xlabel("effective alpha")
plt.ylabel("R2 score")
plt.title("R2 Score vs alpha for training and testing sets")
plt.legend()
plt.grid(True)
plt.savefig('pruning_plot.png')
print("Pruning plot saved as 'pruning_plot.png'")

# Best alpha
best_alpha_idx = np.argmax(test_scores_prune)
best_alpha = selected_alphas[best_alpha_idx]
print(f"Best ccp_alpha: {best_alpha}")
print(f"Best Test R2 Score after pruning: {test_scores_prune[best_alpha_idx]}")

# Final Model Evaluation with Best Alpha
final_model_pruned = DecisionTreeRegressor(ccp_alpha=best_alpha, random_state=42)
final_model_pruned.fit(X_train, y_train)
y_pred_pruned = final_model_pruned.predict(X_test)
rmse_pruned = np.sqrt(mean_squared_error(y_test, y_pred_pruned))

print(f"Final Pruned Test RMSE: {rmse_pruned}")
