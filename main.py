from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Load file
file = open('input.txt')
text = file.read()
file.close()

# Tokenize the text
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

# Create a frequency table to keep the score of each word
freqTable = {}
for word in words:
    word = word.lower()
    if word in stop_words:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Create a dictionary to keep the score of each sentence
sentences = sent_tokenize(text)
sentence_values = {}

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentence_values:
                sentence_values[sentence] += freq
            else:
                sentence_values[sentence] = freq

sum_values = 0
for sentence in sentence_values:
    sum_values += sentence_values[sentence]

# Average value of a sentence from the original text
average = int(sum_values / len(sentence_values))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentence_values) and (sentence_values[sentence] > (1.2 * average)):
        summary += " " + sentence

print(summary)
