class Caminho:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.previous = None


class Pilha:

    def __init__(self, start: Caminho):
        self.top = start

    def empilhar(self, caminho: Caminho):
        caminho.previous = self.top
        self.top = caminho

    def desempilhar(self):
        assert self.top, "Impossível remover valor de pilha vazia."
        self.top = self.top.previous
