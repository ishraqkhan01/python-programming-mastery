a = int(input("Enter first integer (A): "))
b = int(input("Enter second integer (B): "))

print(f"\n--- Binary Representations ---")
print(f"A ({a}) in binary: {bin(a)[2:].zfill(8)}")
print(f"B ({b}) in binary: {bin(b)[2:].zfill(8)}")

print("1.Bitwise AND (&)")
result_and = a & b
print(f"{a} & {b} = {result_and} | Binary: {bin(result_and)[2:].zfill(8)}")

print("2. Bitwise OR (|)")
result_or = a | b
print(f"{a} | {b} = {result_or} | Binary: {bin(result_or)[2:].zfill(8)}")

print("3. Bitwise XOR (^)")
result_xor = a ^ b
print(f"{a} ^ {b} = {result_xor} | Binary: {bin(result_xor)[2:].zfill(8)}")

print("4. Bitwise NOT (~)")
result_not_a = ~a
print(f"~{a} = {result_not_a}")

print("5. Left Shift (<<)")
result_ls = a << 1
print(f"{a} << 1 = {result_ls} | Binary: {bin(result_ls)[2:].zfill(8)}")

print("6. Right Shift (>>)")
result_rs = a >> 1
print(f"{a} >> 1 = {result_rs} | Binary: {bin(result_rs)[2:].zfill(8)}")