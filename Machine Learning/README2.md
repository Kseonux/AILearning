# 🧬 Breast Cancer Diagnosis with PCA and K-Nearest Neighbors

This project was created for the **Machine Learning** course during my **Master’s degree (S2)** in Information Technology.  
**Submission Date**: March 24, 2025

## 🧠 Overview
The project involves diagnosing breast cancer (Benign or Malignant) using **feature reduction with Principal Component Analysis (PCA)** and classification using **K-Nearest Neighbors (KNN)**.

## 📚 Dataset
- Source: UCI Breast Cancer Wisconsin Diagnostic Dataset
- Samples: 569
- Features: 30 numerical measurements (e.g., radius, texture, perimeter, area)
- Target: `0 = Benign`, `1 = Malignant`

## ⚙️ Methodology
1. **Preprocessing**: Standardization & normalization of features
2. **Feature Selection**: Applied PCA to reduce dimensionality
3. **Modeling**: Used KNN classifier on transformed features
4. **Evaluation**:
   - Accuracy on test data: ~95.6%
   - Cross-validation accuracy: ~96.13%
   - Visualizations: Explained Variance, Confusion Matrix

## 🛠 Tools & Libraries
- RapidMiner Studio
- Python 3
- Libraries:
  - `pandas`, `numpy`, `scikit-learn`
  - `matplotlib`, `seaborn`

## 📊 Results Summary
| Evaluation Type     | Accuracy |
|---------------------|----------|
| Train-Test Split    | 95.61%   |
| Cross-Validation    | 96.13%   |

- PCA successfully reduced feature count while preserving performance
- KNN effectively classified malignant vs benign cases with high accuracy

## 📷 Visualizations
- PCA Scree Plot / Variance Ratio
- Confusion Matrix
- Classification Report

## 🔗 Project Files
[GitHub Repository](https://github.com/ravenkong28/breast-cancer-pca-knn)
