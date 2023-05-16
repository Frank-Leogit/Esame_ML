import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st 
import io
from io import StringIO
from sklearn.model_selection import train_test_split
import joblib
import xlsxwriter
from sklearn.linear_model import LinearRegression
import os
import warnings



def main():
    warnings.filterwarnings('ignore')
    absolute_path = os.path.dirname(__file__)
    relative_path = "src/lib"
    full_path = os.path.join(absolute_path)
    model = joblib.load("regression_test.pkl")
    # I valori di massimo e minimo sono stati ottenuti dal describe
    x1= st.number_input("Inserisci il valore di rm",3.56,8.78,6.4,0.1)
    x2 = st.number_input("Inserisci il valore di ptratio",12.6,22.1,16.9,0.1)
    x3 = st.number_input("Inserisci lstat",1.73,37.97,6.4,0.1)
    y_pred=model.predict([[x1,x2,x3]])[0]
    st.write("Predizione = ",y_pred)
    #df_res=pd.DataFrame(data = [y_pred,y_test])
    #Y = pd.DataFrame(y_pred,columns=[f"predizione {target}"])
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        df=df[['rm', 'ptratio', 'lstat']]
        st.write(df)
        y_pred=model.predict(df.to_numpy())
        res = pd.DataFrame(y_pred,columns=["Predizione"])
        st.write(res)
    buffer = io.BytesIO()
    # download button 2 to download dataframe as xlsx
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.
        res.to_excel(writer, sheet_name='Sheet1', index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()

        download2 = st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='large_df.xlsx',
            mime='application/vnd.ms-excel'
        )
        
if __name__=="__main__":
    main()