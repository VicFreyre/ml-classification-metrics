
# 🐍 Avaliação de Modelos de Classificação: Métricas e Implementação em Python 

## 1. Introdução
A avaliação de modelos de classificação é essencial para medir a qualidade das previsões. Essa análise é baseada na **matriz de confusão**, composta pelos seguintes elementos:

- **Verdadeiros Positivos (VP):** Casos positivos corretamente classificados.
- **Verdadeiros Negativos (VN):** Casos negativos corretamente classificados.
- **Falsos Positivos (FP):** Casos negativos incorretamente previstos como positivos.
- **Falsos Negativos (FN):** Casos positivos incorretamente previstos como negativos.

<img width="1093" height="507" alt="image" src="https://github.com/user-attachments/assets/7a61eb51-d76b-42df-8032-1637a03a042c" />

Execute o modelo pelo [Google Colab](https://colab.research.google.com/drive/1FWQuTgwRWB7lslvNlbtoeCgisOpmLh5R#scrollTo=Tu3UAuvVP3Bb)


---

## 2. Métricas de Avaliação

- **Sensibilidade (Recall):**  
  Proporção de positivos reais corretamente identificados pelo modelo.  
  Sensibilidade = VP / (VP + FN)

- **Especificidade:**  
  Proporção de negativos corretamente identificados.  
  Especificidade = VN / (VN + FP)

- **Acurácia:**  
  Proporção de todas as previsões corretas.  
  Acurácia = (VP + VN) / (VP + VN + FP + FN)

- **Precisão (Precision):**  
  Proporção de previsões positivas que são realmente positivas.  
  Precisão = VP / (VP + FP)

- **F-score:**  
  Média harmônica entre precisão e sensibilidade.  
  F-score = 2 × (Precisão × Sensibilidade) / (Precisão + Sensibilidade)

**Legenda:**  
- `VP` = Verdadeiros Positivos  
- `VN` = Verdadeiros Negativos  
- `FP` = Falsos Positivos  
- `FN` = Falsos Negativos
