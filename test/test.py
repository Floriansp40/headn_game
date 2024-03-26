# a = None

# print(type(a))

# a = int(input("Saisie clavier :"))

# print(a)
# print(type(a))

p = ''
t = False
while not p.isdigit():
    if t :
        print("ERROR")
    p = input('Saisie clavier :')
    t = True


p = int(p)
print('-'*30)
print(p)
print(type(p))