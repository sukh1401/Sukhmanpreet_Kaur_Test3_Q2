
class Rectangle:
    def _init_(self):
        pass

    def start(self):

        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the Width of the rectangle: "))
        results = self.getPerimeter(length, width)
        print("\n")
        self.showResults('Perimeter', results)
        print("\n")
        results = self.getArea(length, width)
        self.showResults('Area', results)
        print("\n")

    def getPerimeter(self, length, width):
        return 2*(length+width)

    def getArea(self, length, width):
        return length*width

    def showResults(self, action, results):
        print(action, " of rectangle is :::::: %.2f " % results)


if __name__ == "__main__":
    app = Rectangle()
    app.start()