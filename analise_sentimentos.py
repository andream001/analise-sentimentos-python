from textblob import TextBlob
import pandas as pd
import plotly.express as px
import os

# Definir caminhos (melhor para organização)
PASTA_DADOS = 'dados'
PASTA_RESULTADOS = 'resultados'
NOME_FICHEIRO_ENTRADA = 'avaliacoes_exemplo.csv'
NOME_FICHEIRO_SAIDA_CSV = 'avaliacoes_com_sentimento.csv'
NOME_FICHEIRO_SAIDA_GRAFICO = 'grafico_sentimentos.html'

# Garantir que a pasta de resultados exista
if not os.path.exists(PASTA_RESULTADOS):
    os.makedirs(PASTA_RESULTADOS)

def analisar_sentimento(texto):
    """Analisa o sentimento de um texto e retorna a polaridade e a classificação."""
    # Traduzir para inglês antes da análise pode melhorar a precisão da TextBlob,
    # mas para simplificar, vamos analisar diretamente.
    # Se o texto não for string, converte para string.
    if not isinstance(texto, str):
        texto = str(texto)
        
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    
    if polaridade > 0.1: # Ajuste este limiar conforme necessário
        return polaridade, 'Positivo'
    elif polaridade < -0.1: # Ajuste este limiar conforme necessário
        return polaridade, 'Negativo'
    else:
        return polaridade, 'Neutro'

def main():
    print(f"Iniciando análise de sentimentos...")
    # Carregar os dados
    caminho_entrada = os.path.join(PASTA_DADOS, NOME_FICHEIRO_ENTRADA)
    try:
        df_avaliacoes = pd.read_csv(caminho_entrada)
        print(f"Dados carregados de '{caminho_entrada}' com sucesso.")
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{caminho_entrada}' não foi encontrado. Verifique o caminho e o nome do ficheiro.")
        return
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return

    if 'texto_avaliacao' not in df_avaliacoes.columns:
        print(f"Erro: A coluna 'texto_avaliacao' não foi encontrada no CSV. Colunas disponíveis: {df_avaliacoes.columns.tolist()}")
        return

    # Aplicar a análise de sentimento
    # Usamos .astype(str) para garantir que todos os dados na coluna são strings e tratar NaNs
    resultados_sentimento = df_avaliacoes['texto_avaliacao'].fillna('').astype(str).apply(lambda texto: analisar_sentimento(texto))
    
    df_avaliacoes['polaridade'] = [res[0] for res in resultados_sentimento]
    df_avaliacoes['sentimento_classificado'] = [res[1] for res in resultados_sentimento]

    print("\nAnálise de Sentimentos Concluída (primeiras 5 linhas):")
    print(df_avaliacoes[['texto_avaliacao', 'polaridade', 'sentimento_classificado']].head())

    # Salvar o DataFrame com os resultados
    caminho_saida_csv = os.path.join(PASTA_RESULTADOS, NOME_FICHEIRO_SAIDA_CSV)
    df_avaliacoes.to_csv(caminho_saida_csv, index=False)
    print(f"\nResultados salvos em '{caminho_saida_csv}'")

    # Gerar e salvar o gráfico interativo com Plotly
    contagem_sentimentos = df_avaliacoes['sentimento_classificado'].value_counts().reset_index()
    # Renomeando as colunas de forma segura
    contagem_sentimentos.columns = ['sentimento_classificado', 'contagem']
    
    fig = px.bar(contagem_sentimentos, 
                 x='sentimento_classificado', 
                 y='contagem', 
                 color='sentimento_classificado',
                 labels={'sentimento_classificado': 'Sentimento', 'contagem': 'Número de Avaliações'},
                 title='Distribuição de Sentimentos das Avaliações')
    
    caminho_saida_grafico = os.path.join(PASTA_RESULTADOS, NOME_FICHEIRO_SAIDA_GRAFICO)
    fig.write_html(caminho_saida_grafico)
    print(f"Gráfico interativo salvo em '{caminho_saida_grafico}'")

    # Exibir resumo no console
    print("\nResumo dos Sentimentos:")
    print(contagem_sentimentos)
    print(f"\nScript finalizado com sucesso!")

if __name__ == '__main__':
    main()