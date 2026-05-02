# text-summarizer-using-genism
It looks like you've put together a solid foundational script for **Extractive Text Summarization**. This approach is great because it relies on the actual weight of the words used in the text rather than trying to "rephrase" things (which is what more complex LLMs do).

However, I noticed a small indentation error at the end of your script that will prevent the summary from actually printing. Here is the corrected code and a quick breakdown of how this logic works.

### Corrected Python Script

The final block of code was indented inside the `summarize_text` function. In Python, anything indented under `return` will never be executed. I've moved those lines to the main level.

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary datasets
nltk.download("stopwords")
nltk.download("punkt")

text = """
The concept of artificial intelligence found life long before computers. 
Humans throughout history contemplated the nature of existence, consciousness, and creation, and it’s only natural that from those musings came a variety of myths and art. 
Intelligent beings created through artificial means feature prominently in many belief systems, like the Norse figure, Kvasir (a being made from the spit of the gods), the Greek automaton, Talos (a metal man forged to protect Crete), or the Jewish folklore figure of the golem (a clay being made to serve a master). 
Examples in popular media abound, beginning in the modern era with popular portrayals in Mary Shelley’s 1818 novel, Frankenstein; Czech writer Karel Čapek’s 1920 science-fiction play, R.U.R.; and Fritz Lang’s 1927 German expressionist film, Metropolis. 
The ethical quandaries and risks associated with artificially intelligent constructs have long been on the mind of the human race, and serve as a fascinating mirror into our own struggles with autonomy, existence, and our place as creators. 
"""

def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    word_frequencies = {}

    # Build the frequency dictionary
    for word in words:
        if word.isalpha() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Score sentences based on the sum of word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Sort and pick the top N sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Optional: Keep the sentences in their original order for better flow
    summary_sentences.sort(key=lambda x: sentences.index(x))
    
    return " ".join(summary_sentences)

# This part must NOT be indented inside the function
summary = summarize_text(text, num_sentences=2)
print("--- Original Text ---")
print(text.strip())
print("\n--- Summary ---")
print(summary)
```

---

### How This Algorithm Works

This is a **Frequency-Based Ranking** algorithm. It works through four distinct phases:

1.  **Preprocessing:** It cleans the text by removing "Stopwords" (common words like *the, is, at, which*) because they don't carry specific meaning, even though they appear frequently.
2.  **Word Weighting:** It counts how many times meaningful words (like *intelligence* or *myth*) appear. The logic is: "If a word appears often, it must be the main topic."
3.  **Sentence Scoring:** Each sentence gets a "score" by adding up the weights of the words it contains. Longer sentences with high-value keywords win.
4.  **Selection:** It picks the top $N$ sentences with the highest scores to form the summary.

### A Small Suggestion for Improvement
In the original script, the summary might feel "choppy" because it picks the top sentences and prints them in order of importance, not in the order they appeared in the text. I added a small line in the corrected version (`summary_sentences.sort(...)`) to ensure the summary maintains the original narrative flow!
