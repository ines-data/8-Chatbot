import string
from joblib import load
import pymongo
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

client = pymongo.MongoClient("mongodb+srv://africa:africa2021@bot.cb1sv.mongodb.net/NougatBD2?retryWrites=true&w=majority")

mydb = client["NougatBD2"]
mycols = [mydb["astro2"],mydb["bioinfo"],mydb["datascience"]]

myclient = pymongo.MongoClient("mongodb+srv://africa:africa2021@bot.cb1sv.mongodb.net/NougatBD2?retryWrites=true&w=majority")
mydb = myclient["NougatBD2"]

myquery1 = { "PostTypeId": 1 }
myquery2 = { "PostTypeId": 2 }
clf = load('logreg.joblib')

porter = PorterStemmer()

list_ = ["hello"," here", "yes","no", "now", "later", "today", "tomorow","day" ,
        "if","else", "for", "to", "night","hi","hey", "how", "are" ,"you","thanks" ,
        "welcome", "quit" ,"bye", "sat", "imp", 'very','good']




def resarchQuestion(asked_question):
    id=None
    y_pred =clf.predict([asked_question])
    y= y_pred[0]
    mycol = mycols[y]
    mydoc = mycol.find({"$text": {"$search": asked_question}},{"score": {"$meta": "textScore"}})
    mydoc1= mydoc.sort([("score", {"$meta":"textScore"})]).limit(1)
    for x in mydoc1:
        id = x['AcceptedAnswerId']
        true_question = x['question']


    # comparaison 
    if(id != None) : 
        words_aquestion = tokenize(asked_question)
        words_aq_stem = [porter.stem(words_aquestion) for words_aquestion in words_aquestion]
        matching = check(words_aq_stem,true_question )
    
    if(not(matching)) : id=None

    return id,y


def get_response(_id,y) : 
    myquery1 = { "_id": _id }
    mycol = mycols[y]
    reponses = mycol.find(myquery1)
    for rep in reponses :
        reponse = rep['response']
    return reponse



def tokenize(corpus):
    #Tokenization
    words=[]
    tokens = nltk.word_tokenize(corpus)
    words.append(tokens)
    flat_words = [item for sublist in words for item in sublist]
    stopW = stopwords.words('english')
    stopW.extend(set(string.punctuation))
    tokens_without_stopwords = [x for x in flat_words if x not in stopW]
    return tokens_without_stopwords

def check(words, sentence): 
    matching = False
    
    
    k = [ w.lower() for w in words if w.lower() in sentence.lower() ]   # tous les words qui matches

    for word in k:  
        if word in list_:
            k.remove(word)

    print('len words in question = ', len(words))
    print('words =', words)
    print('len words found = ', len(k))
    print('k = ', k)
    if(len(k)<2) : matching = False
    else : 
        percent =  len(k)/len(words)
        print('percent = ', percent)
        if (percent >=0.6 ):   
            matching = True
    
    return matching