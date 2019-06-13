import os

instances = {'bayg29': 1610, 'bays29': 2020, 'berlin52': 7542, 'bier127': 118282,
             'brazil58': 25395, 'ch130': 6110, 'ch150': 6528, 'swiss42': 1273}

tsp = {'tsp1': 224726, 'tsp2': 69495, 'tsp3': 25181}

methods = ['swap', '2opt', 'vnd', 'vns', 'grasp']
constructions = ['nearest', 'random']

if not os.path.exists('tables'):
    os.mkdir('tables')

# Instancias de teste
for method in methods:
    with open(f'{os.path.join("tables",method)}.csv', 'w', encoding='utf-8') as table:
        table.write(
            'instancia, otimo, media_solucao, melhor_solucao, media_tempo, gap\n')

    for instance in instances:

        print(f'{method} << {instance}')

        os.system(
            f'python run.py instancias/instancias_teste/{instance}.txt -c nearest -m {method} -o {instances[instance]} -n 5 >> {os.path.join("tables",method)}.csv')

for c in constructions:
    with open(f'{os.path.join("tables", c)}.csv', 'w', encoding='utf-8') as table:
        table.write(
            'instancia, otimo, media_solucao, melhor_solucao, media_tempo, gap\n')

    for instance in instances:
        print(f'{c} << {instance}')
        os.system(
            f'python run.py instancias/instancias_teste/{instance}.txt -c {c} -m all -o {instances[instance]} >> {os.path.join("tables", c)}.csv')


# instancias tsp cup
for method in methods:
    for instance in tsp:
        print(f'{method} << {instance}')

        os.system(
            f'python run.py instancias/instancias_tsp_cup/{instance}.txt -c nearest -m {method} -o {tsp[instance]} -n 5 >> {os.path.join("tables",method)}.csv')

for c in constructions:
    for instance in tsp:
        print(f'{c} << {instance}')
        os.system(
            f'python run.py instancias/instancias_teste/{instance}.txt -c {c} -m all -o {tsp[instance]} >> {os.path.join("tables", c)}.csv')
