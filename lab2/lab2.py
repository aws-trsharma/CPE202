"""LAB2
CPE202
"""
def perm_lex(string1):
    """Recursive Function that takes a string and generates all the
   permutations of the characters in a string in lexographic order
   args:
      string1 (string): a string
   returns:
      final_list (string): a list of string values
   """
    final_list = []
    if len(string1) == 1:
        final_list.append(string1)
        return final_list
    for i, char in enumerate(string1):
        val = char
        perm = perm_lex(string1[:i] + string1[i+1:])
        for str1 in perm:
            final_list.append(val + str1)
    return final_list
