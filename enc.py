

def hypergraph_encryption(plaintext, hypergraph):
    

  value_reference={}
  for char in plaintext:
    value_reference[char]=ord(char)

  ciphertext_list=[]
  c=0
  for hyperedge in hypergraph:
    xor_result=value_reference[plaintext[c]]
    for vertex in hyperedge:
      xor_result^=value_reference[vertex]
    ciphertext_list.append(xor_result)
    value_reference[plaintext[c]]= xor_result
    c+=1

  return ciphertext_list