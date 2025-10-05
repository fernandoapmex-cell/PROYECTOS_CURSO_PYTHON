class Color:
    def __init__(self, color):
       self._color = color
    def setColor(self, color):
        self._color = color
    def getColor(self):
        return self._color
    def __str__(self):
        return f'Color: {self._color}'