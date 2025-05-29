# Análise de Sentimentos de Avaliações de Produtos com Python

![Status do Projeto: Em Desenvolvimento](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Linguagem](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto tem como objetivo realizar uma análise de sentimentos em avaliações textuais de produtos. Utilizando Python e bibliotecas de Processamento de Linguagem Natural (NLP), o script classifica cada avaliação como Positiva, Negativa ou Neutra.

➡️ **Veja este projeto em ação na sua página do GitHub Pages:** [https://andream001.github.io/analise-sentimentos-python/]
---

## 🎯 Visão Geral

Em um mundo cada vez mais digital, entender a opinião dos clientes sobre produtos e serviços é crucial. Este projeto oferece uma ferramenta simples para automatizar a análise de sentimentos em textos de avaliações, fornecendo insights rápidos sobre a percepção geral do público.

---

## ✨ Funcionalidades Principais

* Carrega avaliações de um ficheiro CSV.
* Utiliza a biblioteca **TextBlob** para calcular a polaridade do sentimento de cada avaliação.
* Classifica os sentimentos em: Positivo, Negativo e Neutro.
* Salva as avaliações com a classificação de sentimento e a pontuação de polaridade num novo ficheiro CSV.
* Gera um gráfico de barras interativo (com **Plotly**) mostrando a distribuição dos sentimentos classificados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.7+**
* **TextBlob:** Para a análise de sentimento.
* **Pandas:** Para manipulação e análise de dados tabulares (CSV).
* **Plotly Express:** Para a criação de visualizações de dados interativas.

---

## 🚀 Configuração e Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/andream001/analise-sentimentos-python.git](https://github.com/andream001/analise-sentimentos-python.git)
    cd analise-sentimentos-python
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    # No Linux/macOS:
    source venv/bin/activate
    # No Windows:
    # venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Certifique-se de que o ficheiro `requirements.txt` está atualizado com as bibliotecas listadas acima).*

---

## ▶️ Como Executar

1.  **Prepare seus dados:**
    * Certifique-se de que você tem um ficheiro CSV na pasta `dados/` (por exemplo, `dados/avaliacoes_exemplo.csv`).
    * Este ficheiro deve conter pelo menos uma coluna com os textos das avaliações (o script espera uma coluna chamada `texto_avaliacao` por padrão).

2.  **Execute o script principal:**
    ```bash
    python analise_sentimentos.py
    ```

---

## 📊 Saída Esperada (Resultados)

Após a execução bem-sucedida do script:

1.  **Um novo ficheiro CSV** será criado na pasta `resultados/` (ex: `resultados/avaliacoes_com_sentimento.csv`). Este ficheiro conterá as avaliações originais junto com uma coluna para a pontuação de polaridade e outra para a classificação do sentimento (Positivo, Negativo, Neutro).
2.  **Um ficheiro HTML interativo** com um gráfico de barras será gerado na pasta `resultados/` (ex: `resultados/grafico_sentimentos.html`). Este gráfico mostrará a distribuição dos sentimentos encontrados.
3.  **Um resumo** da contagem de sentimentos será exibido no console.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o ficheiro [LICENSE](LICENSE) para mais detalhes.

---

