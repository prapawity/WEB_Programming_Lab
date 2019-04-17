class Cookie():
    def __init__(self,shape,size,cookie_type):
        self.shape = shape
        self.size = size
        self.cookie_type = cookie_type
        self.status = 'raw'

    def __str__(self):
        return 'My %s cookie' % (self.cookie_type)

    def __lt__(self, other):
        return self.size < other.size
    
    def __gt__(self, other):
        return self.size > other.size


    @property
    def shape(self):
        return self._shape
    
    @shape.setter
    def shape(self, value):
        self._shape = 'Shape of cookie a: ' + value

    def bake(self):
        print('Cookie is baking')
        self.status = 'baked'
    @staticmethod
    def cut():
        return "Cut"
c1 = Cookie('star',20,'cc')
c2 = Cookie('re',10,'but')
print(c1.shape,c2.shape)
c2.bake()
print(c2.cut())
print(c2.status)
print(c1>c2)