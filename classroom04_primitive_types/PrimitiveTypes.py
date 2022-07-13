"""
Data Types

str - String - 'this' "this"
int - Integer - 12345, -10
float - Float - 5.3 , -21.6
bool - Boolean - true/false

"""
print('Data Types')

print('Type: string ', 'matheus', type('matheus'), sep=' - ')
print('Type: int', 123, type(123), sep=' - ')
print('Type: float', 32.34, type(32.34), sep=' - ')
print('Type: boolean', '12 == 12', type(12 == 12), sep=' - ')

print()
# Type Casting
print('Type Casting')

print('Type: str', 'matheus', type('matheus'),
      'Type Casting: str -> bool', bool('matheus'),
      sep=' - ')
