

# acidentes['tipo'].value_counts().plot(kind='barh')
# plt.show()
#crossAcidentesBairro = pd.crosstab(acidentes['bairro'], acidentes['tipo'])
#crossAcidentesBairro['total'] = crossAcidentesBairro.sum(axis=1)
# crossAcidentesBairro.plot(kind='bar',legend = True)

# plt.show()

# plt.plot([0,10,20,30])
# plt.show()

#select 

#data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

#visão inicial dos dados
#pd.crosstab(data["Credit_History"],data["Loan_Status"],margins=True)

#tamanho da base
#acidentes.shape

#Tipos de Gráficos
 

# ‘line’ : line plot (default)
# ‘bar’ : vertical bar plot
# ‘barh’ : horizontal bar plot
# ‘hist’ : histogram
# ‘box’ : boxplot
# ‘kde’ : Kernel Density Estimation plot
# ‘density’ : same as ‘kde’
# ‘area’ : area plot
# ‘pie’ : pie plot
# ‘scatter’ : scatter plot
# ‘hexbin’ : hexbin plot



#conta os dados 
#print acidentes['situacao'].value_counts()