def all_valid_parens(n):
    if n == 1:
        return ["()"]

    valid = {}
    new_parens = []
    parens = all_valid_parens(n-1)
    for paren in parens:
        value = f"(){paren}"
        if not valid.get(value):
            new_parens.append(value)
            valid[value] = True
        
        _insert_in_middle(paren, new_parens, valid)

        value = f"{paren}()"
        if not valid.get(value):
            new_parens.append(value)
            valid[value] = True

    return new_parens

def _insert_in_middle(paren, new_parens, valid):
    i = 0
    while i < len(paren):
        while paren[i] != ')':
            i += 1
        
        value = f"{paren[:i]}(){paren[i:]}"
        if not valid.get(value):
            new_parens.append(value)
            valid[value] = True
        
        i += 1


if __name__ == "__main__":
    print(all_valid_parens(4))


            