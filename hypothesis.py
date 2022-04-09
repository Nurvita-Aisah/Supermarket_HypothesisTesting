import streamlit as st
import pandas as pd 
import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import seaborn as sns 


df_raw = pd.read_csv("supermarket_sales - Sheet1.csv") 
df = df_raw.copy()

def App():
    st.title("Hypothesis Testing Dashboard")

    df_msc_col = st.selectbox("MEASURE OF CENTRAL TENDENCY OF SUPERMARKET'S BRANCHES BASED ON GROSS INCOME", ["Gender", "Customer Type", "Product Line","Payment Method"])

    if df_msc_col == "Gender":
        with sns.axes_style(style='ticks'):
            a = sns.factorplot("Branch", "gross income", "Gender", data=df, kind="box", palette="crest")
            a.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON GENDER")
        st.pyplot(a)
    elif df_msc_col == "Customer Type":
        with sns.axes_style(style='ticks'):
            b = sns.factorplot("Branch", "gross income", "Customer type", data=df, kind="box", palette="crest")
            b.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON CUSTOMER TYPE")
        st.pyplot(b)
    elif df_msc_col == "Product Line":
        with sns.axes_style(style='ticks'):
            c = sns.factorplot("Branch", "gross income", "Product line", data=df, kind="box", palette="crest")
            c.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON PRODUCT LINE")
        st.pyplot(c)
    else: 
        with sns.axes_style(style='ticks'):
            d = sns.factorplot("Branch", "gross income", "Payment", data=df, kind="box", palette="crest")
            d.set_axis_labels("Branch", "Gross Income");
        plt.title("THE GROSS INCOME IN EVERY BRANCH BASED ON PAYMENT METHOD")
        st.pyplot(d)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write('''
        **The Hypothesis**

        In the hypothesis testing, we compare whether the average gross income of Branch A, Branch B, and Branch C are significantly different or not. 
        We test the null hypothesis with the assumption that the significant level is 5% (0.05) and the methodology we use is ANOVA.
        ANOVA methodology is used for comparing more than two variables. The hypothesis we use in this case as follows:

        **H0: μ the gross income of Branch A = μ the gross income of Branch B = μ the gross income of Branch C**

        **H0: μ the gross income of Branch A != μ the gross income of Branch B != μ the gross income of Branch C**

        **ANOVA Testing Result**
        - The average of Branch A gross income :  14.87
        - The average of Branch B gross income :  15.23
        - The average of Branch C gross income :  16.05
        - P-Value                              :  0.41
        - F-Statistics                         :  0.88

        **The Conclusion**
        
        Since the p-value obtained (0.41) is greater than the significance level (0.05), thus we accept the null hypothesis. 
        It could be implied that the average gross income of Branch A, Branch B, and Branch C are insignificant.
    ''')
