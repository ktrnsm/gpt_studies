import os
import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'

nltk.download('vader_lexicon')

def getDatapoint(line):
    splitline = line.split('] ')
    dateTime = splitline[0].strip('[')
    date, time = dateTime.split(' ')
    message = " ".join(splitline[1:])
    if ":" in message:
        splitmessage = message.split(": ")
        author = splitmessage[0]
        message = " ".join(splitmessage[1:])
    else:
        author = None
    return date, time, author, message

data = []
conversation = 'C:/Users/Şebnem/Desktop/chat_data.txt'
with open(conversation, encoding="utf-8") as fp:
    messageBuffer = []
    date, time, author = None, None, None
    for line in fp:
        line = line.strip()
        if re.match(r"^\[\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}\]", line):
            if len(messageBuffer) > 0:
                data.append([date, time, author, ' '.join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message = getDatapoint(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

if len(messageBuffer) > 0:
    data.append([date, time, author, ' '.join(messageBuffer)])

df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])

# Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
df['Sentiment'] = df['Message'].apply(lambda x: analyzer.polarity_scores(x))

# Extract sentiment scores
df['Positive'] = df['Sentiment'].apply(lambda x: x['pos'])
df['Negative'] = df['Sentiment'].apply(lambda x: x['neg'])
df['Neutral'] = df['Sentiment'].apply(lambda x: x['neu'])

# Convert date and time columns to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%I:%M %p').dt.strftime('%I:%M %p')

print(df.head())

# Set the style of the plot
plt.style.use('seaborn-whitegrid')

# Create a figure and axis
fig, ax = plt.subplots()

# Get the first 10 rows
df_first_10 = df.head(10)

# Plot the Positive, Negative, and Neutral scores
x = range(10)
ax.plot(x, df_first_10['Positive'], label='Positive')
ax.plot(x, df_first_10['Negative'], label='Negative')
ax.plot(x, df_first_10['Neutral'], label='Neutral')

# Set the x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(df_first_10['Time'], rotation=45)

# Set the y-axis label
ax.set_ylabel('Sentiment Score')

# Set the title and legend
ax.set_title('Sentiment Analysis')
ax.legend()

# Show the plot
plt.show()














