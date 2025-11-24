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
    decimal = ""
    

    for i in range(4):
        partes[i] = bin(int(partes[i]))


        if len(partes[i][2:]) < 8:
            partes[i] = "0b" + '0' * (8 - len(partes[i][2:])) + partes[i][2:]

    for i in partes:
        decimal += i[2:]

    return int(decimal, 2)


def verificaRede(ip, mascara):
    rede = bin(int(ip & mascara))[2:]
    rede_saida = ""

    for i in range(0, 32, 8):
        rede_saida += str(int(rede[i:i+8], 2)) + "."

    inicio = int(rede, 2) + 1
    inicio_saida = ""

    for i in range(0, 32, 8):
        inicio_saida += str(int(bin(inicio)[2:][i:i+8], 2)) + "."


    return rede_saida[:-1], inicio_saida[:-1]

def verificaBroadcast(ip, imasc):
    
    broadcast = bin(int(ip | imasc))[2:]
    broadcast_saida = ""

    for i in range(0, 32, 8):
        broadcast_saida += str(int(broadcast[i:i+8], 2)) + "."
    
    fim = int(broadcast, 2) - 1
    fim_saida = ""

    for i in range(0, 32, 8):
        fim_saida += str(int(bin(fim)[2:][i:i+8], 2)) + "."

    return broadcast_saida[:-1], fim_saida[:-1]


ip, mascara = input().split('/')

dec_ip = transformaIpDecimal(ip)
dec_mascara = fazTudoBitUm(int(mascara))

mascara_invertida = int("0b" + "1" * 32, 2)
mascara_invertida ^= dec_mascara

broadcast, fim = verificaBroadcast(dec_ip, mascara_invertida)
rede, inicio = verificaRede(dec_ip, dec_mascara)

print("Rede: " + rede)
print("Broadcast: " + broadcast)
print("Hosts de " + inicio + " a " + fim)