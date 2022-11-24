import sys
import time
sys.path.insert(0, "./src")

from get_grammar import read_grammar


# Crea un arbol de nodos para cada no-terminal con respecto a la palabra en la oracion


class Node:
    def __init__(self, nonterm=None, start=None, end=None, word=None, left_node=None, right_Node=None, probability=0):
        self.nonterm = nonterm
        self.start_phrase = start
        self.end_phrase = end
        self.word = word
        self.left = left_node
        self.right = right_Node
        self.prob = probability

# Crea una matriz de nodos de NxN


def create_matrix(n):
    return [[Node() for _ in range(n)] for _ in range(n)]


'''
Estructura de datos de tres índices para permitir el almacenamiento y la recuperación de nodos utilizados en el análisis de oraciones.
Representa el árbol de análisis CYK ascendente de la oración.
'''


class Chart:
    # Mapa que almacena cada no terminal de la oración, utilizado para recuperar y configurar el árbol para cada palabra
    data = {}
    # Inicializa el gráfico con una matriz NxN vacía que almacena el árbol CYK-Parse de la oración
    start = time.time()


    def __init__(self, nonterms):
        n = len(nonterms)
        for k in ["Noun", "Verb", "Prep"]:
            self.data[k] = create_matrix(n)
        for nonterm in nonterms:
            self.data[nonterm.p_nont] = create_matrix(n)

    # Permite la indexación de 3 de la estructura de datos, anula el operador []
    def __getitem__(self, key):
        nonterminal_pos, first_index, second_index = key
        return self.data[nonterminal_pos][first_index][second_index]

    # Permite la indexación de 3 de la estructura de datos, anula el operador []
    def __setitem__(self, key, value):
        nonterminal_pos, first_index, second_index = key
        self.data[nonterminal_pos][first_index][second_index] = value

    # Imprime el gráfico, llama al método recursivo `display` en el nodo superior CYK-Parse Tree, S.
    # Muestra la estructura de árbol de la oración analizada, junto con la probabilidad del análisis de la oración.
    def printChart(self, end):
        tree = self.data["S"][0][end-1]
        if tree.left == None and tree.right == None:
            print("No puede ser parseada.")
        else:
            self.display(tree)
        #print("Probability = ", format(tree.prob))

    def display(self, tree, indent=0):
        if tree != None:
            for i in range(indent):
                print(" ", end='')
            print(tree.nonterm, end=' ')
            if tree.word != None:
                print(tree.word, end=' ')
            print()
            self.display(tree.left, indent+3)
            self.display(tree.right, indent+3)

    end = time.time()
    print(end - start)


'''
    
Analiza una oración en Chomsky-Normal usando el algoritmo CYK-Parse, basado en una gramática dada.
'''


def cyk_parse(sentence, grammar):
    # Divide la oración en una lista de palabras.
    words_in_sentence = sentence.strip().lower().split()
    P = Chart(grammar.get_rules())  # crea una tabla para cada oracion
    n = len(words_in_sentence)

    # Rellena el gráfico con nodos de árbol que representen los árboles posibles para cada palabra
    for i, word in enumerate(words_in_sentence):
        for wrule in grammar.word_rules:
            if wrule.p_nont != word:
                continue
            else:
                P[wrule.pos, i, i] = Node(
                    wrule.pos, i, i, word, None, None, wrule.prob)

    '''
Bucles O (N ^ 3) veces calculando la probabilidad máxima de cada palabra en la oración en función de su creación previa
    árbol y calcula la probabilidad del significado de la oración en general.
    '''
    for length in range(1, n):
        for i in range(n-length):
            j = i + length  # type: int
            for nonterm in grammar.get_rules():
                P[nonterm.p_nont, i, j] = Node(
                    nonterm.p_nont, i, j, None, None, None, 0)
                for k in range(i, j):
                    for nrule in grammar.nonterminal_rules:
                        new_prob = P[nrule.fnonterm, i, k].prob * \
                            P[nrule.snonterm, k+1, j].prob * nrule.prob
                        if new_prob > P[nonterm.p_nont, i, j].prob:
                            P[nonterm.p_nont, i, j].left = P[nrule.fnonterm, i, k]
                            P[nonterm.p_nont, i, j].right = P[nrule.snonterm, k+1, j]
                            P[nonterm.p_nont, i, j].prob = new_prob

    return (P, n)


if __name__ == "__main__":
    grammar = read_grammar()  # Lee y analiza la gramática del archivo.
    with open("input/cyk_sentences.txt", "r") as fp:
        for line in fp:
            parse_chart, num_words = cyk_parse(line, grammar)
            print("Oracion: %s\nParse Tree: " % line)
            parse_chart.printChart(num_words)
            print("-------------------------------------------------------------------\n")
