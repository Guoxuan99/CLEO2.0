import webbrowser
import os
import nltk
import textblob


# nltk.download('averaged_perceptron_tagger')
def give_recommendation(text: str):
    textblob.WordList.append("Lazada")
    blob = textblob.TextBlob(text)
    noun_phrase = blob.noun_phrases
    print(noun_phrase)
    if not noun_phrase:
        sentence = nltk.word_tokenize(text)
        list = [nouns[1] for nouns in nltk.pos_tag(sentence) if nouns[1] == 'NN']
        for word in list:
            url = f"https://www.lazada.com.my/catalog/?q={word}%20&rating=5"
            webbrowser.open(url=url, new=2)
        return
    phrase = str(noun_phrase[0]).replace(" ","+")
    url = f"https://www.lazada.com.my/catalog/?q={phrase}%20&rating=5"
    webbrowser.open(url=url, new=2)


text = "recommend me shoes"
# sentence = nltk.word_tokenize(text)
# list = nltk.pos_tag(sentence)
# print(list)
# give_recommendation(text)
from nltk.corpus import wordnet   #Import wordnet from the NLTK
synset = wordnet.synsets("shop")
print('Word and Type : ' + synset[0].name())
print('Synonym of Travel is: ' + synset[0].lemmas()[0].name())
print('The meaning of the word : ' + synset[0].definition())
print('Example of Travel : ' + str(synset[0].examples()))
print(synset)
sentence = nltk.word_tokenize("recommend me shoes")
list = [nouns[0] for nouns in nltk.pos_tag(sentence) if (nouns[1] == 'NN') | (nouns[1]=='NNS')]
