from cryptography.fernet import Fernet
import  os
import shutil

direc = os.getcwd()

def encryptCU(items, U):
    f = Fernet(U)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def encryptCC(items, C):
    f = Fernet(C)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def carga_usu():
    path_to_K = os.getcwd() + '\\' + 'KEY'
    items = os.listdir(path_to_K)
    full_path = [path_to_K + '\\' + item for item in items]

    encryptCU(full_path, C)
    encryptCC(full_path, U)

def carga_con():
    path_to_U = os.getcwd() + '\\' + 'CER'
    items = os.listdir(path_to_U)
    full_path = [path_to_U + '\\' + item for item in items]

    encryptCU(full_path, C)
    encryptCC(full_path, U)

print("Registro: \n")

user = str.encode(input("Ingresa el usuario:"))
contra = str.encode(input("Ingrese la contrasena: "))

os.mkdir('Certificados')
os.chdir(os.getcwd()+'\\'+'Certificados')

with open("Cerificado.cer", "wb") as key_file:
    U = Fernet.generate_key()
    key_file.write(U)

with open("ResCer.cer", "wb") as key_file:
    C = Fernet.generate_key()
    key_file.write(C)

os.mkdir('Cer')
shutil.move('Cerificado.cer', os.getcwd()+'\\'+'Cer')
shutil.move('ResCer.cer', os.getcwd()+'\\'+'Cer')

os.mkdir('RES')
os.chdir(os.getcwd()+'\\'+'RES')

with open("Certificado.txt", "wb") as txt:
    us = user
    txt.write(us)

os.mkdir('CER')
shutil.move('Certificado.txt', os.getcwd()+'\\'+'CER')

with open("ResCer.txt", "wb") as txt:
    ce =contra
    txt.write(ce)

os.mkdir('KEY')
shutil.move('ResCer.txt', os.getcwd()+'\\'+'KEY')

if __name__ == '__main__':
    carga_usu()
    carga_con()


#os.system('"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"')
