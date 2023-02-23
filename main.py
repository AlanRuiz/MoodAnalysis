import glob
import os
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

import function
from function import openFile

analyzer = SentimentIntensityAnalyzer()

#Pulls a list of all the file names .txt
diary_files = glob.glob("diary/*.txt")
diary_files = sorted(diary_files)

#Cleaned up Names that will only show the date
cleaned_dates = sorted([os.path.basename(file)[:10] for file in diary_files])

#Empty list to store content rating
positive_rating = []
negative_rating =[]

for file in diary_files:
    content_file = function.openFile(file)
    score = analyzer.polarity_scores(content_file)
    positive_rating.append(score["pos"])
    negative_rating.append(score['neg'])

st.title("Diary Tone")
st.subheader("Positivity")
positive_figure = px.line(x=cleaned_dates, y=positive_rating,
                          labels={"x":"Date","y":"Positivity"})
st.plotly_chart(positive_figure)

st.subheader("Negativity")
negative_figure = px.line(x=cleaned_dates, y=negative_rating,
                          labels={"x":"Date","y":"Negativity"})
st.plotly_chart(negative_figure)