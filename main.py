class Rectangle :
  def __init__(self,widht,height) :
    self.widht = widht
    self.height = height
    
  def set_width (self, new_widht) :
    self.widht = new_widht
    
  def set_height (self, new_height) :
    self.height = new_height
    
  def get_area (self) :
    return self.widht * self.height
  
  def get_perimeter (self) :
    return 2 * self.widht + 2 * self.height
  
  def get_diagonal (self) :
    return (self.widht**2 + self.height ** 2) **.5
  
  def get_picture (self) :
    #el numero de lineas a imprimir = height
    star = ''
    for i in range (self.height) :
      if self.widht > 50 or self.height > 50 :
        return 'Too big for picture'
      else :
        star = star + '*' * self.widht + '\n'
    return star
  
  def get_among_inside (self,shape) :
    #si la clase es Cuadrado
    big = max(self.widht,self.height) #esto nos da el max del rect
    square_side = Square.self.lenght(shape)


  def __str__(self) :
    return f"Rectangle(widht={self.widht}, height={self.height})"
  
  #pasamos a la segunda parte del programa

class Square (Rectangle) : #comprovar si la herencia funcionaba así
  def __init__(self,lenght) : 
    self.lenght = lenght
    self.widht = lenght
    self.height = lenght

  def set_side (self,new_lenght) :
    self.lenght = new_lenght
    self.widht = new_lenght
    self.height = new_lenght
  
  def __str__ (self) :
    return f"Square(side={self.lenght})"
  
  def side (self) :
    return self.lenght


rectangle1 = Rectangle (10,5)
print (rectangle1.get_area())
rectangle1.set_height(3)
print (rectangle1)
print (rectangle1.get_perimeter())
print (rectangle1.get_picture())

cuadrado = Square (9)
print(cuadrado.get_area())
cuadrado.set_side(4)
print (cuadrado.get_diagonal())
print (cuadrado)
print (cuadrado.get_picture())

rectangle1.set_height(8)
rectangle1.set_width(16)
print (rectangle1.get_among_inside('cuadrado'))

