# Graphes (Graphs) — Algorithmes de théorie des graphes

Ce dossier regroupe plusieurs algorithmes classiques de la théorie des graphes.  
Les graphes sont des structures de données fondamentales en informatique, représentant des relations entre des objets (nœuds/sommets) via des connexions (arêtes/arcs).

---

## Algorithmes présents

- **A\* (A Star)**  
  Algorithme de recherche de chemin avec heuristique, très utilisé en intelligence artificielle et en jeux vidéo.

- **BFS (Breadth-First Search)**  
  Parcours en largeur, explore niveau par niveau tous les nœuds d'un graphe.

- **DFS (Depth-First Search)**  
  Parcours en profondeur, explore un chemin jusqu'au bout avant de revenir en arrière.

- **Bellman-Ford**  
  Trouve les plus courts chemins depuis un sommet source, gère les poids négatifs.

  [Python](./bellman_ford/python/bellman_ford.py), [Typescript](./bellman_ford/typescript/bellman_ford.ts)

- **Dijkstra**  
  Algorithme efficace pour trouver le plus court chemin dans un graphe à poids positifs.

- **Floyd-Warshall**  
  Calcule les plus courts chemins entre toutes les paires de sommets.

- **Kosaraju**  
  Trouve les composantes fortement connexes dans un graphe orienté.

- **Kruskal**  
  Construit un arbre couvrant de poids minimum.

- **Prim**  
  Alternative à Kruskal pour construire un arbre couvrant de poids minimum.

- **Tarjan**  
  Trouve les composantes fortement connexes, plus efficace que Kosaraju.

- **Tri Topologique**  
  Ordonne les sommets d'un graphe orienté acyclique selon leurs dépendances.

---

## Applications courantes

- Navigation GPS et routage
- Réseaux sociaux
- Optimisation de réseaux (télécommunications, transport)
- Intelligence artificielle et jeux
- Analyse de dépendances dans les logiciels
- Planification de projets

---

Chaque algorithme est implémenté dans plusieurs langages, avec ses propres tests unitaires pour garantir la fiabilité.

N'hésitez pas à contribuer ou à poser des questions !

---

## Licence

Ce projet est sous licence MIT.
