# Review the argv module by comparing numbers 

import sys

if len(sys.argv)< 2:
    print('請輸入一些數字，例如: python maxArgv.py 3 7 2 10')
    sys.exit()

validNumbers = []

for arg in sys.argv[1:]:
    try:
        vnum = int(arg)
        validNumbers.append(vnum)
    except ValueError:
        print(f'{arg} 不是有效的整數，略過。')

if len(validNumbers) == 0:
    print('沒有有效的數字可以比較。')
else:
    print('最大值是: ' + str(max(validNumbers)))