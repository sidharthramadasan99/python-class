

i = 10
print(f'i: {i};')
print(f'type(i): {type(i)}')

j = 10
print(f'j: {j};')
print(f'type(j): {id(j)}')


print(f'i == j: {i == j}') # both variable have the same value
print(f' i is j: {i is j}') # both refer to the same object

k = 23.6
print(f'k:{k}')
print(f'type(k): {type(k)}')

c = complex(i,j)
print(f'c: {c}')
print(f'type(c): {type(c)}')

flag = True
print(f'flag: flag: {flag}')
print(f'type(flag): {type(flag)}')

s = "this is a string"
print(f's: {s}')
print(f'type(s): {type(s)}')

m = [10,20]
n = [10,20]
print(f'type(m): {type(m)}')
print(f'type(n): {type(n)}')
print(f'm == n: {m == n}')
print(f'm is n: {m is n}')
print(f'id(m): {id(m)}')
print(f'id(n): {id(n)}')

p = m
print(f'm is p: {m is p}')
print('Appending "30" to m')
m.append(30)
print(f'm: {m}')
print(f'n: {n}')
print(f'p: {p}')

t = (1,2,3)
print(f't: {t}')
print(f'type(t): {type(t)}')

st = {1,2,3}
print(f'st: {st}')
print(f'type(st): {type(st)}')

d = {1: 'one', 2: 'two'}
print(f'd: {d}')
print(f'type(d): {type(d)}')

i = int(k)
print(f'i: {i}')
print(f'type(i): {type(i)}')

k = float(i)
print(f'k: {k}')
print(f'type(k): {type(k)}')

st = '23.4'
k = float(st)
print(f'k: {k}')
print(f'type(k): {type(k)}')