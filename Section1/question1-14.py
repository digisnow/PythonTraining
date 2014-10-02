# reindent
def reindent(s, numSpaces):
    leading_space = numSpaces * ' '
    lines = [ leading_space + line.strip()
             for line in s.splitlines()]
    return '\n'.join(lines)

x = """ line one
    line two
    and line three
    """
print x
print reindent(x, 4)

