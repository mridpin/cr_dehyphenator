# How to use
Put the docs you want to dehyphenate in input_docs dir, then run the script. Output will be in output_docs
```
python3 cr_dehyphenator_es-ES.py
```

# DEHYPHENATOR
This script removes hyphens that split words at the end of the lines. Usually words are split like this to keep the text aligned to the right margin, instead of using the word processor "justify" alignment. When doing NLP work on a text, these types of splits incorporate noise to the file, so we are attempting to remove them.

## Rules
1. Last char of the stripped line must be a hyphen "-".
2. Character previous to the hyphen must be alphabetic
3. (WIP) First character of the next line must be alphabetic
4- (WIP) First character of the next line must be non-capitalized, unless the entire word is. This is to prevent dehyphenating hyphenated proper nouns.


# DESGUIONADOR
Este script quita el guion que separa las palabras al final de la línea. Normalmente las palabras se separan así para mantener el texto alineado al margen derecho, en vez de usar el alineamiento "justificado" del procesador de texto. Cuando se hace NLP en un texto, este tipo de separaciones introduce ruido en el documento.

## Reglas
1. El último char de la línea debe ser un guion '-'
2. El char delante del guión debe ser alfabético
3. (WIP) El primer char de la línea deber ser alfabético
4- (WIP) El primer char de la línea siguiente debe ser minúscula excepto si toda la línea es mayúscula. Esto es para prevenir la desguionación de nombres propios

### Example / Ejemplo
"este script me ha sal-
vado la vida"
-->
"este script me ha 
salvado la vida"
