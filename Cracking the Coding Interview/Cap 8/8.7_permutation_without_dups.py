def all_permutations(name:str) -> list:
    if len(name) <= 1:
        return [name[:]]
    
    permutations = all_permutations(name[1:])
    new_permutations = []
    for _, value in enumerate(permutations):
        _insert_char(name[0], value, new_permutations)

    return new_permutations

def _insert_char(character: str, name:str, array:list):
    for i in range(len(name)+1):
            array.append(f"{name[:i]}{character}{name[i:]}")


if __name__ == "__main__":
    print(all_permutations("ABC"))
