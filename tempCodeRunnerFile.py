import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master(
    "local[1]").appName('Tma_Tme_Digital').getOrCreate()
df = spark.read.csv("01- Código.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("View")


# Consulta SQL usando o DataFrame df
resultado = spark.sql("""
    SELECT
        Data,
        Campanha,
        Segmento,
        SUM(Tempo_logado) AS Tempo_logado,
        SUM(Tempo_falado) AS Tempo_falado,
        SUM(Chamadas_atendidas) AS Chamadas_atendidas,
        SUM(TMA) AS TMA,
        SUM(IDLE) AS IDLE,
        COUNT(*) AS QTD
    FROM View
    WHERE Agente != 'Homologação' AND Data BETWEEN '2023-07-01' AND DATEADD(DAY, -1, CURRENT_DATE())
    GROUP BY Data, Campanha, Segmento
    HAVING SUM(IDLE) > 0
    ORDER BY 1 DESC
""")

# Exibir o resultado
resultado.show()
