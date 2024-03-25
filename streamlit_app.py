import streamlit as st
import string
import tree_main

def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()
        text = ''.join(char for char in text if char not in string.punctuation)
        words = text.split()
        filtered_words = [word for word in words if word not in words_to_remove]
        return filtered_words

# Define o caminho do arquivo a ser processado
BookQuincas = 'Quincas.txt'

# Lista de palavras a serem removidas
words_to_remove = set(["e", "ou", "mas", "a", "o"])

# Processa o arquivo de texto e obtém uma lista de palavras filtradas
filtered_words = process_text_file(BookQuincas)

# Inicializa a árvore AVL
avl_tree = tree_main.AVLTree()

# Preenche a árvore com as palavras filtradas
for word in filtered_words:
    avl_tree.add(word)

# Função para contar as palavras com um determinado prefixo
def count_words_with_prefix(prefix):
    repetition_counter = {}
    for word in filtered_words:
        if word.startswith(prefix):
            if word not in repetition_counter:
                repetition_counter[word] = 1
            else:
                repetition_counter[word] += 1
    return repetition_counter

# Título do aplicativo
st.title("Buscador de palavras a partir do prefixo")

# Solicita ao usuário que digite um prefixo
prefix = st.text_input("Digite o prefixo da palavra:", "")

# Exibe o prefixo digitado pelo usuário
if prefix:
    st.write("Prefixo digitado:", prefix)

    # Conta as palavras com o prefixo especificado
    words_with_prefix = count_words_with_prefix(prefix)

    # Exibe as palavras com o prefixo e suas contagens de repetição
    if words_with_prefix:
        st.write("Palavras com o prefixo '{}' e suas contagens de repetição:".format(prefix))
        for word, repetitions in words_with_prefix.items():
            st.write("{}: {}".format(word, repetitions))
    else:
        st.write("Nenhuma palavra encontrada com o prefixo '{}'.".format(prefix))
