import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

acidentes = pd.read_csv(
    "acidentes2017.csv",
    sep=';',header=None, names=["tipo","situacao","data","hora","bairro","endereco","numero","complemento","natureza","descricao","auto","moto","ciclom","ciclista","pedestre","onibus","caminhao","viatura","outros","vitimas","vitimasfatais"])

# acidentes['tipo'].value_counts().plot(kind='barh')
# plt.show()
crossAcidentesBairro = pd.crosstab(acidentes['bairro'], acidentes['tipo'])
crossAcidentesBairro['total'] = crossAcidentesBairro.sum(axis=1)

crossSimples = crossAcidentesBairro

print crossSimples.head()