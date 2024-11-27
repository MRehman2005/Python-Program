class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    ##make properties for the getter
    @property
    def height(self):
        return f"{self._height}cm"
    @property
    def width(self):
        return f"{self._width}cm"
    #make properties.width and height for setter
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width Must be Greater than 0")
    @height.setter
    def height(self,new_height):
        if new_height>0:
           self._height=new_height
        else:
            print("Height Must be Greater than 0")
rectangle = Rectangle(10,20)
rectangle.width=100
print(rectangle.width)

    