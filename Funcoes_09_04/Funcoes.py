def valida_string(string, valor_min=1, valor_max=100):
    if valor_min <= len (string) <= valor_max:
        return True
    else:
        return False  
print(valida_string("oi"))           
print(valida_string("oi", 5, 10))   
print(valida_string("python", 3, 6)) 
print(valida_string(""))             