import hyper_graph as hg
import copy

def generate_hypergraph_indices(ciphertext, edge_sequence, random_sequence):

    ciphertext = list(ciphertext)
    vertex_count = {i: 0 for i in range(len(ciphertext))}
    hypergraph = []

    hyperedge=[]
    for index in range(len(ciphertext)):
        vertex_count[index] += 1
        hyperedge.append(index)
    hyperedge.remove(0)
    
    hypergraph.append(hyperedge)

    for i in range(1, len(ciphertext)):

        hyperedge=[]
        edge_size = edge_sequence[i]
        min_usage = min(vertex_count.values())
        candidates = [index for index, count in vertex_count.items() if count == min_usage]
        # print(candidates)

        if (len(candidates)<edge_size):
            rem_char=edge_size-len(candidates)
            seq_code=random_sequence[rem_char-1]
            selection_index=sum(map(int,str(seq_code)))%len(ciphertext)
            for index in range(selection_index,selection_index+rem_char):
              if index not in candidates:
                candidates.append(index)

        if len(candidates) > edge_size:
            tie_count = len(candidates)
            seq_code = random_sequence[tie_count-1] 
            selection_index = sum(map(int, str(seq_code))) % len(ciphertext)
        
        candidates=hg.normalise(selection_index,edge_size,random_sequence,candidates)
        # print(candidates)

        for index in candidates:
            hyperedge.append(index)
            vertex_count[index]+= 1

        hyperedge_copy=copy.deepcopy(hyperedge)
        if i in hyperedge_copy:
            hyperedge_copy.remove(i)  
        hypergraph.append(hyperedge_copy)


    return reverse_XOR(hypergraph,ciphertext)

def reverse_XOR(hypergraph_indices,ciphertext):
    reference_value=dict(enumerate(ciphertext))
    print(reference_value)
    plaintext=[0]*len(ciphertext)
    for edge_index in range(len(ciphertext)-1,-1,-1):
        hyperedge=hypergraph_indices[edge_index]
        # print(hyperedge)
        plaintext_vertex=0
        for vertex in hyperedge:
            plaintext_vertex^=reference_value[vertex]
        plaintext_vertex^=ciphertext[edge_index]
        # print(plaintext_vertex)
        plaintext[edge_index]=plaintext_vertex
        reference_value[edge_index]=plaintext_vertex
        # print(reference_value)

    # print(reference_value)
    plaintext=[chr(char) for char in plaintext]
    return plaintext

# ciphertext=[17, 2, 122, 10, 23, 99]
# edge_sequence = [6, 3, 4, 2, 5, 2]
# random_sequence = [51, 99, 85, 26, 34, 55]
# hypergraph = generate_hypergraph_indices(ciphertext, edge_sequence, random_sequence)
# # quit()
# print(hypergraph)
