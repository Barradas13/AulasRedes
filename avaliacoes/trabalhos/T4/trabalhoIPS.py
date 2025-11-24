def fazTudoBitUm(b):
    
    a = 1
    
    for i in range(b):
        a |= 1 << i

    a = bin(a)

    if len(a) < 34:
        a += '0' * (34 - len(a))

    return int(a, 2)

def transformaIpDecimal(ip):
    partes = ip.split('.')
    decimal = "0b"
    

    for i in range(4):
        partes[i] = bin(int(partes[i]))


        if len(partes[i][2:]) < 8:
            partes[i] = "0b" + '0' * (8 - len(partes[i][2:])) + partes[i][2:]

    for i in partes:
        decimal += i[2:]

    return int(decimal, 2)

def padronizaDecimalIP(ip):
    ip_binario = bin(ip)[2:]
    ip_saida = ""

    if len(ip_binario) < 32:
        ip_binario = '0' * (32 - len(ip_binario)) + ip_binario

    for i in range(0, 32, 8):
        ip_saida += str(int(ip_binario[i:i+8], 2)) + "."

    return ip_saida[:-1]

def verificaRede(ip, mascara):
    rede = bin(int(ip & mascara))[2:]
    rede_saida = padronizaDecimalIP(int(rede, 2))

    inicio = transformaIpDecimal(rede_saida) + 1
    inicio_saida = padronizaDecimalIP(inicio)

    return rede_saida, inicio_saida

def verificaBroadcast(ip, imasc):
    
    broadcast = bin(int(ip | imasc))[2:]
    broadcast_saida = padronizaDecimalIP(int(broadcast, 2))
    
    fim = transformaIpDecimal(broadcast_saida) - 1
    fim_saida = padronizaDecimalIP(fim)

    return broadcast_saida, fim_saida


ip, mascara = input().split('/')

while mascara < '0' or mascara > '32':
    ip, mascara = input("Mascara invalida. Digite novamente o ip e mascara: ")

dec_ip = transformaIpDecimal(ip)
dec_mascara = fazTudoBitUm(int(mascara))


mascara_invertida = int("0b" + "1" * 32, 2)
mascara_invertida ^= dec_mascara

broadcast, fim = verificaBroadcast(dec_ip, mascara_invertida)
rede, inicio = verificaRede(dec_ip, dec_mascara)

print("Rede: " + rede)
print("Broadcast: " + broadcast)
print("Hosts de " + inicio + " a " + fim)