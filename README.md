# LifeGuard Diagnostics

**LifeGuard Diagnostics** is a disease prediction application that helps users determine whether they may have certain conditions. The app currently supports predictions for:
- **Diabetes**
- **Heart Disease**
- **Parkinson's Disease**

Users can navigate through the app, enter the required medical data, and receive predictions based on machine learning models.

## Features
- **Accurate Disease Prediction:** The app utilizes machine learning models such as Support Vector Machine (SVM) and Logistic Regression, ensuring an accuracy of at least 80%.
- **Multiple Disease Predictions:** Users can choose from three types of diseases to test.
- **User-Friendly Interface:** Simple navigation allows users to input their information and receive predictions with ease.

## Datasets
The datasets used to train the models have been sourced from Kaggle and cover a wide range of medical parameters for each of the supported diseases.

## Technologies Used
- **Languages:** Python
- **Libraries:** Scikit-learn, NumPy, Pandas
- **Models:** SVM, Logistic Regression
- **Dataset Source:** [Kaggle](https://www.kaggle.com)

## How to Install and Run the Project

### Step 1: Clone the Repository
To run this project locally, clone the repository:

```bash
git clone https://github.com/AyushiiiAwasthi/LifeGuard-Diagnostics.git
```
### Step 2: Navigate to the Project Directory
```bash
cd LifeGuard-Diagnostics
```
### Step 3:Run the Application
After installing all dependencies, you can run the application:
```bash
streamlit run app.py
```
