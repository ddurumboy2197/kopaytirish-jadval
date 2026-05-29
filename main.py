def create_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()

create_multiplication_table(10)
```

```python
def create_multiplication_table(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += f"{i} x {j} = {i * j}\t"
        print(row)

create_multiplication_table(10)
```

```python
def create_multiplication_table(n):
    for i in range(1, n + 1):
        print(f"{'x':^3} | {'Result':^10}", end='\n' if i == 1 else '\t')
        for j in range(1, n + 1):
            print(f"{i:3} | {i * j:10}", end='\t')
        print()

create_multiplication_table(10)
