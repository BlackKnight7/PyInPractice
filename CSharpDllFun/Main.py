import clr

clr.AddReferenceToFile('CSharpMath.dll')

from CSharpMath import *

class CMath(CSharpMath):
    def __init__(self):
        pass

    def normalAdd(self, a, b):
        return CSharpMath.add(self, a, b)


print CMath().normalAdd(3, 5)
print CSharpMath.specialAdd(3, 5)
