import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Menu
while True:
    opt = input('Para codificar digite C, para decodificar digite D').upper()
    if opt == 'C':
        dataQR = input('O que deve conter no QRCode')
        endQR = input('Endereço para download')
        nomeQR = input('Nome do arquivo')
        pathQR = endQR + '\\' + nomeQR + '.png'
        imgQR = qrcode.make(dataQR)
        imgQR.save(pathQR)
        break
    elif opt == 'D':
        endQRdeco = input('Endereço do arquivo')
        imgQRdeco = Image.open(endQRdeco)
        decoded = decode(imgQRdeco)
        print(decoded)
        break
    else:
        continue