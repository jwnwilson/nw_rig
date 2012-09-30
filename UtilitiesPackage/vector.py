import math
class Vector:
    'Represents a 3D vector.'
    def __init__(self, x = 0, y = 0,z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    @classmethod
    def initList(cls, inList):
        "Initialize from list"
        if len(inList) != 3:
            error( "List must contain 3 values")
        return cls(float(inList[0]),float(inList[1]),float(inList[2])) 
        
    def __add__(self, val):
        return Vector( self.x + val[0], self.y + val[1],self.z + val[2] )
    
    def __sub__(self,val):
        return Vector( self.x - val[0], self.y - val[1], self.z - val[2] )
    
    def __iadd__(self, val):
        self.x = val[0] + self.x
        self.y = val[1] + self.y
        self.z = val[2] + self.z
        return self
        
    def __isub__(self, val):
        self.x = self.x - val[0]
        self.y = self.y - val[1]
        self.z = self.z - val[2]
        return self
    
    def __div__(self, val):
        return Vector( self[0] / val, self[1] / val, self[2] / val )
    
    def __mul__(self, val):
        return Vector( self[0] * val, self[1] * val, self[2] * val )
    
    def __idiv__(self, val):
        self[0] = self[0] / val
        self[1] = self[1] / val
        self[2] = self[2] / val
        return self
        
    def __imul__(self, val):
        self[0] = self[0] * val
        self[1] = self[1] * val
        self[2] = self[2] * val
        return self
                
    def __getitem__(self, key):
        if( key == 0):
            return self.x
        elif( key == 1):
            return self.y
        elif( key == 2):
            return self.z
        else:
            raise Exception("Invalid key to Point")
        
    def __setitem__(self, key, value):
        if( key == 0):
            self.x = value
        elif( key == 1):
            self.y = value
        elif( key == 2):
            self.z = value
        else:
            raise Exception("Invalid key to Point")
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z)+ ")"
        
def DistanceSqrd( point1, point2 ):
    'Returns the distance between two points squared. Marginally faster than Distance()'
    return ( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
def Distance( point1, point2 ):
    'Returns the distance between two points'
    return math.sqrt( DistanceSqrd(point1,point2) )
def LengthSqrd( vec ):
    'Returns the length of a vector sqaured. Faster than Length(), but only marginally'
    return vec[0]**2 + vec[1]**2 + vec[2]**2
def Length( vec ):
    'Returns the length of a vector'
    return math.sqrt( LengthSqrd(vec) )
def Normalize( vec ):
    'Returns a new vector that has the same direction as vec, but has a length of one.'
    if( vec[0] == 0. and vec[1] == 0. and vec[2] ==0. ):
        return Vector(0.,0.,0.)
    return vec / Length(vec)
def Dot( a,b ):
    'Computes the dot product of a and b'
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def ProjectOnto( w,v ):
    'Projects w onto v.'
    return v * Dot(w,v) / LengthSqrd(v)
