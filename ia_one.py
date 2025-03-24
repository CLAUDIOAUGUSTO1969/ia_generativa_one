import torch
from transformers import pipeline

# Passo 1: Carregar o modelo de IA Generativa
print("Carregando o modelo...")
text_generator = pipeline("text-generation", model="gpt2")
print("Modelo carregado com sucesso!")

# Passo 2: Função para gerar texto
def gerar_texto(prompt, max_length=100):
    print("Gerando texto...")
    resultado = text_generator(prompt, max_length=max_length, num_return_sequences=1)
    return resultado[0]['generated_text']

# Passo 3: Entrada do usuário
if __name__ == "__main__":
    prompt = input("Digite um texto para a IA continuar: ")
    texto_gerado = gerar_texto(prompt)
    print("\nTexto Gerado:")
    print(texto_gerado)