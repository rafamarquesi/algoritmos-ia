'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''
#Importações
import re
import string
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer, TweetTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer

#Corpus
nltk.download('machado')
nltk.download('punkt')
from nltk.corpus import machado

#Stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

nltk.download('rslp')
nltk.download('wordnet')
nltk.download('omw-1.4')

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


if __name__ == '__main__':
    # Trabalhando com o corpus
    print(machado.fileids()[:3])

    print(machado.raw('contos/macn002.txt'))

    print(machado.categories('contos/macn002.txt'))

    print(machado.words('contos/macn002.txt'))

    print(machado.sents('contos/macn002.txt')[100])

    #Lista de stopwords
    stopwords_pt = stopwords.words('portuguese')
    stopwords_pt.append('jogar')
    print(stopwords_pt)

    #Tokenização
    texto = 'Goku is a hero in the Dragon Ball since 1989! Goku saved the earth so many times.'

    print(word_tokenize(texto))

    print(sent_tokenize(texto))

    token_regex = RegexpTokenizer(r'[A-Z]\w+')
    print(token_regex.tokenize(texto))

    texto_twt = "I'm veryyy happyyyyyyyyy :P :D #betterlife @bstionson"

    print(word_tokenize(texto_twt))

    twt_tokenizer = TweetTokenizer()

    print(twt_tokenizer.tokenize(texto_twt))

    twt_tokenizer2 = TweetTokenizer(strip_handles=True, reduce_len=True)

    print(twt_tokenizer2.tokenize(texto_twt))

    #Simplificação das Palavras
    ##Radicalização com o algoritmo de Porter
    porter_stemmer = PorterStemmer()

    print(porter_stemmer.stem('computing'))
    print(porter_stemmer.stem('computer'))
    print(porter_stemmer.stem('computers'))

    ## Radicalização com o algoritmo Snowball
    print(SnowballStemmer.languages)

    snow_stemmer = SnowballStemmer('portuguese')
    print(snow_stemmer.stem('computadores'))
    print(snow_stemmer.stem('computação'))
    print(snow_stemmer.stem('computando'))

    # Radicalização com RSLPStemmer
    rslp_stemmer = RSLPStemmer()
    print('aqui')
    print(rslp_stemmer.stem('computadores'))
    print(rslp_stemmer.stem('computação'))
    print(rslp_stemmer.stem('computando'))

    ## Lematização com WordNetLemmatizer
    wn_lemmatizer = WordNetLemmatizer()

    print(wn_lemmatizer.lemmatize('rocks'))

    print(wn_lemmatizer.lemmatize('corpora'))

    print(wn_lemmatizer.lemmatize('doing', pos='v'))

    print(wn_lemmatizer.lemmatize('better', pos='a'))

    ##POS Tagging
    text = 'I love Google. Google is the best.'

    print(nltk.pos_tag(word_tokenize(text)))

    text2 = 'Rafael is working at Google in the South America'

    print(nltk.ne_chunk(nltk.pos_tag(word_tokenize(text2))))

    # Integrando NLTK e o ScikitLearn
    stopwords_en = stopwords.words('english')
    lematizador = WordNetLemmatizer()
    pd.set_option('max_colwidth', 250)
    reNumber = re.compile(r'\d+')

    def preprocessamento(texto):
        tokens = word_tokenize(texto)
        final_tokens = []
        for token in tokens:
            if not reNumber.match(token):
                if token not in string.punctuation:
                    token = token.lower()
                    if token not in stopwords_en:
                        token = lematizador.lemmatize(token)
                        final_tokens.append(token)
        return ' '.join(final_tokens)

    texts = [
        'Goku is a hero in the Cragon Ball since 1989! Goku saved the earth so many times.',
        'The 7 Dragon balls can make wishes come true! Each ball contains his own dragon.',
        'If the wishes are superfluous, the dragon balls will become dark.',
        'Seiya is a bronze knight and is one of the main Knights of the Zodiac. He saved Athena several times.',
        'A knight of the zodiac wear a bronze, silver or a gold cloth to protect Athena.',
        'Saint Seiya: Knights of the Zodiac is a Japanese manga in which mystical warriors called the Saints fight wearing sacred cloths.'
    ]
    classes = ['Dragon Ball', 'Dragon Ball', 'Dragon Ball', 'Cav. Zod.', 'Cav. Zod.', 'Cav. Zod.']

    df = pd.DataFrame({'texts': texts, 'classes': classes})

    # print(df)

    df['textos_preproc'] = df['texts'].apply(preprocessamento)

    vetorizador = CountVectorizer(min_df=2)

    vetorizador.fit(df['textos_preproc'])

    representacao = vetorizador.transform(df['textos_preproc'])

    print(representacao.toarray())

    termos = [item[0] for item in sorted(vetorizador.vocabulary_.items(), key=lambda x: x[1])]
    df_repr = pd.DataFrame(representacao.toarray(), columns=termos)
    print(df_repr.shape)