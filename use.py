import NR2 as nr2

plaintext = input('Enter Plaintext: ')
edge_seq=input("Enter Key :").split(" ")
edge_seq = [int(num) for num in edge_seq]
seed=int(input('Enter Seed Value for random generator: '))

nr2.nr2(plaintext,edge_seq,seed)

