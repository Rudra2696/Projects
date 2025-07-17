# Importing the TextBlob library for sentiment analysis
from textblob import TextBlob

# Defining a function to analyze sentiment of given text
def analyze_sentiment(text):
    if not text:
        raise ValueError("Text cannot be empty")

    # Creating a TextBlob object
    blob = TextBlob(text)
    if not blob:
        raise ValueError("TextBlob object is null")

    # Getting the polarity score (-1 to 1)
    sentiment = blob.sentiment.polarity
    # If score > 0, it's positive
    if sentiment > 0:
        return "Positive"
    # If score < 0, it's negative
    elif sentiment < 0:
        return "Negative"
    # If score is 0, it's neutral
    else:
        return "Neutral"
print("DV06AI00026")
# Sample text inputs to test the function
text1 =input("Enter text to analyze : ")

# Printing the sentiment result for each input
print("Text :", analyze_sentiment(text1))

