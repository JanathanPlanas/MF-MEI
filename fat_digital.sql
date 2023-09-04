-- DECLARE @HORA_PROD_PA_META INT = 40200;
-- DECLARE @VALOR_PA INT = 8265;

WITH Subquery AS (
    SELECT 
        [Data],
        SUM([Tempo_logado]) AS TEMP_LOGADO_TOTAL,
        SUM([Tempo_logado]) AS TEMP_PRODUTIVO_REALIZADO,
        CASE 
            WHEN [Data] BETWEEN '2023-07-01' AND '2023-07-28' THEN 36
            ELSE 105
        END AS PA_META
    FROM [Meireles_freitas].[dbo].[TemposAgente]
    WHERE (
        DATA BETWEEN '2023-07-01'
            AND DATEADD(day, - 1, GETDATE())
        )
        AND Agente != 'Homologação'
    GROUP BY [Data]
)

SELECT 
    S.[Data],
    S.TEMP_LOGADO_TOTAL,
    S.TEMP_PRODUTIVO_REALIZADO,
    S.PA_META,
    43200 AS HORA_PROD_PA_META,
    365 AS VALOR_PA,
    S.PA_META * 43200  AS TEMP_PRODUTIVO_META,
    ROUND(S.TEMP_PRODUTIVO_REALIZADO / 43200, 2) AS PA_PRODUTIVO_REALIZADO
FROM Subquery AS S
ORDER BY S.[Data];




DECLARE @HORA_PROD_PA_META INT = 43200;
DECLARE @VALOR_PA INT = 365;

SELECT 
    S.[Data],
    S.TEMP_LOGADO_TOTAL,
    S.TEMP_PRODUTIVO_REALIZADO,
    S.PA_META,
    43200 AS HORA_PROD_PA_META,  --12 hrs o tempo logado 45600
    365 AS VALOR_PA,
    S.PA_META * 43200  AS TEMP_PRODUTIVO_META,
    ROUND(S.TEMP_PRODUTIVO_REALIZADO / 43200, 2) AS PA_PRODUTIVO_REALIZADO
FROM (
    SELECT 
        [Data],
        SUM([Tempo_logado]) AS TEMP_LOGADO_TOTAL,
        SUM([Tempo_falado]) AS TEMP_PRODUTIVO_REALIZADO,
        CASE 
            WHEN [Data] BETWEEN '2023-07-01' AND '2023-07-28' THEN 36
            ELSE 105
        END AS PA_META
    FROM [Meireles_freitas].[dbo].[TemposAgente]
    WHERE (
        DATA BETWEEN '2023-07-01'
            AND DATEADD(day, - 1, GETDATE())
        )
        AND Agente != 'Homologação'
    GROUP BY [Data]
) AS S
ORDER BY S.[Data];





DECLARE @SUBquery TABLE (
    DATA date , 
    TEMP_LOGADO_TOTAL INT ,
    TEMP_PRODUTIVO_REALIZADO INT ,
    PA_META INT
)

INSERT INTO @SUBquery
SELECT 
    [Data],
    SUM([Tempo_logado]) AS TEMP_LOGADO_TOTAL,
    SUM([Tempo_falado]) AS TEMP_PRODUTIVO_REALIZADO,
    CASE 
        WHEN [Data] BETWEEN '2023-07-01' AND '2023-07-28' THEN 36
        ELSE 105
    END AS PA_META
FROM [Meireles_freitas].[dbo].[TemposAgente]
WHERE (
    DATA BETWEEN '2023-07-01'
        AND DATEADD(day, - 1, GETDATE())
    )
    AND Agente != 'Homologação'
GROUP BY [Data]

SELECT 
    S.DATA,
    S.TEMP_LOGADO_TOTAL,
    S.TEMP_PRODUTIVO_REALIZADO,
    S.PA_META,
    43200 AS HORA_PROD_PA_META,  -- 12 hrs o tempo logado 45600
    365 AS VALOR_PA,
    S.PA_META * 43200 AS TEMP_PRODUTIVO_META,
    ROUND(CAST(S.TEMP_PRODUTIVO_REALIZADO AS FLOAT) / 43200, 2) AS PA_PRODUTIVO_REALIZADO
FROM @SUBquery AS S;
