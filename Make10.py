"""A python script that was made to solve the equations in the game 4=10,
https://play.google.com/store/apps/details?id=app.fourequalsten.fourequalsten_app&hl=en&gl=US"""

from itertools import permutations, product


def solver(expression, expression_list):
    """Takes a list of numbers and symbols and turns it into a string to be evaluated as a maths equation"""
    exp = ''.join(str(e) for e in expression)
    expression_list.append(exp)
    try:
        ans = eval(exp)
        if ans == 10:
            print(exp, "=", ans, f"\nTested {len(expression_list)} equations")
    except:
        pass


def add_symbols(symbol, numbers, exp_list):
    """Accepts a list of possible permutations, adds in math symbols, passes it to be solved."""
    symbol_product = product(symbol, repeat=3)
    for sym in symbol_product:
        expression = []
        sym = list(sym)
        while len(sym) != 4:
            sym.append("")
        for n, s in zip(numbers, sym):
            expression.append(n)
            expression.append(s)
        solver(expression, exp_list)


def number_combinations(numbers, symbols):
    """Calculates the number permutations, and passes them to be turned into solvable equations."""
    num_perms = permutations(numbers)
    possible_expressions = []
    answers = []
    for nums in num_perms:
        add_symbols(symbol=symbols, numbers=nums, exp_list=possible_expressions)
    return possible_expressions, answers


def add_brackets(possible_expressions):
    """Adds brackets to equations, passes them to be solved."""
    list_copy = possible_expressions[:]
    # Possible locations for brackets
    bracket_dic = {"A": (0, 4), "B": (0, 6), "C": (0, 8), "D": (2, 6), "E": (2, 8), "F": (4, 8)}
    for exp in possible_expressions:
        exp_list = []
        for i in exp:
            exp_list.append(str(i))
        for open_position in ["A", "B", "C", "D", "E", "F"]:
            exp_list_b = exp_list[:]
            exp_list_b.insert(bracket_dic[open_position][0], "(")
            exp_list_b.insert(bracket_dic[open_position][1], ")")
            solver(exp_list_b, list_copy)


if __name__ == '__main__':
    in_numbers = [1, 1, 5, 8]
    in_symbols = ["-", "/", "*", "+"]
    expressions, answers = number_combinations(in_numbers, in_symbols)
    # final_list = calculate_with_brackets(expressions)
    add_brackets(expressions)
