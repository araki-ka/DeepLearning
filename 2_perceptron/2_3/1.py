# 2.3.1 簡単な実装

# AND circuit
def and_circuit(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

# execute
print("----- AND -----")
print(and_circuit(0, 0))
print(and_circuit(1, 0))
print(and_circuit(0, 1))
print(and_circuit(1, 1))
