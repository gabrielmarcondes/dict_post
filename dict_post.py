class MeuDicionario:
    def __init__(self):
        self._tamanho = 128
        self._chaves = [None for i in range(128)]
        self._valores = [None for i in range(128)]
    
    def __setitem__(self, chave, valor):
        posicao = hash(chave) % self._tamanho
        self._chaves[posicao] = chave
        self._valores[posicao] = valor

# testes
d = MeuDicionario()
d["chave"] = "valor"
assert d["chave"] == "valor"
assert "chave" in d
assert "valor" in d.values()
for c, v in d.items():
    assert c == "chave"
    assert v == "valor"

