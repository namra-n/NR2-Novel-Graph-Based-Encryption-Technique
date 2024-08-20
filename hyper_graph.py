import random

def normalise(start_index, edge_size, random_sequence, candidates):

  seq_len = len(random_sequence)
  indices = []

  for i in range(edge_size):
    index = (start_index + i) % seq_len
    indices.append(random_sequence[index])

  # Normalize and round indices
  min_val = min(indices)
  max_val = max(indices)
  indices = [round((x - min_val) / (max_val - min_val) * (len(candidates) - 1)) for x in indices]
  unique_indices = set(indices)

  subset = list(set(candidates[i] for i in unique_indices))

  return subset


def generate_hypergraph(plaintext, edge_sequence, random_sequence):

    plaintext = list(plaintext)
    vertex_count = {char: 0 for char in plaintext}
    hypergraph = []
    hyperedge_vertices=[]

    for char in plaintext:
        hyperedge_vertices.append(char)
        vertex_count[char] += 1

    hyperedge_vertices.remove(plaintext[0])
    hypergraph.append(hyperedge_vertices)

    for i in range(1, len(plaintext)):

        edge_size = edge_sequence[i]
        hyperedge_vertices = []
        min_usage = min(vertex_count.values())
        candidates = [char for char, count in vertex_count.items() if count == min_usage]

        if (len(candidates)<edge_size):
            rem_char=edge_size-len(candidates)
            seq_code=random_sequence[rem_char-1]
            selection_index=sum(map(int,str(seq_code)))%len(plaintext)
            for char in plaintext[selection_index:selection_index+rem_char]:
              if char not in candidates:
                candidates.append(char)

        if len(candidates) > edge_size:
            tie_count = len(candidates)
            seq_code = random_sequence[tie_count-1] 
            selection_index = sum(map(int, str(seq_code))) % len(plaintext)
        
        candidates=normalise(selection_index,edge_size,random_sequence,candidates)

        for char in candidates:
            hyperedge_vertices.append(char)
            vertex_count[char]+= 1

        if plaintext[i] in hyperedge_vertices:
            hyperedge_vertices.remove(plaintext[i]) 
        hypergraph.append(list(hyperedge_vertices))

    return hypergraph