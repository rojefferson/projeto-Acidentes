import numpy as np
import pandas as pd


acidentes = pd.read_csv(
    "acidentes2017.csv",
    sep=';',header=None, names=["tipo","situacao","data","hora","bairro","endereco","numero","complemento","natureza","descricao","auto","moto","ciclom","ciclista","pedestre","onibus","caminhao","viatura","outros","vitimas","vitimasfatais"])




