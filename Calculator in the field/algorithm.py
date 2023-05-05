

def division(string, field):
    counter = 1
    var = ''
    while counter < len(string):
        for elem in string[counter]:
            if elem != '*' and elem != '('and elem != ')' and elem != '+' and elem != '-' and elem != '.':
                var += elem
            else:
                string[counter] = string[counter].replace(var, f'*{revers(int(var), field)}')
                var = ''
                counter += 1
                break
    return ''.join(string)

def revers2(num, field):
    num = int(num)
    field = int(field)
    x, xx = 1, 0
    while field:
        q = num // field
        num, field = field, num % field
        x, xx = xx, x - xx*q
    if x < 0:
        x = xx + x
    return x

def revers(num, field):
    num = int(num)
    field = int(field)
    var = 0
    while num * var % field != 1:
        var += 1
    return var

def counting(string, field):
    string.replace(' ', '')
    string.replace('^', '**')
    field = int(field)
    if '/' in string:
        string += '.'
        list_strs = string.split('/')
        string = division(list_strs, field)
        string = string[:-1]
    res = eval(string)
    res = res % field
    return res

def IsPrime(numb):
    numb = int(numb)
    divisor = 2
    while numb % divisor != 0:
        divisor += 1
    return divisor == numb


if __name__ == '__main__':
    expression = counting('5/7', '11')
    numb = revers('9', '149')
