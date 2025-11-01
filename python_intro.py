print('Hello, Django girls!')
print('----------------------------------')

if 3 > 2:
    print('It works!')

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("Ola")
print('----------------------------------')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
print('----------------------------------')

for i in range(1, 6):
    print(i)