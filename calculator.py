import re
class Calculator(object):
    def calc(self, expression):
        while '/' in expression:
            expression[expression.index('/') - 1] = float(expression[expression.index('/') - 1]) / float(
                expression[expression.index('/') + 1])
            del expression[expression.index('/'):expression.index('/') + 2]
        while '*' in expression:
            expression[expression.index('*') - 1] = float(expression[expression.index('*') - 1]) * float(
                expression[expression.index('*') + 1])
            del expression[expression.index('*'):expression.index('*') + 2]
        while '-' in expression:
            expression[expression.index('-') - 1] = float(expression[expression.index('-') - 1]) - float(
                expression[expression.index('-') + 1])
            del expression[expression.index('-'):expression.index('-') + 2]
        while '+' in expression:
            expression[expression.index('+') - 1] = float(expression[expression.index('+') - 1]) + float(
                expression[expression.index('+') + 1])
            del expression[expression.index('+'):expression.index('+') + 2]
        return expression[0]

    def evaluate(self, string):
        string = string.replace('(', ' ( ')
        string = string.replace(')', ' ) ')
        param = string.split()
        new = []
        while True:
            a = []
            k = 1
            for i in range(len(param)):
                if param[i] == '(' or param[i] == ')':
                    a.append(i)

            for i in range(len(a) - 1, -1, -1):
                if param[a[i]] == '(':
                    while param[a[i]] == param[a[i + k]]:
                        k += 1
                    new.append(param[a[i] + 1:a[i + k * 2 - 1]])
                    param[a[i]] = self.calc(param[a[i] + 1:a[i + k * 2 - 1]])
                    del param[a[i] + 1:a[i + k * 2 - 1] + 1]
                    break
            if a == []:
                break
        return float(self.calc(param))