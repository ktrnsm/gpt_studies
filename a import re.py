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

# Read the file and extract data
data = []
with open('C:/Users/Şebnem/Desktop/c.txt', 'r',encoding="utf8") as file:
    for line in file.readlines():
        match = re.match(pattern, line.strip())
        if match:
            date = match.group(1)
            time = match.group(2)
            author = match.group(3)
            message = match.group(4)
            message = re.sub('[' + re.escape(string.punctuation) + ']', '', message)

            data.append([date, time, author, message])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])

# Perform further data processing or analysis using the DataFrame
#print(df)

def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

stopwords_list = set(stopwords.words('turkish'))
additional_stopwords = ["bir", "bu", "ok", "ve", "ben", "gibi", "için", "ne", "ok", "de", "da", "ama", "beni", "sen", "mi"]
stopwords_list.update(additional_stopwords)
df['Processed_Message'] = df['Message'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word.lower() not in stopwords_list]))

df['Sentiment'] = df['Processed_Message'].apply(sentiment_analysis)



#print(df[['Message', 'Processed_Message']])


positive_messages = df[df['Sentiment'] == 'Positive']['Processed_Message']
negative_messages = df[df['Sentiment'] == 'Negative']['Processed_Message']
neutral_messages = df[df['Sentiment'] == 'Neutral']['Processed_Message']

positive_wordcloud = WordCloud().generate(' '.join(positive_messages))
negative_wordcloud = WordCloud().generate(' '.join(negative_messages))
neutral_wordcloud = WordCloud().generate(' '.join(neutral_messages))

# Plot the word clouds
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.title('Positive Sentiment')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.title('Negative Sentiment')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(neutral_wordcloud, interpolation='bilinear')
plt.title('Neutral Sentiment')
plt.axis('off')

plt.show()