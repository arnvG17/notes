# 📘 Machine Learning – Structured Notes

---

## 📚 Syllabus Overview

1. **Introduction**
2. **Regression**
   - Linear Regression
   - Logistic Regression
3. **Decision Tree**
4. **Ensemble Learning**
5. **Bayesian Learning**
6. **Support Vector Machine (SVM)**
7. **Association Rules**
8. **Clustering**

---

## 1️⃣ Introduction

<details>
<summary><strong>Click to expand</strong></summary>

- What is Machine Learning?
- Types of ML
- Applications
- ML pipeline

</details>

---

## 2️⃣ Regression

### 2.1 Linear Regression ✅

<details open>
# 🧠 Machine Learning – Regression (Conceptual Flow)

---

## 🔁 Overall Regression Workflow

- Raw Data
- Choose Regression Type
- Define Model (Hypothesis Function)
- Choose Loss Function
- Choose Optimizer
- Train Model
- Evaluate Performance
- Handle Overfitting (if needed)

---

## 🧩 Core Components of a Regression Model

- Model (Equation / Hypothesis)
- Loss Function
- Optimizer
- Regularization
- Evaluation Metric

---

## 📌 1. Types of Regression Models

- **Linear Regression**
  - Simple Linear Regression
  - Multiple Linear Regression

- **Polynomial Regression**

- **Regularized Regression**
  - Ridge Regression (L2)
  - Lasso Regression (L1)

- **Logistic Regression**
  - (Used for classification)

---

## 📌 2. Hypothesis (Model) Functions

### Linear Regression
\[
\hat{y} = a_0 + a_1 x
\]

### Multiple Linear Regression
\[
\hat{y} = a_0 + a_1 x_1 + a_2 x_2 + \dots + a_n x_n
\]

### Logistic Regression
\[
\hat{y} = \frac{1}{1 + e^{-z}}
\quad \text{where } z = a_0 + a_1 x
\]

---

## 📌 3. Loss Functions

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Log Loss (for Logistic Regression)

### Mean Squared Error (MSE)
\[
MSE = \frac{1}{n} \sum (y - \hat{y})^2
\]

**Intuition:**  
Measures average squared distance between predicted and actual values.

---

## 📌 4. Optimization Algorithms

- Batch Gradient Descent
- Stochastic Gradient Descent
- Mini-Batch Gradient Descent

### Gradient Descent Update Rule
\[
\theta = \theta - \alpha \nabla J(\theta)
\]

---

## 📌 5. Regularization Techniques

- Ridge Regression (L2 Regularization)
- Lasso Regression (L1 Regularization)

### Ridge (L2)
\[
Loss = MSE + \lambda \sum \theta^2
\]

### Lasso (L1)
\[
Loss = MSE + \lambda \sum |\theta|
\]

---

## 📌 6. Evaluation Metrics

- Mean Squared Error (MSE)
- R² Score
- Accuracy (for classification)

---

## 🧠 One-Look Mental Model

- Model → makes predictions
- Loss → measures error
- Gradient → gives direction
- Optimizer → updates model
- Regularization → controls complexity


</details>

---

### 2.2 Logistic Regression

<details>
<summary><strong>Click to expand</strong></summary>

- Classification problem  
- Uses sigmoid function  
- Outputs probability  

</details>

---

## 3️⃣ Decision Tree

<details>
<summary><strong>Click to expand</strong></summary>

- Tree-based model  
- Gini / Entropy  
- Recursive splits  

</details>

---

## 4️⃣ Ensemble Learning

<details>
<summary><strong>Click to expand</strong></summary>

- Bagging  
- Boosting  
- Random Forest  

</details>

---

## 5️⃣ Bayesian Learning

<details>
<summary><strong>Click to expand</strong></summary>

- Bayes Theorem  
- Naive Bayes  

</details>

---

## 6️⃣ Support Vector Machine (SVM)

<details>
<summary><strong>Click to expand</strong></summary>

- Max-margin classifier  
- Kernel trick  

</details>

---

## 7️⃣ Association Rules

<details>
<summary><strong>Click to expand</strong></summary>

- Support  
- Confidence  
- Lift  

</details>

---

## 8️⃣ Clustering

<details>
<summary><strong>Click to expand</strong></summary>

- K-Means  
- Hierarchical  
- DBSCAN  

</details>
