# MiniProject_group15
group 15, Liya, Fatima, Ömer, Rebecca, Nadia

Data with the CVR API explained:
I have built a small Python program that makes it easy to find company data from the Danish CVR register. First, I use the requests library to fetch data from the API. I save the data in a JSON file, so it can be reuased later. Then, I use Pandaas to create a DataFrame and select the relevant fields, such as name, address, number of employees, and so on. I also save the data as a CSV file, making it easy to work with afterwards. Finally, I create a simple visualization of the number of employees using Matplotlib, and the entire project is wrapped in a user-friendly Streamlit app.
Use this command in the terminal to view it in the browser: streamlit run streamlit_app.py
If you havent installed streamlit write this in the terminal: pip install streamlit

# Miniproject 2:
9,11,12,13,14 done. 
Sources used to solve the tasks:
PDF: Exploratory Data Analysis - EDA.pdf (very helpful!)
→ Used to understand how to prepare and explore the data in tasks 9 and 11.

PDF: PCA Explained.pdf
→ Used for tasks 13 and 14 to understand how PCA works and how to reduce the number of columns.

Notebook: Explore_data.ipynb
→ Used to understand how to use .describe(), .corr() and how to make scatter plots.

Website: Pandas toolbox – dat3cph.github.io
→ Used to learn how functions like .drop(), .sample() and .select_dtypes() works in tasks 12 and 13.

Website: Data visualization toolbox – dat3cph.github.io
→ Helped with making 2D scatter plots in matplotlib and how to color the points by wine quality in task 14.

# Miniproject 3:
```diff
! Potential Problem on Task 3: Classification
- The Random Forest model performs reasonably well but there’s an important issue in the cleaning of data that can hurt the model's quality, especially on categorical features like JobRole, Department, MaritalStatus, etc.
- Using LabelEncoder on nominal categories is risky and can introduce bias in how splits are made in the tree, since the Random Forest might treat the values as ordered, but they are not supposed to be ordered.
```

### Which machine learning methods did you choose to apply in the application and why?
#### For the classification task of predicting employee attrition
- Random Forest is an ensemble learning method that builds multiple decision trees and combines their results for more accurate and stable predictions. The reason for selecting this method is:
  - It is robust to overfitting, especially when compared to individual decision trees.
  - It automatically captures non-linear relationships and feature interactions - such as how 'YearsAtCompany ' and 'JobSatisfaction' could affect attrition together.
  - It provides feature importance scores, which are helpful for interpretability in an HR context.

#### For the clustering task of segmenting employees into meaningful groups
- We used KMeans Clustering, an unsupervised learning algortihm that groups data points based on similarity across selected features.
- The goal was to identify natural segments in th eworkforce based on factors such as income, age, job satisfaction, and years at the company.
- KMeans was chosen because:
 -  it's a simple, yet powerful algorithm that works
 well for identifying patterns in datasets.
 - Allowed us to divide employees into distinct groups without needing labeled outcomes.
 - We could use the silhuette score to evaluate and choose the most optimal number of clusters. Which in our case was K = 2, based on our silhouette score of 0.2001.
 

### How accurate is your solution of prediction? Explain the meaning of the quality measures.
#### For the classification task of predicting employee attrition
- The model achieved an overall accuracy of 85.9% on the test set but it seems imbalanced
  - I evaluated the model using a Confusion matrix to help us understand how well the classifier did based on number of cases of correct or wrong prediction
    - The model correctly predicted 125 out of 128 employees who stayed.
    - It correctly predicted 9 out of 28 employees who left.
    - When the model predicts that an employee will leave, it is correct 75% of the time.
    - The model only detects 32% of the employees who actually leave.
    - The F1-score (Attrition = Yes) being 0.45 is a relatively low score indicating the model is not catching enough of the true "leavers."
    - The Macro Average F1-score being 0.68 gives equal weight to both classes and highlights and tells us that the model struggles more with predicting attrition than retention.


### Which are the most decisive factors for quitting a job? Why do people quit their job?
#### For the classification task of predicting employee attrition
- The Random Forest model suggests that employees' income, age, commute distance, and tenure are the primary factors influencing attrition. Job satisfaction, overtime, and the work environment also play key roles, but not as much as the other features. Some of the primary reasons could be:
  - Employees with lower salaries might be more inclined to leave for better opportunities. High compensation can be a strong retention factor.
  - Younger employees or those with less experience might be more likely to leave in search of better growth opportunities. On the other hand, older or more experienced employees might expect career stability.
  - Employees who live farther away from the office may be more prone to attrition due to long commutes. This can lead to higher burnout or dissatisfaction, especially in jobs that are physically demanding.
  - Employees who have worked at the company for a longer time or who have been with the same manager for several years may experience stagnation or a lack of new challenges, which could influence their decision to leave.

#### For the clustering task of segmenting employees into meaningful groups
- We got revealed two clear employee segments:
 - Cluster 1: employees with shorter tenure, lower income and lower job levels.
 - Cluster 2: more experienced employees with higher salaries and longer time at the company.
- The observations from our clustering results revealed that employees in Cluster 1 may be at a higher risk of leaving due to limited compensation and career development.
- Supporting this departments like Sales and HR had a larger share of Cluster 1 employees, pointing to possible retention challenges.

### What could be done for further improvement of the accuracy of the models?
#### For the classification task of predicting employee attrition
- To improve the Random Forest model, especially its ability to correctly identify employees likely to leave we could:
  - Potentially handle class imbalance by appling class weighting (fx. RandomForestClassifier(class_weight='balanced')) to penalize mistakes on the minority class
  - Combine features or create new ones, such as YearsInCurrentRole / TotalWorkingYears to represent role stability
  - Or simply try alternative models/use other classifiers to compare accuracy

#### For the clustering task of segmenting employees into meaningful groups
- Trying other clustering algorithms like DBSCAN or hierarchical clustering, which may capture more complex patterns. 
- Improving feature selection, such as removing weakly correlated variables or testing new derived features.
- Performing PCA (Principal Component Analysis) before clustering to reduce noise and highlight meaningful structure in the data.

### Which work positions and departments are in higher risk of losing employees?
#### For the clustering task of segmenting employees into meaningful groups
By analyzing the cluster distribution across departments, we found that:
- Sales, Human Resources, and Research & Development had a higher number of employees in Cluster 1 — the segment associated with lower tenure, lower salary, and earlier career stage.
- For example, over 68% of HR employees were in Cluster 1.
This suggests that these departments may face higher retention risks, and could benefit from targeted career development or engagement strategies.

### Are employees of different gender paid equally in all departments?
#### For the clustering task of segmenting employees into meaningful groups
A grouped analysis of average monthly income by gender and department showed no major pay inequality across the dataset.
- Minor differences were visible in some departments:
 - In Human Resources, for instance, female employees had slightly higher average income than male employees.

Overall, the data does not indicate a consistent gender pay gap, but further investigation (e.g. into job roles or seniority) would be needed for a deeper audit.

### Do the family status and the distance from work influence the work-life balance?
#### For the clustering task of segmenting employees into meaningful groups
From the clustering and statistical analysis:
- The average work-life balance rating was nearly identical across clusters (≈ 2.76).
- The correlation between DistanceFromHome and WorkLifeBalance was -0.026, which is nearly zero — meaning no meaningful relationship exists between how far someone lives and how they rate their work-life balance.
Marital status was not found to significantly differ across clusters or strongly influence work-life balance either.

### Does education make people happy (satisfied from the work)?
#### For the clustering task of segmenting employees into meaningful groups
An analysis of average job satisfaction by education level revealed:
- There is no clear trend that more education = more job satisfaction.
- Surprisingly, employees with lower education levels (e.g. “Below College”) had slightly higher satisfaction than those with advanced degrees.
This suggests that education alone is not a strong predictor of job satisfaction, and that other factors like job role or expectations might have more impact.

### Which were the challenges in the project development?


