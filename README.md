# ed-tsp

Códigos para o Projeto Final da disciplina de Estrutura de Dados e Complexidade de Algoritmos

## Heurísticas de Cosntrução

- Vizinho mais próximo (nearest)
- Aleatório (random)

## Movimentos de Vizinhança

- Best Improvement Method (bi)
- First Improvment Method (fi)
- Random Descent (random)
- Variable Neighborhood Descent (vnd)

## Execução

### Uso

```
usage: main.py [-h] [-c {nearest,random}] [-m {bi,fi,random,vnd,all}]
               [-l LIMIT]
               instance

positional arguments:
  instance              File with instances

optional arguments:
  -h, --help            show this help message and exit
  -c {nearest,random}, --construction {nearest,random}
                        Construction heuristic
  -m {bi,fi,random,vnd,all}, --method {bi,fi,random,vnd,all}
                        Heuristic method
  -l LIMIT, --limit LIMIT
                        Limit for random and vnd methods
```

### Exemplos

```
  $ python main.py instancias/instancias_teste/bayg29.txt -m bi
```

```
  $ python main.py instancias/instancias_teste/bayg29.txt -m fi
```

```
  $ python main.py instancias/instancias_teste/bayg29.txt -m random -l 5
```

```
  $ python main.py instancias/instancias_teste/bayg29.txt -m vnd -l 10
```

```
  $ python main.py instancias/instancias_teste/bayg29.txt -m all -l 10 -c nearest
```
