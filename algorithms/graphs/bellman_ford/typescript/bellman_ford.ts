/*
-----------------------------------------------------------------------------
Nom du fichier : bellman_ford.ts
Auteur        : CAPELLE Gabin (https://github.com/CapelleGab)
Créé le      : 10-06-2025 20:39
Dernière MAJ : 10-06-2025 20:39

Description   : Implémentation de l'algorithme de Bellman-Ford en TypeScript.
-----------------------------------------------------------------------------
*/

const bellman_ford = (Graph: any, start: string) => {
  const distances = {};
  const previous = {};

  for (const vertex of Graph.vertices) {
    distances[vertex] = Infinity;
    previous[vertex] = null;
  }

  distances[start] = 0;

  for (let i = 0; i < Graph.vertices.length - 1; i++) {
    for (const vortex of Graph.vertices) {
      for (const neighbor of Object.keys(Graph.adjacencyList[vortex])) {
        const distance =
          distances[vortex] + Graph.adjacencyList[vortex][neighbor];
        if (distance < distances[neighbor]) {
          distances[neighbor] = distance;
          previous[neighbor] = vortex;
        }
      }
    }
  }
  return { distances, previous };
};

const test_bellman_ford = () => {
  const graph = {
    vertices: ["A", "B", "C", "D"],
    adjacencyList: {
      A: { B: 1, C: 4 },
      B: { C: 2, D: 5 },
      C: { D: 1 },
      D: {},
    },
  };
  const result = bellman_ford(graph, "A");
  console.log(result);

  const graph_negative = {
    vertices: ["A", "B", "C", "D"],
    adjacencyList: {
      A: { B: 1, C: 4 },
      B: { C: -3, D: 2 },
      C: { D: 1 },
      D: {},
    },
  };
  const result_negative = bellman_ford(graph_negative, "A");
  console.log(result_negative);

  const graph_disconnected = {
    vertices: ["A", "B", "C", "D"],
    adjacencyList: {
      A: { B: 1 },
      B: { C: 2 },
      C: { D: 1 },
      D: {},
    },
  };
  const result_disconnected = bellman_ford(graph_disconnected, "A");
  console.log(result_disconnected);
};

test_bellman_ford();
