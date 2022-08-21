def arithmetic_arranger(*problems):
  if len(problems[0]) > 5:
    return "Error: Too many problems."
  first = []
  second = []
  operators = []
  for problem in problems[0]:
    fir, operator, sec = problem.strip().split()
    first.append(fir)
    second.append(sec)
    operators.append(operator)

  legal_operators = ['+', '-']
  if not all(operators in legal_operators for operators in operators):
    return "Error: Operator must be '+' or '-'."
  if not all(num.isnumeric() for num in first):
    return "Error: Numbers must only contain digits."
  if not all(num.isnumeric() for num in second):
    return "Error: Numbers must only contain digits."
  if not all(len(num) <= 4 for num in first) or not all(len(num) <= 4 for num in second):
    return "Error: Numbers cannot be more than four digits."

  answers = []
  for i in range(0, len(problems[0])):
    if operators[i] == '+':
      answers.append(int(first[i]) + int(second[i]))
    else:
      answers.append(int(first[i]) - int(second[i]))

  row1 = []
  row2 = []
  row3 = []
  row4 = []
  arranged_problems = ""

  for i in range(0, len(problems[0])):
    longest = max(len(first[i]), len(second[i])) + 2
    row1.append(first[i].rjust(longest))
    row2.append(operators[i] + second[i].rjust(longest-1))
    row3.append("-" * longest)
    row4.append(str(answers[i]).rjust(longest))

  row1 = "    ".join(row1) + "\n"
  row2 = "    ".join(row2) + "\n"
  row3 = "    ".join(row3)
  row4 = "    ".join(row4)

  if len(problems) > 1:
    arranged_problems = row1 + row2 + row3 + "\n" + row4
  else:
    arranged_problems = row1 + row2 + row3

  return arranged_problems


def main():
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
    print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
    print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
    print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
    print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

if __name__ == '__main__':
    main()
