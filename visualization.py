import streamlit as st
import pandas as pd 
import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import seaborn as sns 


df_raw = pd.read_csv("supermarket_sales - Sheet1.csv") 
df = df_raw.copy()

def App():
    st.title("Visualization Dashboard")

    df_supermarket_col = st.selectbox("Percentage of Supermarket Categories", ['Product Line', 'City', 'Branch', 'Customer Type', 'Gender', 'Payment Method']) 

    if df_supermarket_col == 'Product Line':
        products = df['Product line'].value_counts() 
        products.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="Product Line Percentation")
        st.pyplot()
    elif df_supermarket_col == 'City':
        cities = df['City'].value_counts()
        cities.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="City Percentation")
        st.pyplot()
    elif df_supermarket_col == 'Branch':
        branchs = df['Branch'].value_counts() 
        branchs.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="Branch Percentation")
        st.pyplot()
    elif df_supermarket_col == 'Customer Type':
        customers = df['Customer type'].value_counts()
        customers.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="Customer Type Percentation")
        st.pyplot()
    elif df_supermarket_col == 'Gender':
        genders = df['Gender'].value_counts() 
        genders.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="Gender Percentation")
        st.pyplot()
    else:
        payment = df['Payment'].value_counts()
        payment.plot(kind='pie', figsize=[16, 8], autopct='%1.1f%%', title="Payment Methods Percentation")
        st.pyplot()

    df_gross_in_branch = st.selectbox("The Gross Income of Supermarket's Branches", ["Daily Gross Income", "Gender", "Customer Type", "Product Line","Payment Method"]) 

    if df_gross_in_branch == "Daily Gross Income": 
        daily_gross_income_a = df[df['Branch']=='A'].groupby('Date').sum()['gross income']
        daily_gross_income_b = df[df['Branch']=='B'].groupby('Date').sum()['gross income']
        daily_gross_income_c = df[df['Branch']=='C'].groupby('Date').sum()['gross income'] 

        daily_gross_income_a.plot(figsize=(16,8), label= 'Branch A') 
        daily_gross_income_b.plot(figsize=(16,8), label= 'Branch B')
        daily_gross_income_c.plot(figsize=(16,8), label= 'Branch C')


        plt.legend()
        plt.ylabel("Gross Income ($)")
        plt.title("DAILY GROSS INCOME IN EVERY BRANCH")
        st.pyplot()
    elif df_gross_in_branch == "Gender":
        with sns.axes_style(style='whitegrid'):
            a = sns.factorplot("Branch", "gross income", "Gender", data=df, kind="bar", ci=None, palette="Blues_d")
            a.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON GENDER")
        st.pyplot(a)
    elif df_gross_in_branch == "Customer Type":
        with sns.axes_style(style='whitegrid'):
            b = sns.factorplot("Branch", "gross income", "Customer type", data=df, kind="bar", ci=None, palette="Blues_d")
            b.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON CUSTOMER TYPE")
        st.pyplot(b) 
    elif df_gross_in_branch == "Product Line":
        with sns.axes_style(style='whitegrid'):
            c = sns.factorplot("Branch", "gross income", "Product line", data=df, kind="bar", ci=None, palette="Blues_d")
            c.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON PRODUCT LINE")
        st.pyplot(c)
    else:
        with sns.axes_style(style='whitegrid'):
            d = sns.factorplot("Branch", "gross income", "Payment", data=df, kind="bar", ci=None, palette="Blues_d")
            d.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON PAYMENT METHOD")
        st.pyplot(d)



st.set_option('deprecation.showPyplotGlobalUse', False)