# ed-tsp

Códigos para o Projeto Final da disciplina de Estrutura de Dados e Complexidade de Algoritmos

## Instalação

### Python 3.5

```
  $ pip install -r requirements.txt
```

## Heurísticas de Cosntrução

- Vizinho mais próximo (nearest)
- Aleatório (random)

## Movimentos de Vizinhança

- Swap Method (swap)
- 2-OPT (2opt)
- Variable Neighborhood Descent (vnd)

## Execução

### Uso

```
usage: run.py [-h] [-c {nearest,random}] [-m {swap,2opt,vnd,all}]
              [-i {best,first}]
              [--vnd-methods [{swap,swapbi,swapfi,2opt,2optbi,2optfi} [{swap,swapbi,swapfi,2opt,2optbi,2optfi} ...]]]
              [-p] [-a]
              instance

positional arguments:
  instance              File with instances

optional arguments:
  -h, --help            show this help message and exit
  -c {nearest,random}, --construction {nearest,random}
                        Construction heuristic
  -m {swap,2opt,vnd,all}, --method {swap,2opt,vnd,all}
                        Heuristic approach
  -i {best,first}, --improvement {best,first}
                        Type of improvement choice
  --vnd-methods [{swap,swapbi,swapfi,2opt,2optbi,2optfi} [{swap,swapbi,swapfi,2opt,2optbi,2optfi} ...]]
                        Sequence of the methods used in VND approach
  -p, --plot            Plot the result
  -a, --animate         Animated plot
```

### Exemplos

#### Usando o método de 'Swap Method' com Best Improvement

```
  $ python run.py instancias/instancias_teste/bayg29.txt -m swap -i best
```

### Usando a método de '2-OPT Method' com First Improvement

```
  $ python run.py instancias/instancias_teste/bayg29.txt -m 2opt -i best
```

### Usando a método de 'Variable Neighborhood Descent'

```
  $ python run.py instancias/instancias_teste/bayg29.txt -c nearest -m vnd --vnd-methods swapbi 2optfi
```

### Usando todos os métodos

```
  $ python run.py instancias/instancias_teste/bayg29.txt --construction nearest --method all
```

### Executando com plot e animação

```
  $ python run.py instancias/instancias_teste/swiss42.txt --construction random --method vnd --vnd-methods swap 2opt --animate --plot
```

Corrigir complexidade da vizinhança
VND

GRASP ou VNS
