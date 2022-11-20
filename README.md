# Proyecto CYK usando una CFG para generar el parse-tree

## Gramaticas 

Investigar sobre el algoritmo CYK (Cocke-Younger-Kasami) para realizar el parsing de una gram´atica CFG.
Esta parte del proyecto consiste en implementar el algoritmo CKY para determinar si una frase simple en el idioma ingl´es es parte
de un lenguaje generado por una gram´atica.
La gram´atica que usaremos como ejemplo es la siguiente:
S −→ NP VP
VP −→ VP PP
VP −→ V NP
VP −→ cooks | drinks | eats | cuts
PP −→ P NP
NP −→ Det N
NP −→ he | she
V −→ cooks | drinks | eats | cuts
P −→ in | with
N −→ cat | dog
N −→ beer | cake | juice | meat | soup
N −→ fork | knife | oven | spoon
Det −→ a | the

## Objetivos 

- Implementaci´on del algoritmo CYK.

## Especificaciones 

### Entrada

- Solamente se ingresar´a textualmente una expresi´on sentencia (frase) en el idioma ingl´es w. Por ejemplo, se ingresa la
expresi´on w = She eats a cake with a fork; w = The cat drinks the beer.
- Indique en su reporte ejemplos de frases en el lenguaje, y ejemplos que no est´en en el lenguaje.

### Salida 

- un S´I, si la expresi´on w pertenece al lenguaje descrito por la gram´atica, o un NO en caso contrario.
- Tambi´en se debe indicar el tiempo que se tarda el algoritmo en realizar dicha validaci´on.
- Construir el parse tree de la expresi´on w. (Para ello,

> Nota: El algoritmo CYK requiere que la gram´atica a usar est´e en la Forma Normal de Chomsky. No se olviden de convertir la gram´atica a su Forma Normal de Chomsky, antes de implementar el algoritmo. El algoritmo requiere el uso de programaci´on din´amica. Deber´an investigar en qu´e consiste y c´omo se implementa. Las frases aceptadas son sint´acticamente correctas (nadie garantiza que sean sem´anticamente correctas).