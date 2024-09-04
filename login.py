import re

def emailc(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


n=str(input('nome:'))
e=input('email:')
e2=input('confirme email:')
s = input("Senha: ")
s2 = input("Confirme a senha: ")

confir= len(s) and len(s2)
confir2= len(n)

if confir <=10 and confir >=4 and s==s2 and confir2<20 and confir2>0 and e==e2 and emailc(e):
    print('conta registrada')
else:
    print('conta não registrada')
