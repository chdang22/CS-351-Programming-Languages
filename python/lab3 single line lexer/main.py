import re


def cut_one_line_tokens(line):
    # Output list starting from empty list
    # Your lexer logic, find output_list using regular expression
    # add its type and format into <type, token> pair as a string and save it into the output list
    # remove/cut the first token you found from the line of line,
    # and continue finding/cutting the next token
    # Print your output list, look like this: [<key,int>, <id,A1>, <op,=>, <lit,5>]

    # define reg ex for each token
    keyword_regex = re.compile("if|else|int|float")
    operator_regex = re.compile("=|\+|>|\*")
    separator_regex = re.compile("\(|\)|:|\"|;")
    identifier_regex = re.compile("[a-zA-Z]+[0-9]*")
    int_literal_regex = re.compile("\d+")
    float_literal_regex = re.compile("\d+\.\d+")
    string_literal_regex = re.compile("\".+\"")

    #output list
    output_list = []

    #loop until find all token
    for i in line:

        # Check keyword
        keyword_match = keyword_regex.match(line)
        if keyword_match:
            token = keyword_match.group()
            output_list.append(("<key," + token + ">"))
            line = line[len(token):].strip()
            continue
# Check for operators
        operator_match = operator_regex.match(line)
        if operator_match:
            token = operator_match.group()
            output_list.append(("<op," + token + ">"))
            line = line[len(token):].strip()
            continue

        # Check for separators
        separator_match = separator_regex.match(line)
        if separator_match:
            token = separator_match.group()
            output_list.append(("<sep," + token + ">"))
            line = line[len(token):].strip()
            continue

        # Check for identifiers
        identifier_match = identifier_regex.match(line)
        if identifier_match:
            token = identifier_match.group()
            output_list.append(("<id," + token + ">"))
            line = line[len(token):].strip()
            continue

        # Check for int literals
        int_literal_match = int_literal_regex.match(line)
        if int_literal_match:
            token = int_literal_match.group()
            output_list.append(("<lit," + token + ">"))
            line = line[len(token):].strip()
            continue

        # Check for float literals
        float_literal_match = float_literal_regex.match(line)
        if float_literal_match:
            token = float_literal_match.group()
            output_list.append(("<lit," + token + ">"))
            line = line[len(token):].strip()
            continue

        # Check for string literals
        string_literal_match = string_literal_regex.match(line)
        if string_literal_match:
            token = string_literal_match.group()
            output_list.append(("<lit," + token + ">"))
            line = line[len(token):].strip
            continue
    print(output_list)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cut_one_line_tokens("int A1=5")
    cut_one_line_tokens("int a1 = 5")
    cut_one_line_tokens(" ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
