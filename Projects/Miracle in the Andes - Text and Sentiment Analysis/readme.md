# Miracle in the Andes - Text and Sentiment Analysis

This project performs text analysis and sentiment evaluation on the book *“Miracle in the Andes”*. It extracts key information such as chapter titles, word frequency, sentences and paragraphs containing specific words, and analyzes sentiment scores chapter-wise.

## Features

- Count the number of chapters in the book  
- Extract sentences and paragraphs containing specific keywords (e.g., “love”)  
- Retrieve all chapter titles  
- Calculate word frequency excluding stopwords  
- Perform sentiment analysis for the entire book and for each chapter  
- Identify chapters with the most positive or negative sentiments

## Technologies Used

- Python  
- Regular Expressions (`re` module)  
- [NLTK](https://www.nltk.org/) for stopwords and sentiment analysis  
- VADER SentimentIntensityAnalyzer from NLTK’s `sentiment` module

## Installation

1. Clone the repository or download the project files.  
2. Install required Python packages:

    ```bash
    pip install nltk
    ```

3. Download necessary NLTK data (run in Python shell or script):

    ```python
    import nltk
    nltk.download('vader_lexicon')
    nltk.download('stopwords')
    ```

4. Place the book text file (`miracle_in_the_andes.txt`) in the project directory.

## Usage

Run your Python script to analyze the book. Example snippet:

```python
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Read book text
with open('miracle_in_the_andes.txt', 'r') as file:
    book = file.read()

# Split chapters
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)[1:]  # Skip any preface text

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment per chapter
for i, chapter in enumerate(chapters, 1):
    scores = analyzer.polarity_scores(chapter)
    print(f"Chapter {i} Sentiment Scores: {scores}")
