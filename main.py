class Rectangle :
  def __init__(self,widht,height) :
    self.widht = widht
    self.height = height
    
  def set_width (self,new_widht) :
    self.widht = new_widht
    
  def set_height (self, new_height) :
    self.height = new_height
    
  def get_area (self) :
    a = self.widht
    b = self.height
    return a * b
  
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
  
  def __str__(self) :
    return f"Rectangle(widht={self.widht}, height={self.height})"
  
  #pasamos a la segunda parte del programa
  


rectangle1 = Rectangle (10,5)
print (rectangle1.get_area())
rectangle1.set_height(3)
print (rectangle1)
print (rectangle1.get_perimeter())
print (rectangle1.get_picture()) 

