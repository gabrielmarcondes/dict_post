class MeuDicionario:
    def __init__(self):
        self._tamanho = 128
        self._chaves = [None for i in range(128)]
        self._valores = [None for i in range(128)]
    
    def __setitem__(self, chave, valor):
        posicao = hash(chave) % self._tamanho
        self._chaves[posicao] = chave
        self._valores[posicao] = valor
    
    def __getitem__(self, chave):
        posicao = hash(chave) % self._tamanho
        return self._valores[posicao]
    
    def __contains__(self, chave):
        posicao = hash(chave) % self._tamanho
        return self._chaves[posicao] is not None
    
    def values(self):
        return [valor for valor in self._valores if valor is not None]

    def items(self):
        for par in zip(self._chaves, self._valores):
            if par[0] is not None:
                yield par
        
# testes
d = MeuDicionario()
d["chave"] = "valor"
assert d["chave"] == "valor"
assert "chave" in d
assert "valor" in d.values()
for c, v in d.items():
    assert c == "chave"
    assert v == "valor"

print("sucesso!")

