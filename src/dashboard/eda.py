import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def EDA(df):
    st.title("Exploratory Data Analysis")
    st.info("In this section, you are invited to create insightful graphs "
            "about the card fraud dataset that you were provided.")


    st.header("Dataset details")
    st.subheader("Head of DataSet")
    st.write(df.head(15))

    st.subheader('Shape of the dataframe')
    st.write(df.shape)

    st.subheader("Show fraud and valid transaction details")
    fraud=df[df.Class==1]
    valid=df[df.Class==0]

    st.write('Fraud Cases: ',len(fraud))
    st.write('Valid Cases: ',len(valid))


    st.header('Visualise charts')

    #Bar Chart
    st.subheader("Bar Chart of Class column")
    st.bar_chart(df['Class'].value_counts())

    st.subheader("Pie chart of Class column")
    fig, ax = plt.subplots(figsize=(8, 4.5))

    ax.pie(df["Class"].value_counts(), autopct='%0.2f%%',shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    st.subheader("Line Chart of Amount column")
    st.line_chart(df['Amount'])

    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)

       

    st.subheader("Correlation Matrix Table")
    st.dataframe(df.corr())

    st.header('Stats Details')
    st.subheader("Describe table")
    st.dataframe(df.describe())