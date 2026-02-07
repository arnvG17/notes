# Regularization

Regularization techniques like Ridge (L2) and Lasso (L1) are used to prevent overfitting by adding a penalty term to the cost function.

## ⚖️ Regularization: Bias-Variance Tradeoff

```mermaid
graph TD
    A["Model Complexity"] --> B{"Regularization (λ)"}
    B -- "High λ" --> C["Strong Penalty"]
    C --> D["Simpler Model (High Bias)"]
    B -- "Low λ" --> E["Weak Penalty"]
    E --> F["Complex Model (High Variance)"]
```

---

[⬅️ Back to Regression Overview](README.md) | [⬅️ Back to Home](../README.md)
