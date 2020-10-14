from collections import deque

friends = deque(('Rolf', 'Harry', 'John', 'Snow'))


def get_friend():
    yield from friends


friend = get_friend()
print(next(friend))
print(next(friend))
print(next(friend))


def greet(gen):
    while True:
        try:
            res = next(gen)
            yield f'Hello {res}'
        except StopIteration:
            pass


g = greet(friend)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
