## How to use Matrix class
```python 
from main import Matrix
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
result = m1 + m2
print(result)
```
output
```
6 8 
10 12 
```
```python
from main import Matrix
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
scalar = 2
result1 = m1 * scalar
result2 = m1 * m2
print(result1)
print(result2)
```
output
```
2 4 
6 8 

5 12 
21 32 
```
```python
from main import Matrix
m = Matrix([[1, 2, 3], [4, 5, 6]])
result = m.transpose()
print(result)
```
output
```
1 4 
2 5 
3 6 
```