def para_func (*para):
    result = 0
    for num in para:
        result = result + num
    return result

hap = 0

hap = para_func(10,20)
print(hap)