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
    st.success('This is a success message!')
    st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">Buonasera</p>', unsafe_allow_html=True)
    # warnings.filterwarnings('ignore')
    # absolute_path = os.path.dirname(__file__)
    # relative_path = "src/lib"
    # full_path = os.path.join(absolute_path)
    # model = joblib.load("regression_test.pkl")
    # x1 = st.number_input("Inserisci",,)
    # x2 = st.number_input("Inserisci",,)
    # x3 = st.number_input("Inserisci",,)
    # y_pred=model.predict([[x1,x2,x3]])[0]
    # st.write("Predizione = ",y_pred)
    # df_res=pd.DataFrame(data = [y_pred,y_test])
    # Y = pd.DataFrame(y_pred,columns=[f"predizione {target}"])


    # buffer = io.BytesIO()
    # # download button 2 to download dataframe as xlsx
    # with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    #     # Write each dataframe to a different worksheet.
    #     Y.to_excel(writer, sheet_name='Sheet1', index=False)
    #     # Close the Pandas Excel writer and output the Excel file to the buffer
    #     writer.save()

    #     download2 = st.download_button(
    #         label="Download data as Excel",
    #         data=buffer,
    #         file_name='large_df.xlsx',
    #         mime='application/vnd.ms-excel'
    #     )
        
if __name__=="__main__":
    main()