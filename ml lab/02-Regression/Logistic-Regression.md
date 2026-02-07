# Logistic Regression

Logistic regression is used for classification problems where the output is categorical.

## 📉 Logistic Regression Process

```mermaid
graph TD
    A["Linear Combination: Z = WX + b"] --> B["Sigmoid Function"]
    B --> C["Probability (0 to 1)"]
    C --> D{"Threshold (0.5)"}
    D -- "> 0.5" --> E["Class 1"]
    D -- "< 0.5" --> F["Class 0"]
```

---

[⬅️ Back to Regression Overview](README.md) | [⬅️ Back to Home](../README.md)
