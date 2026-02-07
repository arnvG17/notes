# Gradient Descent

Gradient descent is an optimization algorithm used to minimize the cost function.

## 🔄 Gradient Descent Iteration

```mermaid
graph TD
    A["Initialize Weights"] --> B["Calculate Prediction"]
    B --> C["Compute Loss"]
    C --> D["Calculate Gradient"]
    D --> E["Update Weights: W = W - α*Grad"]
    E --> F{"Converged?"}
    F -- "No" --> B
    F -- "Yes" --> G["Optimized Model"]
```

---

[⬅️ Back to Regression Overview](README.md) | [⬅️ Back to Home](../README.md)
