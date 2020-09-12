import es

test = [
    {"documentId": "12345", "name": "Japa"},
    {"documentId": "6789", "name": "Japa1"},
]

es.index_batch('test', test)

