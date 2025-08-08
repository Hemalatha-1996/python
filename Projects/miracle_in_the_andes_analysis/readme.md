# Miracle in the Andes - Text and Sentiment Analysis

This project performs text analysis and sentiment evaluation on the book *“Miracle in the Andes”*. It extracts chapters, counts word frequencies, finds sentences and paragraphs containing specific words, and analyzes sentiment scores chapter-wise.

## Features

- Load and parse the full text of the book.
- Count the number of chapters.
- Extract sentences and paragraphs containing specific keywords like "love".
- Extract chapter titles using multiple methods.
- Compute word frequency distribution.
- Filter out common stopwords to find meaningful frequent words.
- Search for the occurrence count of any given word.
- Perform sentiment analysis on the whole book and each chapter using NLTK's VADER.

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- NLTK (Natural Language Toolkit)
- NLTK SentimentIntensityAnalyzer for sentiment analysis

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/miracle-in-the-andes-nlp.git
