# Display book information and total copies from a nested library dictionary

library = {
    'Harry Potter': {'copies': 4, 'genres': ['Fantasy', 'Adventure']},
    'Python 101': {'copies': 2, 'genres': ['Programming', 'Education']},
    'Dune': {'copies': 5, 'genres': ['Sci-Fi']}
}

def displayLibrary(library):
    totalCopies = 0
    for K, V in library.items():
        print('Book: ' + K)
        totalCopies +=V['copies']
        for k, v in V.items():
            print(k, end = ': ')
            try:
                if len(v) == 1:
                    print(v[0])
                else:
                    print(', '.join(v[:-1]) + ', '  + v[-1])
            except TypeError:
                print(v)
        print()

    print('Total number of books: ' + str(totalCopies))

displayLibrary(library)