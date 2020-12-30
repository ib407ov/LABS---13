import math
class TVektor2D:
    def __init__(self, *args):
        arguments_count = len(args)
        if arguments_count == 0:
            self.x1 = 0
            self.x2 = 0
            self.y1 = 1
            self.y2 = 1

        elif arguments_count == 1:
            self.x1 = args[0]
            self.x2 = 0
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 2:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 3:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = 0

        else:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = args[3]

    @property
    def function(self):
        print('firs vektor = [{0}, {1}]'.format(self.x1, self.x2))
        print('second vektor = [{0}, {1}]'.format(self.y1, self.y2))

    @property
    def lehghtVekror(self):
        return (math.fabs(math.sqrt(((self.x1 - self.y1) ** 2 ) + ((self.x2 - self.y2) ** 2))))

    @property
    def normalizationvektor(self):
        z = (math.pow(self.x1, 2) + math.pow(self.x2, 2) + (self.y1 ** 2) + (self.x2 ** 2))
        print('x1 = ', self.x1/z)
        print('x2 = ', self.x2/z)
        print('y1 = ', self.y1/z)
        print('y2 = ', self.y2/z)

    @property
    def comparison(self):
        A = math.sqrt(math.pow(self.x1, 2) + math.pow(self.x2, 2))
        B = math.sqrt(math.pow(self.y1, 2) + math.pow(self.y2, 2))
        A = math.fabs(A)
        B = math.fabs(B)
        return (A, B)

    def __add__(self, other):
        return TVektor2D(self.x1 + other,
                         self.x2 + other,
                         self.y1 + other,
                         self.y2 + other)

    def __sub__(self, other):
        return TVektor2D(self.x1 - other,
                         self.x2 - other,
                         self.y1 - other,
                         self.y2 - other)

    def __mul__(self, other):
        return TVektor2D(self.x1 * other,
                         self.x2 * other,
                         self.y1 * other,
                         self.y2 * other)

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 1:
            return self.x1
        elif key == 2:
            return self.x2
        elif key == 3:
            return self.y1
        elif key == 4:
            return self.y2
        else:
            raise Error("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if key == 1:
            self.x1 = value
        elif key == 2:
            self.x2 = value
        elif key == 3:
            self.y1 = value
        elif key == 4:
            self.y2 = value
        else:
            raise Error("Wrong key")

class TVector3D(TVektor2D):

    def __init__(self, *args):
        super().__init__(*args)
        if len(args) == 5:
            self.z1 = args[4]
            self.z2 = 0

        elif len(args) == 6:
            self.z1 = args[4]
            self.z2 = args[5]

        else:
            self.z1 = 0
            self.z2 = 0

    #вивід данних
    @property
    def readVektor3D(self):
        super().function
        print('third vektor = [{0}, {1}]'.format(self.z1, self.z2))

    @property
    def comparisonVektor3D(self):
        C = math.sqrt(math.pow(self.z1, 2) + math.pow(self.z2, 2))
        C = math.fabs(C)
        return super().comparison, C

    def __add__(self, other):
        return TVektor2D(self.x1 + other,
                         self.x2 + other,
                         self.y1 + other,
                         self.y2 + other,
                         self.z1 + other,
                         self.z2 + other)

    def __sub__(self, other):
        return TVektor2D(self.x1 - other,
                         self.x2 - other,
                         self.y1 - other,
                         self.y2 - other,
                         self.z1 - other,
                         self.z2 - other)

    def __mul__(self, other):
        return TVektor2D(self.x1 * other,
                         self.x2 * other,
                         self.y1 * other,
                         self.y2 * other,
                         self.z1 * other,
                         self.z2 * other)

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 1:
            return self.x1
        elif key == 2:
            return self.x2
        elif key == 3:
            return self.y1
        elif key == 4:
            return self.y2
        elif key == 5:
            return self.z1
        elif key == 6:
            return self.z2
        else:
            raise Error("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if key == 1:
            self.x1 = value
        elif key == 2:
            self.x2 = value
        elif key == 3:
            self.y1 = value
        elif key == 4:
            self.y2 = value
        elif key == 5:
            self.z1 = value
        elif key == 6:
            self.z2 = value
        else:
            raise Error("Wrong key")

#t = TVektor2D(0,2)
#t.function

yN = int(input('Create:\n' 
               '1.2D vekor\n' 
               '2.3D vektor\n'
               'Enter number : '))

if yN == 1:
    print('Set 4 coordinates\n')
    A = [int(input('{0} = '.format(i + 1)))for i in range(4)]
    g = TVektor2D(A[0], A[1], A[2], A[3])
    g.function
    print('lehght vektor:\n', g.lehghtVekror)
    print('normalization vectors:\n', g.normalizationvektor)
    print('comprasion vectors:\n', g.comparison)
    k = int(input('1. +\n'
                  '2. -\n'
                  '3. *\n'
                  '4. break'
                  'Enter number : '))
    n = int(input('n = '))
    if k == 1:
        g = g + n
    elif k == 2:
        g = g - n
    elif k == 3:
        g = g * n
    g.function
    k = int(input('Change coordinate:\n'
                  '1. \n'
                  '2. \n'
                  '3. \n'
                  '4. \n'
                  '5.break\n'
                  'Enter number : '))
    if k == 1 or k == 2 or k == 3 or k == 4:
        n = int(input('new number: '))
        g[k] = n
        g.function
else:
    print('Set 6 coordinates\n')
    A = [int(input('{0} = '.format(i + 1))) for i in range(6)]
    g = TVector3D(A[0], A[1], A[2], A[3], A[4], A[5])
    g.readVektor3D
    print('lehght vektor:\n', g.lehghtVekror)
    print('normalization vectors:\n', g.normalizationvektor)
    print('comprasion vectors:\n', g.comparisonVektor3D)
    k = int(input('1. +\n'
                  '2. -\n'
                  '3. *\n'
                  '4. break'
                  'Enter number : '))
    n = int(input('n = '))
    if k == 1:
        g = g + n
    elif k == 2:
        g = g - n
    elif k == 3:
        g = g * n
    g.readVektor3D
    k = int(input('Change coordinate:\n'
                  '1. \n'
                  '2. \n'
                  '3. \n'
                  '4. \n'
                  '5. \n'
                  '6. \n'
                  '7.break\n'
                  'Enter number : '))
    if k < 7:
        n = int(input('new number: '))
        g[k] = n
        g.readVektor3D