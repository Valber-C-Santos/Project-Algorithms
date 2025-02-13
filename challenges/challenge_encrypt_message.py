def encrypt_message(message: str, key: int):

    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


print(encrypt_message("hello", 0))
print(encrypt_message("hello", 1))
print(encrypt_message("hello", 2))
print(encrypt_message("hello", 3))