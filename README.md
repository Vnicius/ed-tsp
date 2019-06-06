# ed-tsp

Códigos para o Projeto Final da disciplina de Estrutura de Dados e Complexidade de Algoritmos

## Instalação

```
  $ pip install -r requirements.txt
```

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
usage: run.py [-h] [-c {nearest,random}] [-m {bi,fi,random,vnd,all}]
              [-l LIMIT] [-p] [-a]
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
  -p, --plot            Plot the result
  -a, --animate         Animated plot
```

### Exemplos

#### Usando o método de 'Best Improvement Method'

```
  $ python run.py instancias/instancias_teste/bayg29.txt -m bi
```

### Usando a método de 'First Improvement Method'

```
  $ python run.py instancias/instancias_teste/bayg29.txt -m fi
```

### Usando a método de 'First Improvement Method'

```
  $ python run.py instancias/instancias_teste/bayg29.txt -c nearest -m vnd
```

### Usando todos os métodos

```
  $ python run.py instancias/instancias_teste/bayg29.txt --construction nearest --method all --limit 10
```

### Executando com plot e animação

```
  $ python run.py instancias/instancias_teste/swiss42.txt --construction random --method bi --animate --plot
```
