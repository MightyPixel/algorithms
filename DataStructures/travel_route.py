thickets = [
    ('SOF', 'PAR'),
    ('PAR', 'LON'),
    ('LON', 'NY')
]

def find_starting_point(thickets):
    outgoing = set()
    ingoing = set()

    for start, end in thickets:
        outgoing.add(start)
        ingoing.add(end)

    return next(iter(outgoing.difference(ingoing)))

print(find_starting_point(thickets))
