import pandas as pd
import numpy as np

'''Utilizado nas vídeos aulas do professor Rafael Rossi (https://www.youtube.com/playlist?list=PLAHmHkSA6KkWCgf7yayMVed0vCu95ZFV6)'''

if __name__ == '__main__':
    # Estruturas básicas - Series
    series1 = pd.Series(data=['Rafael','Ricardo','Ronaldo'], index=['000.121.321-10','123.321.121-32','998.887.776-62'],
                        dtype=str, copy=True, name='Nomes')
    print(series1)
    print(series1['000.121.321-10'])

    series2 = pd.Series(data=np.random.randint(100, size=10))
    print(series2)
    print(series2[1])
    print(series2.max())
    print(series2.sum())
    print(series2[0:3])
    print(series2 > 50)

    series3 = pd.Series(data={'SO':'Sistema Operacional', 'POO':'Programação orientada a objetos','IA':'Inteligência Artificial'})
    print(series3)
    print(series3['SO'])

    # Estruturas básicas - DataFrame
    dados = np.array(
        [
            ['Rafael', 1985, '345.666.888-99', 'SI'],
            ['Ricardo', 1980, '258.222.989-90', 'ADM'],
            ['Ronaldo', 1983, '555.654.987-98', 'CC']
        ]
    )
    df1 = pd.DataFrame(data=dados, columns=['Nome','Ano_Nasc','CPF','Curso'], index=dados[:,2])
    print(df1)

    df2 = pd.DataFrame(
        {
            'Nome':['Rafael','Ricardo','Ronaldo'],
            'Ano_Nasc':[1985,1980,1983],
            'CPF':['345.666.888-99','258.222.989-90','555.654.987-98'],
            'Curso':['SI','ADM','CC']
        }
    )
    print(df2)

    # Propriedades
    print(df2.shape)
    print(len(df2))
    print(df2.index)
    print(df1.index)
    print(df2.columns)
    print(df2.shape[0] * df2.shape[1])
    print(df2.size)

    #Entrada e saída em diferentes formatos
    #Entrada
    df3 = pd.read_csv(
        '/mnt/Dados/Mestrado_Computacao_Aplicada_UFMS/1_semestre/Inteligencia_Artificial/algoritmos-ia/trabalhofinalsemestre/TAB_MODELAGEM_ANIMAL_06052021_COMPAC.csv',
        sep=';', nrows=300)
    print(df3)

    df4 = pd.read_json('matriculas.json')
    print(df4)

    df5 = pd.read_json('matriculas_zuadas.json')
    print(df5)

    df7 = pd.read_json('https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking')
    print(df7)

    df6 = pd.read_html('https://www.ufms.br/cursos/graduacao/')
    print(type(df6))
    print(df6[0])

    # Saídas
    df2.to_csv('cadastro.csv', index=False)
    # df3.to_csv('TAB_MODELAGEM_ANIMAL_06052021_COMPAC.csv', sep=';', index=False)
    print(pd.read_csv('cadastro.csv'))
    print(df2.to_html(index=False))
    df2.to_html('cadastro.html', index=False)
    print(df2.to_latex(index=False))

    # Exibição
    print(df3)
    print(pd.options.display.max_rows)
    # pd.set_option('display.max_rows', None) # -> exibir todas linhas e colunas
    print(df3.head(n=10))
    print(df3.tail(n=10))

    print(df1['Nome'])
    df3['Peso'] = df3['Peso'].str.replace(',', '.').astype(float)
    print(df3['Peso'].sum())
    print(df1[['Nome','Curso']])
    print(df1.Nome)
    print(df1.iloc[1])
    print(df1.iloc[0:2])
    print(df1.loc['258.222.989-90'])
    print(df1['Nome'][0])
    print(df1.iloc[1,0])

    # Consultas
    print(df3[df3['CATEGORIA'] == 'AAA'])

    # Percorrendo elementos
    print(df2)
    num_linhas, num_colunas = df2.shape
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            print(df2.iloc[linha,coluna], end='\t')
        print()

    for linha in df2.index:
        for coluna in df2.columns:
            print(df2.loc[linha, coluna], end='\t')
        print()

    for ind, series in df2.iterrows():
        print('Indice: ', ind)
        print('Series: ', series)
        print('Nome: ', series['Nome'])
        print('-----------------')

    for coluna in df2.items():
        print(coluna)
        print('------')

    for item in df2.itertuples():
        print(item)
        print('Nome: ', item.Nome)
        print('------')

    def conv_minusulo(x):
        return x.lower()

    print(df2['Nome'].apply(conv_minusulo))

    def calc_idade(x):
        return 2020 - x

    print(df2['Ano_Nasc'].apply(calc_idade))

    df2['Idade'] = df2['Ano_Nasc'].apply(calc_idade)
    print(df2)

    def teste_conteudo(x):
        print(x)
        print('==========')

    df2[['Nome','Curso']].apply(teste_conteudo, axis=1)

    df10 = pd.DataFrame(
        data=np.array(
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
        ),
        columns=['Atr1','Atr2', 'Atr3']
    )

    print(df10)

    def prepocessa(x):
        return x / x.max()

    print(df10.apply(prepocessa, axis=1))

    """
    Parte 2
    https://www.youtube.com/playlist?list=PLAHmHkSA6KkUxN041cFqHGsXD5UFVfANr
    """

    # Manipulando Dados
    ## Adicionando Colunas

    df11 = pd.DataFrame(
        {'Nome': ['Rafael', 'Ricardo', 'Ronaldo'],
         'CPF': ['000.000.000-01', '000.000.000-02', '000.000.000-03'],
         'Abr_Curso': ['SI', 'ADM', 'DIR']}
    )
    print(df11)

    df11['Idade'] = np.random.random_integers(80, size=3) + 18

    df11['Cidade'] = ['Porto Ferreira', 'Jales', 'Rinópolis']

    print(df11)

    print(df11['Idade'].apply(lambda x : 2022 - x))

    df11['Ano_Nascimento'] = df11['Idade'].apply(lambda x : 2022 - x)

    df3['Peso_Medio_CATEGORIA'] = df3['CATEGORIA'].apply(
        lambda x: df3[df3['CATEGORIA'] == x]['Peso'].sum() / len(df3[df3['CATEGORIA'] == x]['Peso'])).round(2)

    df13 = df11.copy()

    df14 = pd.DataFrame({'Média_Limpa':[10.0,8.0,7.5],
                         'Média_Suja': [10.0,7.5,6.0]})

    print(df14)
    print(pd.concat([df13,df14], axis=1))
    df13 = pd.concat([df13,df14], axis=1)

    print(df11)

    df15 = pd.DataFrame({'Abr_Curso':['SI','ADM','DIR','CONT','MED'],
                         'Nome_Curso':['Sistemas de Informação','Administração','Direito','Contabilidade','Medicina']})
    print(df15)

    print(df11.merge(df15,left_on='Abr_Curso', right_on='Abr_Curso'))

    ## Adicionar Linhas
    print(df11)

    df11 = df11.append({'Nome': 'Messi',
                        'CPF': '000.000.000-04',
                        'Abr_Curso': 'MED',
                        'Idade': 35,
                        'Cidade': 'Barcelona',
                        'Ano_Nascimento': 1988}, ignore_index=True)

    df11 = df11.append([{'Nome': 'Firmino',
                         'CPF': '000.000.000-05',
                         'Abr_Curso': 'CONT',
                         'Idade': 45,
                         'Cidade': 'Liverpool'},
                        {'Nome': 'Mané',
                         'CPF': '000.000.000-06',
                         'Abr_Curso': 'DIR',
                         'Idade': 32,
                         'Cidade': 'Liverpool'}], ignore_index=True)

    print(df11)

    df11 = df11.append([pd.Series(['Mané', '000.000.000-07', 'DIR', 32, 'Liverpool', 1985], index=df11.columns),
                        pd.Series(['Salah', '000.000.000-07', 'SI', 33, 'Liverpool', 1989], index=df11.columns)],
                       ignore_index=True)

    print(df11)

    df16 = pd.DataFrame(
        {'Nome': ['Willian','Coutinho'],
         'CPF': ['000.000.000-01','000.000.000-02'],
         'Abr_Curso': ['MED','ADM'],
         'Idade': [29,27],
         'Cidade': ['Londres','Barcelona'],
         'Ano_Nascimento': [1990,1991]}
    )
    print(df16)

    df11 = df11.append(df16)

    print(df11.loc[1])

    print(pd.concat([df11,df16]))

    df11.loc[9] = ['Rafael','000.000.000-01','SI',98,'Porto Ferreira',1924.0]

    print(df11.loc[9])

    ## Substituições
    df11['Idade'] = np.random.randint(22,size=len(df11)) + 18
    # print(df11)

    df11['Ano_Nascimento'] = df11['Idade'].apply(lambda x : 2021 - x)
    print(df11)

    df11.loc[9] = ['Rogério','000.000.000-09','CONT',22,'Jales',1999]
    print(df11)

    df11.iloc[9] = ['Abelardo','000.000.000-10','CONT',22,'Jales',1999]
    print(df11)

    ## Apagando dados

    df17 = df11.copy()

    df17.drop(labels=[0,9], inplace=True)
    print(df17)

    df17.drop(labels=['Ano_Nascimento'], axis=1, inplace=True)
    print(df17)

    df17.drop(index=[1,4], inplace=True)
    print(df17)

    df17.drop(columns=['Abr_Curso','Idade'], inplace=True)
    print(df17)

    selecao = df3['ID_ANIMAL'] <= 50
    print(df3[~selecao])

    df18 = df11.copy()

    del df18['Ano_Nascimento']
    df18 = df18[['Nome','CPF']]
    print(df18)

    # Alterando Índices
    df18['Ano Nascimento'] = np.random.randint(40, size=len(df18)) + 1980
    print(df18)

    df19 = df18.copy()

    df19.reset_index(inplace=True)
    print(df19)

    df19.drop(columns=['index'], inplace=True)
    print(df19)

    df19.index = np.random.randint(100, size=len(df19))
    print(df19)

    df19.index = np.arange(11)
    print(df19)
    print(df19.index)

    df19.index = df19.CPF
    print(df19)

    print(df19.loc['000.000.000-09'])

    print(df18.columns)

    df18.columns = ['Nome','CPF','Ano_Nasc']
    print(df18)

    df18.rename({'CPF':'Cad_Pessoa_Física'}, axis=1, inplace=True)
    print(df18)

    df18.rename({7:17}, axis=0, inplace=True)
    print(df18)

    df18.rename(columns={'Cad_Pessoa_Física':'CPF'}, inplace=True)
    print(df18)

    # Ordenação

    print(df3)
    print(df3.sort_index(axis=1, ascending=True))

    print(df3.sort_values(by=['Peso','Peso_Medio_CATEGORIA'], ascending=(False,True)).head(n=20))

    # Tratando Dados
    print(df3)
    print(df3.sort_values(by=['med1m_NDVI'], na_position='first').head(n=20))

    print(df3.dropna())

    print(df3.dropna(subset=['med1m_NDVI']))

    print(df3.fillna(0))

    print(df3.fillna({'med1m_NDVI':0, 'Med1m_EVI':1}))

    df20 = pd.DataFrame(
        {'Nome':['Rafael', 'Ricardo', 'Alexandre', 'Ronaldo'],
         'Profissão': ['Professor', 'Professor', 'Diretor', 'Professor'],
         'Idade': [34, 36, 50, 35],
         'Salário': [3500, None, 8000, 3600]}
    )

    print(df20)

    print(df20.interpolate(method='nearest'))
    print(df20.interpolate(method='linear'))

    df20 = df20.interpolate(method='nearest')

    df20.loc[4] = ['Rafael','Professor', 34, 3500]
    print(df20)

    print(df20.drop_duplicates())

    df20.loc[4] = ['Rafael', 'Lavador', 34, 5000]
    print(df20)

    print(df20.drop_duplicates(subset=['Nome']))

    print(df20.replace('Rafael', 'Rafael Rodrigues Marquesi'))

    print(df20)

    print(df20.replace(['Professor','Lavador'],'Categoria C'))

    print(df20.replace(regex='D.*', value='Categoria A'))

    # Filtrando Dados

    print(df20[df20['Profissão'].isin(['Professor','Desenvolvedor'])])

    print(df3.filter(regex='AN.*',axis=1))

    df3.index = df3['classificacao']
    print(df3)

    print(df3.filter(regex='^0.*', axis=0))

    print(df3.filter(like='0', axis=0))

    df3.drop(columns='classificacao', inplace=True)
    df3 = df3.reset_index()

    print(df3.filter(items=['Peso','classificacao'], axis=1))

    print(df3['Tipificacao'].unique())

    print(df3['Tipificacao'].value_counts())

    print(df3['Peso'].describe())

    print(df3.describe())

    grupos = df3.groupby(by='Maturidade')
    print(grupos.groups)

    print(df3.loc[grupos.groups['Seis dentes']])

    print(grupos.mean()[['Peso']])

    print(grupos.describe())

    print(grupos.describe()['Peso'])

    grupos2 = df3.groupby(['Maturidade','Acabamento'])

    print(grupos2.groups)

    print(grupos2.describe())