# -*- coding: utf-8 -*-
"""treinamento_spark.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GNnNtfshUSKXOfAufoO0V0aq6me9U6Od

Olá, sou Janatã Aruanda, estudante na área de tecnologia, meu objetivo é me tornar um eng. de dados. 
 
Treinando usando o Spark com python 
está tudo comentando e explicado como cada célula foi excutada 
---

**`arquitetura do Spark (Simples)`**

criado o ambiente no colab
"""

# instalar as dependências
# baixando a versão mais recente do java8;
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
#download via stp do hadoop
!wget -q https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz
#extraindo o arquivo tgz
!tar xf /content/spark-3.3.1-bin-hadoop3.tgz
#instalando o  Findspark que é responsavel para que as variáveis ​​do ambiente sejam definidas corretamente e o pyspark seja importado.
!pip install -q findspark

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"

os.environ["SPARK_HOME"] = "/content/spark-3.3.1-bin-hadoop3"

# utilizando o findspark para que o pyspark seja "importável"
import findspark
findspark.init('spark-3.3.1-bin-hadoop3')

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

"""Carregando os datafermes e visualiizando 

"""

clientes = spark.read.load('/content/dados_atividade/Clientes.parquet')

clientes.show(2)

vendas = spark.read.load('/content/dados_atividade/Vendas.parquet')

vendas.show(2)

"""Fazendo as manipulaçãoes """

#Selecionado as colunas e visualizando 
resultado1 = clientes.select(F.col('Cliente'), F.col('Estado'), F.col('Status'))

#Imprimir o resultado 
resultado1.show()

#Selecionado todas as colunas ('*') e procurando na coluna o valor 
resultado2 = clientes.select('*').where((F.col("Status") == 'Platinum') | (F.col("Status") == 'Gold'))

#Imprimir o resultado 
resultado2.show()

# Pega o ClienteID que estão na duas 'datafarme' unsando o Join, soma o tatal do status e ordena em descrecente. 
resultado3 =  vendas.join(clientes,vendas.ClienteID == clientes.ClienteID).groupBy(clientes.Status)\
.agg(F.sum("Total"))\
.orderBy(F.col("sum(Total)")\
.desc())

resultado3.show()