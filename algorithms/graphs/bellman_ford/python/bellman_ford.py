"""
-----------------------------------------------------------------------------
Nom du fichier : bellman_ford.py
Auteur        : CAPELLE Gabin (https://github.com/CapelleGab)
Créé le      : 10-06-2025 20:39
Dernière MAJ : 10-06-2025 20:39

Description   : Implémentation de l'algorithme de Bellman-Ford en Python.
-----------------------------------------------------------------------------
"""

def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    return distances

## Test de la fonction bellman_ford
def test_bellman_ford():
    # Exemple de graphe
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    
    # Test 1: Vérifier les distances minimales à partir du sommet 'A'
    distances = bellman_ford(graph, 'A')
    assert distances == {'A': 0, 'B': 1, 'C': 3, 'D': 4}, "❌ Test échoué: distances incorrectes"
    print("✅ Test 1 réussi")

    # Test 2: Vérifier le comportement avec un graphe contenant des arêtes négatives
    graph_negative = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': -3, 'D': 2},
        'C': {'D': 1},
        'D': {}
    }
    distances_negative = bellman_ford(graph_negative, 'A')
    assert distances_negative == {'A': 0, 'B': 1, 'C': -2, 'D': -1}, "❌ Test échoué: distances incorrectes avec arêtes négatives"
    print("✅ Test 2 réussi")

    # Test 3: Vérifier le comportement avec un graphe déconnecté
    graph_disconnected = {
        'A': {'B': 1},
        'B': {},
        'C': {'D': 2},
        'D': {}
    }
    distances_disconnected = bellman_ford(graph_disconnected, 'A')
    assert distances_disconnected == {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')}, "❌ Test échoué: distances incorrectes pour graphe déconnecté"
    print("✅ Test 3 réussi")
    
test_bellman_ford()