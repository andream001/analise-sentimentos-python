import sys
print(f"--- Testando Importação ---")
print(f"Executável Python: {sys.executable}")
print(f"Caminhos de Busca (sys.path):")
for path_item in sys.path:
    print(path_item)

try:
    from textblob import TextBlob
    print("\nSUCESSO! TextBlob importado corretamente.")
    blob = TextBlob("Textblob is working!")
    print(f"Sentimento de teste: {blob.sentiment}")
except ImportError as e:
    print(f"\nERRO AO IMPORTAR: {e}")
except Exception as e:
    print(f"\nOCORREU UM ERRO INESPERADO: {e}")
print(f"--- Fim do Teste ---")