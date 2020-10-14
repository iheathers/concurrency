# def greet():
#     friend = yield
#     print(f'Hello {friend}')
#
#
# g = greet()
# g.send(None)  # Priming the generator
# g.send("dear")

from collections import deque
from types import coroutine

friends = deque(('Harry', 'John', 'Sherlock', 'Jacky'))


@coroutine
def greet_friend():
    while friends:
        greeting = yield
        print(f'{greeting} {friends.popleft().upper()}')


# def greet(g):
#     g.send(None)
#     while True:
#         greeting = yield
#         g.send(greeting)

async def greet(g):
    await g


greeter = greet(greet_friend())
greeter.send(None)
greeter.send("Hey")

greeting = input('Enter a greeting: ')
greeter.send(greeting)


