def drawTop():
    for i in range(4):
        print("-", end = " ")

def drawSide():
        print("|         ", end = "")
        
def drawFirstCorner():
    print("+", end = " ")
    
def drawLastCorner():
    print("+")
    
def draw_grid(n):
    for i in range(n):
        for i in range(n):
            drawFirstCorner()
            drawTop()
        drawLastCorner()
        for i in range(4):
            for i in range(n+1):
                drawSide()
            print("")
    for i in range(n):
        drawFirstCorner()
        drawTop()
    drawLastCorner()

if __name__ == "__main__":
    size = int(input("Enter grid size:"))
    draw_grid(size)