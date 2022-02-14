import math

def surfacesphere(radius):
    S = 4.0 * math.pi * radius ** 2
    return S

def volumesphere(radius):
    V = 4.0 / 3.0 * math.pi * radius ** 3
    return V

def surfacecone(radius, height):
    S = math.pi * radius * math.sqrt(radius**2 + height**2)
    return S

def volumecone(radius, height):
    V = 1.0 / 3.0 * math.pi * radius**2 * height
    return V
