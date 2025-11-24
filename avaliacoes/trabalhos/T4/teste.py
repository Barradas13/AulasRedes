def fazTudoBitUm(b):
    
    a = 1
    
    for i in range(b):
        a |= 1 << i
        
    return a

def transformaIpDecimal(ip):
    partes = ip.split('.')
    decimal = 0
    
    for i in range(4):
        decimal += int(partes[i]) << 8
    
    return decimal

def verificaDeRede(ip, mascara):
    return ip ^ fazTudoBitUm(mascara)


ip, mascara = input().split('/')

transformaIpDecimal(ip)
print(verificaDeRede(transformaIpDecimal(ip), mascara))
