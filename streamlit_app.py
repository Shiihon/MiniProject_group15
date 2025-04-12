#Json: to save and read data from our file
#Requests: to fetch data from the API that we found on an open source "cvrapi.dk", public api's.
#Pandas: We use pandas to work with data in a table format
#Streamlit: Is used to build the application(remember to download streamlit in the terminal). To open it in the browser, write: streamlit run stremlit_app.py (<- the files name), in the terminal.
#matplotlib:Creating charts.
import json
import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# st. stands for= streamlit
# st.titel: Biggest text at the top — like the main title. 
# st.write() → Normal text or description.
st.title("Clean Analysis of Company Data with the CVR API")
st.write("Search for any Danish company and find their details, including the number of employees.")


# User interaction/input happens here:
# Line 22: We create an input section where the user can type the name of a company.
company = st.text_input("Enter the company's name:")

#I will split the code so it will be easier to udnerstand:
# If the user clicks on the search button, then a request will be sent to our api
if st.button("Search"):

    # Our API have the following details;
    # url= of the api we want to use 
    # params(meaning parameters), that is the exstra data we send with the request -> "search": the company name that the user type, "country": we set it to "dk" for denmark.
    # headers= its information the api needs, its basically the same as saying "who is calling?" 
    # Why user-agent you proberly be thinking? We use user-agent because in python they expect an "user-agent", as an keyword for "hey, hello I am not spam or a annoying bot, I AM A REAL USER". 
    url = 'https://cvrapi.dk/api'
    params = {'search': company, 'country': 'dk'}
    headers = {'User-Agent': 'user'}

    # And now we send our GEt request to the API with our URL, params and headers. 
    # If everything went sucessfully, we receive a response 200, which means everything went OK:)
    # After that, the response is converted to json format 
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()

    # A good reminder would be to save the raw data somewhere, so we always have an backup. 
    # So what we do is to use "open()", a python function that opens a file
    # We write the files name "apitest.json", so it knows, what to open? 
    # f= file 
    # w= opens the file in "write" mode.
    # json.dump(data, f)= dumps the data into a file, in json fomat.
        with open('apitest.json', 'w') as f:
            json.dump(data, f)

    
    # df= Meaning-> DataFrame -> When we talk about data frame, we usally think of it as a table, like excel, but inside python:)
    # pd= Meaning -> Pandas Liberay. 
    # json_normalize() is a function inside pandas.
        df = pd.json_normalize(data)
    
    # Here we only choose the most relevant columns to show the user
    # VAT= Value Added Tax number — unique company ID (CVR number that is used here in Denmark)
        selected_fields = ['vat', 'name', 'address', 'zipcode', 'city', 'employees', 'industrydesc']
        df_selected = df[selected_fields]

    
    # st.subheader() → Smaller heading, used to give a label to smaller sections
    # st.dataframe(df_selected) -> Shows the selected data as a table
        st.subheader("The Company's data")
        st.dataframe(df_selected)
    
    # csv = df_selected.to_csv(index=False).encode('utf-8')= Convert the selected data to CSV format
    # st.download_button= Creating a download button in Streamlit Giving the user the oppitunity to download the data as CSV.
        csv = df_selected.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='selected_company_data.csv',
            mime='text/csv',
        )

    #  First, I check if there is any data in the 'employees' column by using notnull().any()
    #  If yes, I continue to show a section title using Streamlit's subheader()
    #  Then, I plot a bar chart of the number of employees using plot(kind='bar')
    #  I label the x-axis as 'Company' and the y-axis as 'Number of Employees'
    #  I make sure the labels are straight with plt.xticks(rotation=0) and finally display the chart in the app with st.pyplot().
    # If there is no data, I show a warning message to the user. And if the API call itself failed, I show an error message with the status code.
        if df_selected['employees'].notnull().any():
            st.subheader("Number of Employees")
            df_selected['employees'].plot(kind='bar', title='Number of employees in the company')
            plt.xlabel("Company")
            plt.ylabel("Number of Employees")
            plt.xticks(rotation=0)
            st.pyplot(plt.gcf())
        else:
            st.warning("No data available for number of employees.")
    else:
        st.error(f"API call failed with status code: {response.status_code}")