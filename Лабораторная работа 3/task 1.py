src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and False
result = True and False
result = True

print(src == result)
