# Association Rules

Association rule learning is used for finding interesting relations between variables in large databases (e.g., Market Basket Analysis).

## 🛒 Association Rule Mining

```mermaid
graph LR
    A["Transaction Data"] --> B["Calculate Support"]
    B --> C["Calc Confidence & Lift"]
    C --> D{"Prune Rules"}
    D -- "Pass Threshold" --> E["Actionable Insights"]
```

---

[⬅️ Back to Home](README.md)
