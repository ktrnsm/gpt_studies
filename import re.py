import re
import pandas as pd
import numpy as np
import emoji
from collections import Counter
import matplotlib.pyplot as plt

# Sample data
data = [
    "[14.06.2018 12:52:43] gözümün nuru 💐💐💐: ‎Mesajlar ve aramalar uçtan uca şifrelidir.",
    "[14.06.2018 12:52:43] gözümün nuru 💐💐💐: Semih merhaba.Şebnem ben. Senin dağıtımda çektiğin bir fotoğraf vardı ya rica etsem onu bana atar mısın. Ve rıza gösterirsen de paylaşmak istiyorum.",
    "[14.06.2018 12:54:19] iktueren: Selamlar tabiki,",
    "[14.06.2018 12:54:35] iktueren: ‎görüntü dahil edilmedi",
    "[14.06.2018 12:55:08] iktueren: ‎görüntü dahil edilmedi",
    "[14.06.2018 12:55:52] gözümün nuru 💐💐💐: Ne güzel çekmişsin ya çok teşekkürler.",
    "[14.06.2018 12:56:21] iktueren: ‎görüntü dahil edilmedi"
]

# Preprocess the data (extract date, time, author, and message)
pattern = r'^\[(\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2}:\d{2})\] ([^:]+): (.+)$'
processed_data = []
for line in data:
    match = re.match(pattern, line)
    if match:
        date = match.group(1)
        time = match.group(2)
        author = match.group(3)
        message = match.group(4)
        processed_data.append([date, time, author, message])

# Create a DataFrame from the processed data
df = pd.DataFrame(processed_data, columns=['Date', 'Time', 'Author', 'Message'])

# Perform data analysis or visualization tasks using the DataFrame

# Example: Count the number of messages per author
message_counts = df['Author'].value_counts()

# Example: Plot a bar chart of message counts
plt.bar(message_counts.index, message_counts.values)
plt.xlabel('Author')
plt.ylabel('Message Count')
plt.title('Message Counts per Author')
plt.show()
