import string

from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

lemma = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation)

tree = etree.parse('news.xml')

root = tree.getroot()

news_headings = []
cleaned_news_items = []

for news_row in root[0]:
    news_headings.append(news_row[0].text)
    text = news_row[1].text.lower()
    words = word_tokenize(text)

    words = [lemma.lemmatize(word) for word in words]

    words = [word for word in words if word not in stop_words]

    words = [word for word in words if nltk.pos_tag([word])[0][1] == "NN"]

    cleaned_news_items.append(" ".join(words))

vectoriser = TfidfVectorizer()
fitted_words = vectoriser.fit_transform(cleaned_news_items)

word_list = [[(vectoriser.get_feature_names()[fitted_words[i].indices[j]], fitted_words[i].data[j]) for j in
              range(fitted_words[i].data.shape[0])] for i in range(fitted_words.shape[0])]

for j in range(len(word_list)):
    sorted_list = sorted(sorted(word_list[j], key=lambda x: x[0], reverse=True), key=lambda x: x[1], reverse=True)[0:5]
    print(f"{news_headings[j]}:")
    print(" ".join([i[0] for i in sorted_list]))
    print()
