class Documento:
    def imprimir(self):
        raise NotImplementedError("Subclase debe implementar este método")

class PDF(Documento):
    def imprimir(self):
        return "Imprimiendo PDF"

class Word(Documento):
    def imprimir(self):
        return "Imprimiendo Word"

def imprimir_documento(doc):
    print(doc.imprimir())

# Usando las clases con polimorfismo
doc_pdf = PDF()
doc_word = Word()

imprimir_documento(doc_pdf)  # Output: Imprimiendo PDF
imprimir_documento(doc_word) # Output: Imprimiendo Word
