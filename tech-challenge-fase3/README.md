# Tech Challenge — Fase 3 | Alfabetização

Projeto de Ciência de Dados voltado à análise e modelagem do resultado de alfabetização, com foco em transformar dados educacionais públicos em inteligência para apoiar decisões e políticas públicas.

## Objetivo

Investigar se informações disponíveis sobre estudantes, contexto escolar e participação na avaliação podem apoiar a classificação do resultado de alfabetização e, principalmente, orientar uma futura rotina de diagnóstico, priorização e acompanhamento de ações educacionais.

> **Importante:** os modelos não substituem a avaliação pedagógica, os professores ou a gestão educacional. Eles devem ser utilizados como instrumentos de apoio à decisão, com validação humana, governança e monitoramento de vieses.

## Estrutura do projeto

```text
tech-challenge-fase3/
├── data/                       # Bases de dados locais — não versionadas
├── notebooks/
│   └── TechChallenge_Fase3.ipynb
├── src/
│   ├── preprocessing/          # Preparação e transformação dos dados
│   ├── modeling/               # Treinamento dos modelos
│   ├── evaluation/             # Métricas e avaliação
│   └── visualization/          # Gráficos e visualizações
├── reports/
│   └── Apresentacao_Executiva_Alfabetizacao.pptx
├── images/                     # Imagens exportadas para documentação
├── requirements.txt
├── README.md
└── .gitignore
```

## Dados utilizados

A base consolidada utilizada no notebook possui:

- **1.048.575 registros**
- **64 variáveis**
- Anos de referência: **2023 e 2024**
- 473.136 registros em 2023
- 575.439 registros em 2024
- 538.755 registros com `alfabetizado = 1`
- 509.820 registros com `alfabetizado = 0`

A chave `ano + id_aluno` não apresentou duplicidades na validação realizada.

O arquivo de dados deve ser colocado localmente em:

```text
data/dataset_alfabetizacao_unificada.csv
```

O arquivo não é versionado pelo Git por meio do `.gitignore`.

## Metodologia

### 1. Validação e exploração

Foram realizadas verificações de:

- dimensão da base;
- distribuição temporal;
- valores ausentes;
- duplicidades;
- distribuição da variável-alvo;
- consistência das variáveis categóricas e numéricas.

### 2. Variável-alvo

A variável `alfabetizado` foi utilizada como target.

- `1`: alfabetizado
- `0`: não alfabetizado

### 3. Variáveis utilizadas

As variáveis preditoras utilizadas foram:

- `sigla_uf`
- `serie`
- `rede`
- `presenca`
- `preenchimento_caderno`

Foram removidos identificadores, campos administrativos, variáveis derivadas do resultado e outras informações com potencial de **data leakage**, como proficiência, médias, taxas, proporções de níveis, pesos e metas.

### 4. Separação temporal

- Treino: **2023**
- Teste: **2024**

A separação temporal busca simular um cenário mais próximo da aplicação real, no qual o modelo aprende com dados históricos e é avaliado em um período posterior.

### 5. Modelos

Foram comparados:

- Regressão Logística;
- Random Forest.

O pré-processamento foi organizado com `Pipeline` e `ColumnTransformer`, incluindo imputação, padronização de variáveis numéricas e codificação one-hot de variáveis categóricas.

## Resultados

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC | Average Precision |
|---|---:|---:|---:|---:|---:|---:|
| Regressão Logística | 0,666 | 0,630 | 0,874 | 0,732 | 0,712 | 0,686 |
| Random Forest | 0,667 | 0,634 | 0,859 | 0,729 | 0,713 | 0,688 |

O Random Forest apresentou desempenho ligeiramente superior em accuracy, ROC AUC e average precision. A Regressão Logística apresentou maior recall para a classe positiva.

### Interpretação executiva

Os resultados indicam capacidade preditiva **moderada**, ainda insuficiente para decisões automáticas individuais. O principal valor da solução está em apoiar:

1. diagnóstico territorial e escolar;
2. priorização de análises;
3. direcionamento de ações de acompanhamento;
4. monitoramento de resultados ao longo do tempo.

Para uma política pública orientada a identificar estudantes em risco de **não alfabetização**, recomenda-se avaliar explicitamente a classe `0`, recalculando as métricas e, se necessário, redefinindo o target para que o risco seja a classe positiva.

## Como executar

```bash
git clone <URL_DO_REPOSITORIO>
cd tech-challenge-fase3

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
jupyter notebook notebooks/TechChallenge_Fase3.ipynb
```

Depois, disponibilize a base em `data/dataset_alfabetizacao_unificada.csv` e execute as células do notebook em ordem.

## Entregáveis

- Notebook completo com exploração, preparação, modelagem e avaliação.
- Apresentação executiva em PowerPoint.
- Estrutura inicial para evolução do notebook em módulos Python.
- Documentação de metodologia, resultados, limitações e aplicação estratégica.

## Limitações

- A base contém somente os anos de 2023 e 2024.
- O conjunto de variáveis preditoras é restrito.
- O desempenho não deve ser interpretado como diagnóstico pedagógico individual.
- A utilização em políticas públicas exige validação externa, análise de equidade, explicabilidade e monitoramento de drift.
- A métrica de recall apresentada refere-se à classe positiva `alfabetizado = 1`; ela não representa diretamente a capacidade de identificar estudantes não alfabetizados.

## Próximos passos

- Recalcular métricas com foco na classe `não alfabetizado`.
- Testar novos atributos contextuais disponíveis antes da avaliação.
- Avaliar calibração das probabilidades.
- Criar análise de importância e explicabilidade.
- Validar desempenho por UF, rede, série e grupos de interesse.
- Construir um piloto com gestores educacionais.
- Monitorar impacto real das intervenções, não apenas métricas preditivas.

## Apresentação executiva

O arquivo `reports/Apresentacao_Executiva_Alfabetizacao.pptx` simula uma reunião com gestores públicos e apresenta:

- o problema educacional;
- os principais insights;
- o valor estratégico da solução;
- aplicações possíveis em políticas públicas;
- recomendações para um piloto responsável.


## Notebooks disponíveis

- `notebooks/TechChallenge_Fase3_original.ipynb`: versão analítica original, preservada para rastreabilidade.
- `notebooks/TechChallenge_Fase3_modular.ipynb`: versão enxuta que importa as funções de `src/`.

## Fluxo modular

1. `src/preprocessing/pipeline.py`: leitura, conversão de tipos, separação temporal e pré-processamento.
2. `src/modeling/models.py`: definição e treinamento dos modelos.
3. `src/evaluation/metrics.py`: cálculo das métricas e matrizes de confusão.
4. `src/visualization/plots.py`: geração dos gráficos.

O notebook modular deve ser executado a partir da pasta `notebooks/`, com a base salva em `data/dataset_alfabetizacao_unificada.csv`.
