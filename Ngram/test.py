import spacy

def bigram(doc):
    result=[]
    sentence=[]
    # only consider alaphabets
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    print(sentence)

    for i in range(len(sentence)-1):
        first_word=sentence[i]
        second_word=sentence[i+1]
        result.append([first_word,second_word])
    print(result)



#load English model
nlp=spacy.load('en_core_web_sm')

#create a document
doc=nlp('Mapbox, Inc. 50 Beale St., Floor 9 San Francisco, CA 94105')

bigram(doc)

#print(result)

