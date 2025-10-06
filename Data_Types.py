int_var = 42
print("Integer:", int_var, type(int_var))

float_var = 3.14
print("Float:", float_var, type(float_var))

str_var = "Hello, World!"
print("String:", str_var, type(str_var))

bool_var = True
print("Boolean:", bool_var, type(bool_var))

list_var = [1, 2, 3, [4, 5], ["a", "b", [6, 7]]]
print("List:", list_var, type(list_var))

tuple_var = (1, 2, (3, 4), ("a", "b", (5, 6)))
print("Tuple:", tuple_var, type(tuple_var))

set_var = {1, 2, 3, frozenset({4, 5})}
print("Set:", set_var, type(set_var))

frozenset_var = frozenset([1, 2, 3, 4])
print("Frozenset:", frozenset_var, type(frozenset_var))

dict_var = {
    "name": "Alice",
    "age": 25,
    "marks": {"math": 90, "science": 95},
    "hobbies": ["reading", "sports", {"indoor": "chess"}]
}
print("Dictionary:", dict_var, type(dict_var))

bytes_var = b'hello'
print("Bytes:", bytes_var, type(bytes_var))

bytearray_var = bytearray([65, 66, 67])
print("Bytearray:", bytearray_var, type(bytearray_var))

none_var = None
print("NoneType:", none_var, type(none_var))

complex_var = 2 + 3j
print("Complex:", complex_var, type(complex_var))