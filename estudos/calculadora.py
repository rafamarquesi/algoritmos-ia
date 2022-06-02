def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide (a, b):
    return a / b

if __name__ == '__main__':
    # print(soma(2,3))
    # print(subtrai(4,3))
    # print(multiplica(5,5))
    # print(divide(3,2))
    import numpy as np
    attr_bd_v1 = np.array(['id_animal', 'EstabelecimentoMunicipio', 'DataAbate', 'Frigorifico_ID',
       'Frigorifico_CNPJ', 'Frigorifico_RazaoSocial', 'Municipio_Frigorifico',
       'Tipificacao', 'Maturidade', 'Acabamento', 'Peso',
       'EstabelecimentoIdentificador', 'Data_homol', 'Questionario_ID',
       'QuestionarioClassificacaoEstabel', 'FERTIRRIGACAO', 'ILP', 'IFP',
       'ILPF', 'CONCEN_VOLUM', 'CREEPFEEDING', 'FORN_ESTRAT_SILAGEM',
       'PROTEICO', 'PROTEICO_ENERGÉTICO', 'RAÇÃO_BAL_CONSUMO_INFERIOR',
       'SAL_MINERAL', 'SALMINERAL_URÉIA', 'RAÇÃO_BAL_CONSUMO_IG',
       'GRÃO_INTEIRO', 'ALTO_CONCENTR_VOLUM', 'ALTO_CONCENTRADO',
       'QuestionarioPossuiOutrosIncentiv', 'QuestionarioFabricaRacao',
       'area so confinamento', 'regua de manejo',
       'boa cobertura vegetal, com baixa', 'erosaoo laminar ou em sulco igua',
       'identificacao individual', 'rastreamento SISBOV', 'Lista Trace', 'BPA',
       'participa de aliancas mercadolog', 'QuestionarioPraticaRecuperacaoPa',
       'Confinamento', 'Suplementacao_a_campo', 'SemiConfinamento',
       'tot1m_Chuva', 'med1m_TempInst', 'med1m_UmidInst', 'med1m_formITUinst',
       'med1m_NDVI', 'med1m_EVI', 'med1m_preR_soja', 'med1m_preR_milho',
       'med1m_preR_boi', 'tot3m_Chuva', 'med3m_TempInst', 'med3m_UmidInst',
       'med3m_formITUinst', 'med3m_NDVI', 'med3m_EVI', 'med3m_preR_soja',
       'med3m_preR_milho', 'med3m_preR_boi', 'tot6m_Chuva', 'med6m_TempInst',
       'med6m_UmidInst', 'med6m_formITUinst', 'med6m_NDVI', 'med6m_EVI',
       'med6m_preR_soja', 'med6m_preR_milho', 'med6m_preR_boi', 'tot12m_Chuva',
       'med12m_TempInst', 'med12m_UmidInst', 'med12m_formITUinst',
       'med12m_NDVI', 'med12m_EVI', 'med12m_preR_soja', 'med12m_preR_milho',
       'med12m_preR_boi', 'cnt1m_CL_ITUinst', 'cnt3m_CL_ITUinst',
       'cnt6m_CL_ITUinst', 'cnt12m_CL_ITUinst', 'ANO', 'CATEGORIA',
       'Classificado?', 'classificacao2', 'Motivo'])
    attr_bd_v2 = np.array(['ID_ANIMAL', 'EstabelecimentoMunicipio', 'DataAbate', 'Frigorifico_ID', 'Frigorifico_CNPJ',
        'Frigorifico_RazaoSocial', 'Municipio_Frigorifico', 'Tipificacao', 'Maturidade', 'Acabamento', 'Peso',
        'EstabelecimentoIdentificador', 'Data_homol', 'Questionario_ID', 'QuestionarioClassificacaoEstabel',
        'FERTIIRRIGACAO', 'ILP', 'IFP', 'ILPF', 'CONCEN_VOLUM', 'CREEPFEEDING', 'FORN_ESTRAT_SILAGEM',
        'PROTEICO', 'PROTEICO_ENERGETICO', 'RACAO_BAL_CONS_INFERIOR', 'SAL_MINERAL', 'SALMINERAL_UREIA',
        'RACAOO_BAL_CONSUMO_IG', 'GRAO_INTEIRO', 'ALTO_CONCENTR_VOLUM', 'ALTO_CONCENTRADO',
        'QuestionarioPossuiOutrosIncentiv', 'QuestionarioFabricaRacao', 'area so confinamento',
        'regua de manejo', 'boa cobertura vegetal, com baixa', 'erosaoo laminar ou em sulco igua',
        'identificacao individual', 'rastreamento SISBOV', 'Lista Trace', 'BPA',
        'participa de aliancas mercadolog', 'QuestionarioPraticaRecuperacaoPa', 'Confinamento',
        'Suplementacao_a_campo', 'SemiConfinamento', 'dif_datas', 'DataAbate_6m_ANT', 'data_homol_select',
        'data12m', 'data6m', 'data3m', 'data1m', 'data7d', 'tot7d_Chuva', 'med7d_TempInst', 'med7d_TempMin',
        'med7d_UmidInst', 'med7d_formITUinst', 'med7d_formITUmax', 'med7d_NDVI', 'med7d_EVI',
        'med7d_preR_soja', 'med7d_preR_milho', 'med7d_preR_boi', 'tot1m_Chuva', 'med1m_TempInst',
        'med1m_UmidInst', 'med1m_formITUinst', 'med1m_NDVI', 'med1m_EVI', 'med1m_preR_soja',
        'med1m_preR_milho', 'med1m_preR_boi', 'tot3m_Chuva', 'med3m_TempInst', 'med3m_UmidInst',
        'med3m_formITUinst', 'med3m_formITUmax', 'med3m_NDVI', 'med3m_EVI', 'med3m_preR_soja',
        'med3m_preR_milho', 'med3m_preR_boi', 'tot6m_Chuva', 'med6m_TempInst', 'med6m_UmidInst',
        'med6m_formITUinst', 'med6m_NDVI', 'med6m_EVI', 'med6m_preR_soja', 'med6m_preR_milho',
        'med6m_preR_boi', 'tot12m_Chuva', 'med12m_TempInst', 'med12m_TempMin',
        'med12m_UmidInst', 'med12m_formITUinst', 'med12m_NDVI', 'med12m_EVI', 'med12m_preR_soja',
        'med12m_preR_milho', 'med12m_preR_boi', 'cnt7d_CL_ITUinst', 'cnt1m_CL_ITUinst', 'cnt3m_CL_ITUinst',
        'cnt6m_CL_ITUinst', 'cnt12m_CL_ITUinst', 'ANO', 'CATEGORIA', 'classificacao', 'Motivo'])

    for attr_bd_v2_col in attr_bd_v2:
        col_existe_bd1 = False
        for attr_bd_v1_col in attr_bd_v1:
            if attr_bd_v1_col.upper() == attr_bd_v2_col.upper():
                col_existe_bd1 = True
        if not col_existe_bd1:
            print(attr_bd_v2_col)