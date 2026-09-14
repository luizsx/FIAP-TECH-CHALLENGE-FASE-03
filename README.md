# FIAP-TECH-CHALLENGE-FASE-03


Esse projeto foi desenvolvido para analisar dados educacionais e entender se algumas informações disponíveis sobre os alunos podem ajudar a identificar padrões relacionados à alfabetização.

A ideia não é substituir professores ou avaliações pedagógicas, mas usar os dados como apoio para identificar cenários, direcionar análises e ajudar na tomada de decisão.

## Objetivo

O principal objetivo foi construir uma primeira solução de análise e modelagem preditiva usando dados de alfabetização.

Durante o projeto, organizei os dados, fiz uma análise exploratória, tratei as variáveis, criei o indicador de alfabetização e treinei modelos de classificação para entender se era possível identificar padrões associados ao resultado dos alunos.

## Estrutura do projeto

```text
tech-challenge-fase3/
├── data/
├── notebooks/
│   ├── TechChallenge_Fase3.ipynb
│   ├── TechChallenge_Fase3_original.ipynb
│   └── TechChallenge_Fase3_modular.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   └── pipeline.py
│   ├── modeling/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── metrics.py
│   └── visualization/
│       ├── __init__.py
│       └── plots.py
├── reports/
│   └── Apresentacao_Executiva_Alfabetizacao.pptx
├── images/
├── requirements.txt
├── README.md
└── .gitignore
```

## Dados utilizados

A base utilizada foi a `dataset_alfabetizacao_unificada.csv`.

***OS DADOS CARREGADOS DENTRO DA PASTA DATA/ SÃO UMA AMOSTRA DEVIDO AO TAMANHO DA BASE FINAL GERADA NA FASE ANTERIOR ***

- AS ANALISES DENTRO DO NOTEBOOK ESTÃO COM A BASE COM A SUA TOTALIDADE

A base possui:

- 1.048.575 registros;
- 64 variáveis;
- 473.136 registros referentes a 2023;
- 575.439 registros referentes a 2024;
- 538.755 registros com `alfabetizado = 1`;
- 509.820 registros com `alfabetizado = 0`.

Também foi feita uma verificação de duplicidade considerando a combinação de `ano` e `id_aluno`. Não foram identificadas duplicidades nessa chave.

## Etapas realizadas

No notebook, foram realizadas as seguintes etapas:

1. Leitura e entendimento da base;
2. Análise exploratória dos dados;
3. Verificação dos tipos das variáveis;
4. Tratamento e padronização dos dados;
5. Auditoria de qualidade;
6. Criação do target de alfabetização;
7. Seleção das variáveis utilizadas nos modelos;
8. Separação temporal entre treino e teste;
9. Treinamento dos modelos;
10. Avaliação das métricas;
11. Análise da importância das variáveis;
12. Construção de ranking municipal;
13. Avaliação de um cenário antecipativo;
14. Análise da matriz de confusão;
15. Avaliação de diferentes thresholds.

## Variável target

A variável utilizada como target foi `alfabetizado`.

Ela representa o resultado de classificação utilizado para treinar os modelos:

- `1`: aluno alfabetizado;
- `0`: aluno não alfabetizado.

É importante destacar que o recall apresentado nas métricas está relacionado à classe positiva, ou seja, à classe `alfabetizado = 1`.

Caso o objetivo seja priorizar alunos com maior risco de não alfabetização, será necessário avaliar especificamente a classe `0` ou redefinir o target para que o modelo tenha como foco a identificação desse risco.

## Variáveis utilizadas

As principais variáveis utilizadas na modelagem foram:

- `sigla_uf`;
- `serie`;
- `rede`;
- `presenca`;
- `preenchimento_caderno`.

Algumas variáveis foram removidas por apresentarem potencial de vazamento de informação, como:

- proficiências;
- médias;
- taxas;
- proporções de níveis;
- pesos;
- metas;
- identificadores.

A ideia foi evitar que o modelo utilizasse informações que poderiam não estar disponíveis no momento em que uma previsão fosse feita.

## Separação entre treino e teste

Foi utilizada uma separação temporal:

- dados de 2023 para treinamento;
- dados de 2024 para teste.

Essa abordagem foi escolhida para deixar a avaliação mais próxima de um cenário real, em que o modelo é treinado com dados históricos e depois utilizado para analisar um período posterior.

## Modelos utilizados

Foram treinados dois modelos de classificação:

- Regressão Logística;
- Random Forest.

A Regressão Logística foi utilizada como modelo mais simples e interpretável.

O Random Forest foi utilizado para comparar o desempenho com um modelo capaz de capturar relações não lineares entre as variáveis.

## Resultados

### Regressão Logística

- Accuracy: 0,665666;
- Precision: 0,629930;
- Recall: 0,873833;
- F1-score: 0,732101;
- ROC AUC: 0,711639;
- Average Precision: 0,685987.

### Random Forest

- Accuracy: 0,666740;
- Precision: 0,633796;
- Recall: 0,858655;
- F1-score: 0,729287;
- ROC AUC: 0,712577;
- Average Precision: 0,687909.

Os dois modelos apresentaram resultados próximos.

O Random Forest teve uma pequena vantagem em accuracy, precision, ROC AUC e average precision. Já a Regressão Logística apresentou recall e F1-score ligeiramente maiores.

Isso mostra que, com as variáveis disponíveis, os modelos conseguem identificar alguns padrões, mas ainda existe espaço para melhorar a capacidade preditiva.

## Interpretação dos resultados

Os resultados devem ser interpretados com cuidado.

O modelo não deve ser entendido como uma avaliação definitiva da aprendizagem de um aluno. Ele funciona como uma ferramenta de apoio para identificar padrões e possíveis cenários de atenção.

Também é importante considerar que as variáveis disponíveis representam apenas parte do contexto educacional. Aspectos pedagógicos, familiares, sociais e regionais podem influenciar o resultado e não estão necessariamente representados na base.

## Como executar

Para executar o projeto, é necessário ter Python instalado e instalar as dependências:

```bash
pip install -r requirements.txt
```

Depois, basta abrir o notebook:

```text
notebooks/TechChallenge_Fase3_modular.ipynb
```

O notebook modular importa as funções organizadas dentro da pasta `src`.

## Notebooks

O projeto possui três versões do notebook:

### `TechChallenge_Fase3.ipynb`

Versão principal utilizada para a análise.

### `TechChallenge_Fase3_original.ipynb`

Cópia do notebook original, mantida como referência.

### `TechChallenge_Fase3_modular.ipynb`

Versão reorganizada, com funções separadas em módulos de:

- pré-processamento;
- modelagem;
- avaliação;
- visualização.

Essa organização facilita a manutenção e permite reaproveitar as funções em outras análises.

## Apresentação

A apresentação executiva está disponível em:

```text
reports/Apresentacao_Executiva_Alfabetizacao.pptx
```

Ela resume o problema, os dados utilizados, a abordagem de modelagem, os resultados e os principais pontos de atenção.

## Limitações

Algumas limitações precisam ser consideradas:

- a base possui informações limitadas sobre o contexto dos alunos;
- o modelo não representa uma avaliação pedagógica completa;
- o target utilizado está relacionado à classificação de alfabetização, mas o objetivo de identificar risco de não alfabetização exige uma análise específica da classe `0`;
- os resultados podem variar conforme novas variáveis sejam incorporadas;
- a separação temporal entre 2023 e 2024 é útil, mas ainda pode ser complementada com outras estratégias de validação;
- os modelos não devem ser utilizados de forma isolada para tomada de decisão sobre alunos ou escolas.

## Próximos passos

Como próximos passos, considero interessante:

- incluir mais variáveis contextuais;
- avaliar modelos com foco na classe de não alfabetizados;
- testar outros algoritmos;
- fazer validação temporal mais robusta;
- analisar a estabilidade dos resultados por estado, rede e município;
- acompanhar a evolução dos indicadores ao longo dos anos;
- criar uma rotina de monitoramento;
- disponibilizar os resultados em um dashboard;
- avaliar como os rankings podem apoiar ações de acompanhamento.

## Conclusão

O projeto mostrou como dados públicos podem ser organizados e utilizados para construir uma primeira solução de apoio à análise educacional.

Mesmo com as limitações atuais, os modelos podem servir como ponto de partida para uma rotina de diagnóstico, priorização e acompanhamento.

A ideia principal é transformar os dados em informação útil para apoiar decisões, sempre considerando a análise humana, o contexto educacional e o impacto das ações na aprendizagem dos alunos.
