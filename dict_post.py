class MeuDicionario:
    def __init__(self, tamanho_inicial=128):
        self._tamanho = tamanho_inicial
        self._ocupacao = 0
        self._chaves = [[] for i in range(self._tamanho)]
        self._valores = [[] for i in range(self._tamanho)]
        
    def _expandir(self):
        pares_existentes = list(self.items())
        self._tamanho = int(1.5 * self._tamanho)
        self._chaves = [[] for i in range(self._tamanho)]
        self._valores = [[] for i in range(self._tamanho)]
        for chave, valor in pares_existentes:
            self[chave] = valor
    
    def __setitem__(self, chave, valor):
        if self._ocupacao / self._tamanho > 0.3:
            self._expandir()        
        posicao = hash(chave) % self._tamanho
        self._chaves[posicao].append(chave)
        self._valores[posicao].append(valor)
        self._ocupacao += 1
    
    def __getitem__(self, chave):
        posicao = hash(chave) % self._tamanho
        try:
            sub_posicao = self._chaves[posicao].index(chave)
        except ValueError:
            raise KeyError("Chave não Encontrada")
        return self._valores[posicao][sub_posicao]
    
    def __contains__(self, chave):
        posicao = hash(chave) % self._tamanho
        return chave in self._chaves[posicao]
    
    def values(self):
        for valores in self._valores:
            if valores is not None:
                for valor in valores:
                    yield valor

    def items(self):
        for par in zip(self._chaves, self._valores):
            if par[0]:
                for chave, valor in zip(par[0], par[1]):
                    yield chave, valor
        
# testes
d = MeuDicionario(tamanho_inicial=3)
d["chave"] = "valor"
assert d["chave"] == "valor"
assert "chave" in d
assert "valor" in d.values()
for c, v in d.items():
    assert c == "chave"
    assert v == "valor"

d["outra chave"] = "outro valor"
assert d["chave"] == "valor"
assert d["outra chave"] == "outro valor"
assert d._tamanho > 3

try:
    d["chave inexistente"]
except KeyError:
    pass  # exceção esperada!
except Exception:
    raise  # outra exceção, inesperada

print("sucesso!")

