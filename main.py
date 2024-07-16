import glob
import streamlit as st
import pathlib
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

# Obtain filenames
files = glob.glob('files/*.txt')

# Create analyzer and get scores
results = {}
analyzer = SentimentIntensityAnalyzer()
for file in files:
    with open(file, 'r') as text:
        content = text.read()
    scores = analyzer.polarity_scores(content)
    date = pathlib.Path(file).stem
    results[date] = scores

pos = [(key,value['pos']) for key,value in results.items()]
neg = [(key, value['neg']) for key, value in results.items()]

# Positive diagram
x_pos = [date for (date,value) in sorted(pos)]
y_pos = [value for (date,value) in sorted(pos)]
figure_pos = px.line(x=x_pos, y=y_pos, labels={'x': 'Date', 'y': 'Scores'})

# Negative diagram
x_neg = [date for (date,value) in sorted(neg)]
y_neg = [value for (date,value) in sorted(neg)]
figure_neg = px.line(x=x_neg, y=y_neg, labels={'x': 'Date', 'y': 'Scores'})

st.set_page_config(layout='centered')
st.header('Diary Tone')

st.subheader('Positivity')
st.plotly_chart(figure_pos)

st.subheader('Negativity')
st.plotly_chart(figure_neg)
