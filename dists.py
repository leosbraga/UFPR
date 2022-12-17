dists = {
    'Bucharest': [
        ('Urzineci',85),
        ('Giurgiu',90),
        ('Pitesti',101),
        ('Fagaras',211)
    ],
    'Giurgiu': [
        ('Bucharest',90)
    ],
    'Urzineci': [
        ('Bucharest',85),
        ('Hirsova',98),
        ('Vaslui',142)
    ],
    'Hirsova': [
        ('Urzineci',98),
        ('Eforie',86)
    ],
    'Eforie': [
        ('Hirsova',86)
    ],
    'Vaslui': [
        ('Urzineci',142),
        ('Iasi',92)
    ],
    'Iasi': [
        ('Vaslui', 92),
        ('Neamt',87)
    ],
    'Neamt': [
        ('Iasi', 87)
    ],
    'Fagaras': [
        ('Bucharest',211),
        ('Sibiu',99)
    ],
    'Pitesti': [
        ('Bucharest',101),
        ('Rimnicu Vilcea',97),
        ('Craiova',138)
    ],
    'Craiova':[
        ('Pitesti',138),
        ('Rimnicu Vilcea',146),
        ('Dobreta',120)
    ],
    'Rimnicu Vilcea':[
        ('Craiova',146),
        ('Pitesti',97),
        ('Sibiu',80)
    ],
    'Sibiu':[
        ('Rimnicu Vilcea',80),
        ('Fagaras',99),
        ('Oradea',151),
        ('Arad',140)
    ],
    'Oradea':[
        ('Sibiu',151),
        ('Zerind',71)
    ],
    'Zerind':[
        ('Oradea',71),
        ('Arad',75)
    ],
    'Arad':[
        ('Zerind',75),
        ('Timisoara',118),
        ('Sibiu',140)
    ],
    'Timisoara':[
        ('Arad',118),
        ('Lugoj',111)
    ],
    'Lugoj':[
        ('Timisoara',111),
        ('Mehadia',70)
    ],
    'Mehadia':[
        ('Lugoj',70),
        ('Dobreta',75)
    ],
    'Dobreta':[
        ('Mehadia',75),
        ('Craiova',120)
    ],
}
"""Aqui eu decidi criar um dicionário com os custos pré-calculados e deixar o script de a_star menor"""
dists_cost = {
    'Bucharest': [
        ('Urzineci',165),
        ('Giurgiu',167),
        ('Pitesti',201),
        ('Fagaras',387)
    ],
    'Giurgiu': [
        ('Bucharest',167)
    ],
    'Urzineci': [
        ('Bucharest',165),
        ('Hirsova',249),
        ('Vaslui',341)
    ],
    'Hirsova': [
        ('Urzineci',178),
        ('Eforie',247)
    ],
    'Eforie': [
        ('Hirsova',273)
    ],
    'Vaslui': [
        ('Urzineci',222),
        ('Iasi',318)
    ],
    'Iasi': [
        ('Vaslui', 291),
        ('Neamt',321)
    ],
    'Neamt': [
        ('Iasi', 353)
    ],
    'Fagaras': [
        ('Bucharest',211),
        ('Sibiu',352)
    ],
    'Pitesti': [
        ('Bucharest',101),
        ('Rimnicu Vilcea',290),
        ('Craiova',298)
    ],
    'Craiova':[
        ('Pitesti',238),
        ('Rimnicu Vilcea',339),
        ('Dobreta',362)
    ],
    'Rimnicu Vilcea':[
        ('Craiova',306),
        ('Pitesti',197),
        ('Sibiu',333)
    ],
    'Sibiu':[
        ('Rimnicu Vilcea',273),
        ('Fagaras',275),
        ('Oradea',531),
        ('Arad',506)
    ],
    'Oradea':[
        ('Sibiu',404),
        ('Zerind',445)
    ],
    'Zerind':[
        ('Oradea',451),
        ('Arad',441)
    ],
    'Arad':[
        ('Zerind',449),
        ('Timisoara',447),
        ('Sibiu',393)
    ],
    'Timisoara':[
        ('Arad',484),
        ('Lugoj',355)
    ],
    'Lugoj':[
        ('Timisoara',440),
        ('Mehadia',311)
    ],
    'Mehadia':[
        ('Lugoj',314),
        ('Dobreta',317)
    ],
    'Dobreta':[
        ('Mehadia',316),
        ('Craiova',280)
    ],
}

dist_euclidiana = {
    'Arad': 366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urzineci':80,
    'Vaslui':199,
    'Zerind':374
}