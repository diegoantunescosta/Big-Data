import csv

nome = input("Digite seu nome")
end = input("Digite seu endereco ")
cid = input ("Digite a cidade ")
est = input ("Digite seu estado ")
cep = input ("Digite seu CEP ")

print(nome)
print(end)
print(cid)
print(est)
print(cep)


filename = 'test.csv'
with open('test.csv','wb') as f:
  f.write(nome+"\n")
  f.write(end+"\n")
  f.write(cid+"\n")
  f.write(est+"\n")
  f.write(cep+"\n")
