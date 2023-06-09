#whatsapp sent analyse
import re
import string
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')

from wordcloud import WordCloud
import matplotlib.pyplot as plt



# Define the pattern for extracting data
pattern = r'^\[(\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2}:\d{2})\] ([^:]+): (.+)$'

def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding="utf8") as file:
        for line in file.readlines():
            match = re.match(pattern, line.strip())
            if match:
                date = match.group(1)
                time = match.group(2)
                author = match.group(3)
                message = match.group(4)
                message = re.sub('[' + re.escape(string.punctuation) + ']', '', message)
                data.append([date, time, author, message])
    return data

def preprocess_message(message):
    stopwords_list = set(stopwords.words('turkish'))
    additional_stopwords = ["bir", "bu", "ok", "ve", "ben", "gibi", "için", "ne", "ok", "de", "da", "ama", "beni", "sen", "mi","görüntü dahil edilmedi"]
    stopwords_list.update(additional_stopwords)
    processed_message = ' '.join([word for word in word_tokenize(message) if word.lower() not in stopwords_list])
    return processed_message

def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def visualize_word_cloud(sentiment, messages):
    wordcloud = WordCloud().generate(' '.join(messages))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(sentiment + ' Sentiment')
    plt.axis('off')
    plt.show()

# Load the data
file_path = 'C:/Users/Şebnem/Desktop/c.txt'
data = load_data(file_path)

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])

# Preprocess the messages
df['Processed_Message'] = df['Message'].apply(preprocess_message)

# Perform sentiment analysis
df['Sentiment'] = df['Processed_Message'].apply(perform_sentiment_analysis)

# Data Summary
num_messages = len(df)
num_authors = len(df['Author'].unique())
print("Data Summary:")
print("Number of Messages:", num_messages)
print("Number of Authors:", num_authors)

# Sentiment Distribution
sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar', rot=0)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Word Clouds for each sentiment
sentiments = ['Positive', 'Negative', 'Neutral']
for sentiment in sentiments:
    messages = df[df['Sentiment'] == sentiment]['Processed_Message']
    visualize_word_cloud(sentiment, messages)

# Top Authors
top_authors = df['Author'].value_counts().head(5)
top_authors.plot(kind='bar', rot=0)
plt.title("Top 5 Authors")
plt.xlabel("Author")
plt.ylabel("Message Count")
plt.show()

# Most Frequent Words
word_counts = df['Processed_Message'].str.split(expand=True).stack().value_counts()
top_words = word_counts.head(10)
top_words.plot(kind='bar', rot=45)
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Count")
plt.show()


sentiment_counts = df.groupby(['Date', 'Sentiment']).size().unstack(fill_value=0)
sentiment_counts['Positive'] = sentiment_counts['Positive'].cumsum()
sentiment_counts['Negative'] = sentiment_counts['Negative'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(sentiment_counts.index, sentiment_counts['Positive'], label='Positive')
plt.plot(sentiment_counts.index, sentiment_counts['Negative'], label='Negative')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Change in Positive and Negative Sentiments over Time')
plt.legend()
plt.xticks(rotation=45)
plt.show()
