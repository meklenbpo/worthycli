"""
Worthy CLI app.
"""

# import pandas as pd


def decorate(s:str) -> None:
	print('')
	print(s)
	for _ in range(len(s)):
		print('-', end='')
	print('\n')


greeting = 'Welcome to Worthy CLI:'
decorate(greeting)



while True:
	cmd = input('$>')
	cmd = cmd.lower()
	if cmd == 'exit':
		break


print('---\nTerminated successfully.\n')
# EOA
