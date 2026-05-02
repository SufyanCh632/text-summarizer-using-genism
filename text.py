# Import Necessary Libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required data (only needed once)
nltk.download("stopwords")
nltk.download("punkt")

# Example text
text = """
The concept of artificial intelligence found life long before computers. 
Humans throughout history contemplated the nature of existence, consciousness, and creation, and it’s only natural that from those musings came a variety of myths and art. 
Intelligent beings created through artificial means feature prominently in many belief systems, like the Norse figure, Kvasir, the Greek automaton, Talos, or the Jewish folklore figure of the golem. 
Examples in popular media abound, beginning in the modern era with Mary Shelley’s 1818 novel Frankenstein; Karel Čapek’s 1920 play R.U.R.; and Fritz Lang’s 1927 film Metropolis. 
The ethical quandaries and risks associated with artificial intelligence have long been on the mind of the human race.
"""

# Function
def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    word_frequencies = {}

    for word in words:
        if word.isalpha() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = " ".join(summary_sentences)
    return summary

# Call function (OUTSIDE function)
summary = summarize_text(text, num_sentences=2)

print("Original Text:\n", text)
print("\nSummary:\n", summary)