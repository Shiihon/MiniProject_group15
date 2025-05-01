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


