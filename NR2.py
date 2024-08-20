import enc
import RC4_Random_seq as rc4_g
import hyper_graph as hg
import decrypt as dec
def nr2(plaintext,edge_seq,seed):
    
    random_seq=rc4_g.generate_rc4_sequence(seed,len(plaintext))

    hypergraph=hg.generate_hypergraph(plaintext,edge_seq,random_seq)

    ciphertext_list=enc.hypergraph_encryption(plaintext,hypergraph)
    ciphertext=""
    for char in ciphertext_list:
        ciphertext+=str(char)+"x"

    decrypted_plaintext=dec.generate_hypergraph_indices(ciphertext_list,edge_seq,random_seq)
    print("Encryption:")
    print()
    print("Plain Text: ", plaintext)
    print("Generated Hypergraph: ", hypergraph)
    print("Cipher Text: ",ciphertext)
    print()
    print("Decryption:")
    print()
    print("Encrypted Plain Text: ", decrypted_plaintext)


    return ciphertext
    
