from cryptography.fernet import Fernet
import  os
import shutil

print("Registro: \n")

user = str.encode(input("Ingresa el usuario:"))

U = Fernet.generate_key()
usuario_cifrado = Fernet(U)
usuario_encriptado = usuario_cifrado.encrypt(user)

contra = str.encode(input("Ingrese la contrasena: "))

C = Fernet.generate_key()
contra_cifrada = Fernet(C)
contra_encriptada = contra_cifrada.encrypt(contra)

os.mkdir('Certificados')
os.chdir(os.getcwd()+'\\'+'Certificados')
print(os.getcwd())

with open("Cerificado.cer", "wb") as key_file:
    key_file.write(U)

with open("Certificado.key", "wb") as key_file:
    key_file.write(C)

os.mkdir('Cer')
os.mkdir('Key')
shutil.move('Cerificado.cer', os.getcwd()+'\\'+'Cer')
shutil.move('Certificado.key', os.getcwd()+'\\'+'Key')

'''def encrypt(items, U):
    f = Fernet(U)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

    path_to_encrypt = os.getcwd()+'\\'+'Key'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    encrypt(full_path, U)

#os.system('"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"')
'''