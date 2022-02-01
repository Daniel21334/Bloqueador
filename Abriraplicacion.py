from cryptography.fernet import Fernet
import os

os.chdir(os.getcwd()+'\\'+'Certificados')
direc = os.getcwd()

def cargar_cer():
    os.chdir(os.getcwd() + '\\' + 'Cer')
    return open('Cerificado.cer', 'rb').read()

def cargar_key():
    return open('ResCer.cer', 'rb').read()

def cargar_cer_txt():
    os.chdir(direc)
    os.chdir(os.getcwd() + '\\' + 'RES' + '\\' + 'CER')
    return open('Certificado.txt', 'rb').read()

def cargar_key_txt():
    return open('ResCer.txt', 'rb').read()

def decrypt(items, u):
    f = Fernet(u)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

usua = input("Ingresa el usuario: ")
contrase = input("Ingrese la contrasena: ")

if __name__ == '__main__':

    path_to_U = os.getcwd() + '\\' + 'RES' + '\\' + 'CER'
    items = os.listdir(path_to_U)
    full_path = [path_to_U + '\\' + item for item in items]

    Us = cargar_cer()
    USS = cargar_key()
    decrypt(full_path, Us)
    decrypt(full_path, USS)

    U = cargar_cer_txt().decode()

    if usua == U:
        os.chdir(direc)
        path_to_U = os.getcwd() + '\\' + 'RES' + '\\' + 'KEY'
        items = os.listdir(path_to_U)
        full_path = [path_to_U + '\\' + item for item in items]

        Us = cargar_cer()
        USS = cargar_key()
        decrypt(full_path, Us)
        decrypt(full_path, USS)
    else:
        print("none")

