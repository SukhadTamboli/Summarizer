import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = """
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[33]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.
"""
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm') #.bin 
doc = nlp(text)
tokens = [token.text for token in doc]
#print(tokens)
punctuation = punctuation + '\n'
word_frequencies = {}
for word in doc:
  if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
  word_frequencies[word] = word_frequencies[word]/max_frequency
sentence_tokens = [sent for sent in doc.sents]
sentence_scores = {}
for sent in sentence_tokens:
  for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
            select_length = int(len(sentence_tokens)*0.3)
summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)

print(summary)