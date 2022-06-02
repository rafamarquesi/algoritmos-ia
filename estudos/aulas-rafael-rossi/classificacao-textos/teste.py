'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkV1euSfT1YaE1rT-d8cXE-I)'''

# Importando as Bibliotecas
import numpy as np

import pandas as pd
pd.set_option('max_colwidth', 250)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

if __name__ == '__main__':
    # Base de Textos
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

    #print(df)

    vetorizador = CountVectorizer(lowercase=True, stop_words='english',
                                  token_pattern=r'(?u)\b\w\w+\b', min_df=2,
                                  ngram_range=(1,1), dtype=np.int16)

    # vetorizador = TfidfVectorizer(
    #     lowercase=True, stop_words='english',
    #     token_pattern=r'(?u)\b\w\w+\b', min_df=2,
    #     ngram_range=(1, 1), dtype=np.float32
    # )

    vetorizador.fit(df['texts'])

    print(vetorizador.vocabulary_)

    representacao = vetorizador.transform(df['texts'])

    print(representacao.toarray())

    termos = [item[0] for item in sorted(vetorizador.vocabulary_.items(), key=lambda x:x[1])]
    print(termos)

    df_repr = pd.DataFrame(representacao.toarray(), columns=termos)
    print(df_repr.shape)

    # Treinando um modelo de classificação
    from sklearn.neighbors import KNeighborsClassifier

    modelo = KNeighborsClassifier(n_neighbors=2, metric='cosine')
    modelo.fit(representacao, df['classes'])

    # Predizendo novos exemplos
    novos_textos = ['Goku will have to save the earth again in Dragon Ball',
                    'Seiya is loyal to Athena']
    repr_novos = vetorizador.transform(novos_textos)
    print(repr_novos.toarray().shape)
    print(modelo.predict(repr_novos))