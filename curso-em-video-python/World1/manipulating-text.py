# C-U-R-S-O E-M V-I-D-E-O P-Y-T-O-N -> String(cadeia de caracteres)

pharse = 'CURSO EM VIDEO PYTHON'
print(pharse[9])  # return V
print(pharse[9:14])  # return VIDEO
print(pharse[9:21])  # return VIDEO PYTHON
print(pharse[9:21:2])  # return VDOPTO -> jump two by two
print(pharse[:5])  # return CURSO -> [:num] == [0:num]
print(pharse[15:])  # return PYTHON -> [num:] == [num:final]
print(pharse[9::3])  # return VEPH -> 9 - end, jump three by three

print('\n')
print('='*25)

print('\nAnalysis')
print(len(pharse))  # return string length
print(pharse.count('O'))  # return 3 -> quantity of 'O' in the sentence
# return 1 -> quantity of 'O' in the sentence, between 0 and 13
print(pharse.count('O', 0, 13))
print(pharse.find('DEO'))  # return 11 -> starts at index 11
print(pharse.find('IOS'))  # return -1 -> because it was not found
print('CURSO' in pharse)  # return True -> bacause "CURSO" exist in pharse

print('\nTransformation')
# CURSO EM VIDEO PYTHON -> CURSO EM VIDEO Android
pharse = pharse.replace('PYTHON', 'Android')
print(pharse)
print(pharse.upper())  # to upper case
print(pharse.lower())  # to lower case
# capitalize(transform to upper case) the first letter
print(pharse.capitalize())
pharse = pharse.lower()
print(pharse.title())  # curso em video python -> Curso Em Video Python

pharse = '   aprenda python        '
print(pharse.strip())  # '   aprenda python        ' -> 'aprenda python'
print(pharse.rstrip())  # '   aprenda python        ' -> '   aprenda python'
print(pharse.lstrip())  # '   aprenda python        ' -> 'aprenda python        '

print('\nDivision')
pharse = 'CURSO EM VIDEO PYTHON'
print(pharse.split())  # return ['CURSO', 'EM', 'VIDEO', 'PYTHON']

print('\nJunction')
print('-'.join(pharse))
