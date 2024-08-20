# NR2-Novel-Graph-Based-Encryption-Technique
NR2 is a Python-based encryption and decryption algorithm designed to offer an innovative approach to data security. It leverages concepts from graph theory, specifically hypergraphs, to represent plaintext characters as vertices and perform internal operations on them. This approach aims to produce a unique and potentially difficult-to-crack encryption scheme.

**Modular Design**: The NR2 project is structured into distinct modules, each with a specific function. This promotes code readability and maintainability.

**Exection**
Locate the use.py script within the project directory for execution.

***Project Structure***
*hyper_graph.py*: Responsible for generating the hypergraph representation of the plaintext message based on the user-provided degree sequence and seed.
*enc.py*: Implements the encryption logic, performing internal operations on the hypergraph vertices.
*decryption.py*: Reverses the encryption process, returning the decrypted plaintext from the encrypted ciphertext.
*NR2.py*: Imports all necessary modules and functions to orchestrate the encryption and decryption operations.
*use.py*: The main script that interacts with the user, collects input, drives the encryption/decryption processes using other modules, and displays the results.

 

