# MiniProject_group15
group 15, Liya, Fatima, Ömer, Rebecca, Nadia

Data with the CVR API explained:
I have built a small Python program that makes it easy to find company data from the Danish CVR register. First, I use the requests library to fetch data from the API. I save the data in a JSON file, so it can be reuased later. Then, I use Pandaas to create a DataFrame and select the relevant fields, such as name, address, number of employees, and so on. I also save the data as a CSV file, making it easy to work with afterwards. Finally, I create a simple visualization of the number of employees using Matplotlib, and the entire project is wrapped in a user-friendly Streamlit app.
Use this command in the terminal to view it in the browser: streamlit run streamlit_app.py
If you havent installed streamlit write this in the terminal: pip install streamlit

