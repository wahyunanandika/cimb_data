# CIMB Data - Loan Default Prediction

## Business Problem
The objective of this project is to build a **Probability of Default (PD) model** for predicting loan defaults in a portfolio of individual loans. The model helps to assess the likelihood that a borrower will default on their loan, which is critical for managing the risk in a lending institution.

The dataset contains various features about loan applications, including information like **loan grade**, **purpose**, **income**, and **employment length**. The challenge is to predict whether a loan will default or not, with **0** indicating a default and **1** indicating a non-default.

## Key Features
- **Loan_ID**: Unique identifier for each loan.
- **Grade**: The grade of the loan (A, B, C, etc.).
- **Home_Ownership**: The borrower's home ownership status (Rent, Own, Mortgage).
- **Purpose**: The category of the loan.
- **Verification_Status**: Whether the income was verified or not.
- **Term**: The term period of the loan (in months).
- **Emp_Length_Int**: The length of the borrower's employment (in years).
- **Int_Rate**: The interest rate of the loan.
- **Annual_Inc**: The annual income of the borrower.
- **Dti**: The debt-to-income ratio.
- **Good_Bad**: The target variable, indicating loan default (0 = default, 1 = non-default).

## Results
After implementing several machine learning models, the **Random Forest** model emerged as the best performing model with a **Macro F1 score** of 0.61, achieving an excellent balance between **precision** and **recall** for both classes (default and non-default).

### Model Evaluation Metrics
- **Precision**:
  - Class 0 (Default): 0.31
  - Class 1 (Non-default): 0.89
  - **Macro Avg**: 0.60
  - **Weighted Avg**: 0.81

- **Recall**:
  - Class 0 (Default): 0.39
  - Class 1 (Non-default): 0.86
  - **Macro Avg**: 0.62
  - **Weighted Avg**: 0.79

- **F1-Score**:
  - Class 0 (Default): 0.34
  - Class 1 (Non-default): 0.87
  - **Macro Avg**: 0.61
  - **Weighted Avg**: 0.80

## Approach
1. **Feature Engineering**: Several features like **interest rate**, **debt-to-income ratio**, and **annual income** were found to be important in predicting loan defaults.
2. **Model Selection**: 
   - Logistic Regression, Random Forest, and XGBoost were tried.
   - Random Forest emerged as the best model with the best performance on both precision and recall for classifying non-default loans.
3. **Evaluation Metrics**: F1 Score (Macro) was chosen as the primary evaluation metric to ensure a balanced evaluation between the default and non-default classes, especially in the context of class imbalance.

## Workflow and Notebook
The primary notebook used for model development is **Wahyunan-andika.ipynb**, which contains all the key steps for:
- Data preparation and exploration (EDA)
- Model development (training and tuning)
- Model evaluation

The other notebooks were used for trial and error during the feature selection process, addressing class imbalance through techniques like **Random OverSampling (ROS)** and transforming features with **log1p** to improve model performance.

## Deployment
The model has been successfully deployed on **Streamlit**. You can interact with the model and predict loan defaults at the following link:
[Loan Default Prediction App](https://cimb-wahyunan-andika.streamlit.app/)

## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/wahyunanandika/cimb_data.git
