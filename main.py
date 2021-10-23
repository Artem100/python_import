# Типы импортирования без init

import package1.file1
from package1 import file2
from package1.file2 import a

print(package1.file1.h)
print(file2.b)
print(a)


import package2

print(package2.n)