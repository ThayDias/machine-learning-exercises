
matriz = [ [0, 1, 2],
           [3, 4, 5],
           [6, 7, 8], ]


# Variável onde seu índice representa a posíção no labirinto
# E seu valor representa os possíveis lugares para se mover
nos = [
    [3],
    [4, 2],
    [1],
    [4, 0],
    [7, 5, 1],
    [8, 4, 2]
    [7],
    [6, 4],
    [5] 
]

inicio = 0
final = 8


#Função para testar qual a distância espacial do nó n para o nó final
def retorna_h(destino, node):
    def h(n):
        def caminhar(pos, visitados, distancia):
            caminhos = node[pos]
            distancias = []
            visitados.add(pos)
            if pos == destino:
                return distancia
            distancia += 1
            for novo_pos in caminhos:
                if novo_pos == destino:
                    return distancia
                if not novo_pos in visitados:
                    try:
                        distancias.append( caminhar(novo_pos,set(visitados), distancia) )
                    except:
                        pass
            return min(distancias)


        try:
            return caminhar(n,set(), 0)
        except:
            return None
                    
    return h

meu_h = retorna_h(final, nos)

print( meu_h(0) )

def retorna_caminho(destino, node, meu_h):
    def meu_f(n):
        def calculo_f(pos, g_anterior):
            valor = meu_h(pos)
            if not valor:
                raise Exception('Não há caminho para determinado destino')
            return g_anterior + valor
        pos = n
        g = 0
        path = [pos]
        try:
            while True:
                menor = 999999
                idx_menor = -1
                caminhos = node[pos]
                for caminho in caminhos:
                    if caminho == destino:
                        path.append(caminho)
                        return path
                    if caminho in path:
                        continue
                    heuristica = calculo_f(caminho, g+1)
                    if heuristica < menor:
                        menor = heuristica
                        idx_menor = caminho
                if idx_menor != -1:
                    pos = idx_menor
                    path.append(idx_menor)
                    g += 1
                    continue
                else:
                    break
        except:
            return []
        return path
    return meu_f

calcular_caminho = retorna_caminho(final, nos, meu_h)


texto = ''
caminhos = calcular_caminho(0)
for i in range( len(caminhos) ):
    passagem = caminhos[i]
    if i != 0:
        texto += ' => '
    texto += str(passagem)

print(texto)
