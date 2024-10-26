#bitwise operator in python
# Bitwise operators in Python perform operations on binary representations of integers at the bit level. Here’s a rundown of the common bitwise operators:

### 1. **AND (`&`)**
#    - Sets each bit to 1 if both bits are 1.
#    - **Example**:
#      ```python
a = 5      # Binary: 0101
b = 3      # Binary: 0011
result = a & b  # Binary: 0001 (1 in decimal)
print(result)   # Output: 1
    #  ```

### 2. **OR (`|`)**
#    - Sets each bit to 1 if at least one of the bits is 1.
#    - **Example**:
#      ```python
a = 5      # Binary: 0101
b = 3      # Binary: 0011
result = a | b  # Binary: 0111 (7 in decimal)
print(result)   # Output: 7
    #  ```

### 3. **XOR (`^`)**
#    - Sets each bit to 1 if only one of the bits is 1 (but not both).
#    - **Example**:
#      ```python
a = 5      # Binary: 0101
b = 3      # Binary: 0011
result = a ^ b  # Binary: 0110 (6 in decimal)
print(result)   # Output: 6
    #  ```

### 4. **NOT (`~`)**
#    - Inverts all the bits (also called bitwise negation).
#    - **Example**:
#      ```python
a = 5        # Binary: 0101
result = ~a  # Binary: 1010 (inverts bits)
print(result) # Output: -6 (two's complement representation)
    #  ```

### 5. **Left Shift (`<<`)**
#    - Shifts the bits of the number to the left by the specified number of positions.
#    - **Example**:
#      ```python
a = 5       # Binary: 0101
result = a << 1  # Binary: 1010 (10 in decimal)
print(result)    # Output: 10
    #  ```

### 6. **Right Shift (`>>`)**
#    - Shifts the bits of the number to the right by the specified number of positions.
#    - **Example**:
#      ```python
a = 5       # Binary: 0101
result = a >> 1  # Binary: 0010 (2 in decimal)
print(result)    # Output: 2
    #  ```

### Summary of Bitwise Operators
# \ Operator   \ Name        \ Example         \
# \---------- \ -------------\-----------------\
# \ `&`        \ AND         \ `a & b`         \
# \`|`        \  OR          \ `a | b`         \
# \ `^`      \ XOR         \ `a ^ b`         \
# \ `~`       \ NOT         \ `~a`            \
# \ `<<`     \ Left Shift  \ `a << n`        \
# \ `>>`     \ Right Shift \ `a >> n`        \

# These operators are useful for tasks like low-level programming, encryption algorithms, and optimization in certain mathematical computations.