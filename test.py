print('Hello, Django girls')
if 3>2:
    print("Funguje to!")
if 5>2:
    print("5 je väčšie ako 2")
else:
    print("5 nie je väčšie ako 2")

name='Nika'
if name == 'Ola':
    print('Ahoj Ola!')
elif name == 'Sonja':
    print('Ahoj Sonja')
else:
    print('Ahoj neznama')

volume=52
if volume < 20:
    print("Potichu")
elif 20<= volume < 50:
    print("Super")
elif 50<= volume < 100:
    print("Nahlas")

#Change the volume if it's too loud or too quiet
if volume<20 or volume>80:
    volume = 50
    print("To je lepsie!")

def hi():
    print ("Ahoj!")
    print("Ako sa mas?")
hi()

def hi(meno):
    if meno == 'Ola':
        print('Ahoj Ola!')
    elif meno == 'Sonja':
        print('"Ahoj Sonja!')
    else:
        print('Ahoj neznama!')
hi('Ola')
hi('Nika')

def hi(meno):
    print("Ahoj " + meno + "!")
hi("Nika")

dievcata=["Katka", "Monika", "Mirka", "Nika"]
for meno in dievcata:
    hi(meno)
for i in range(1,9):
    print(i)


