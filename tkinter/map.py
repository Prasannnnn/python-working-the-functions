from tkinter import *
import sys

class App:
    def __init__(self, master):
        self.master = master

        self.frame1 = Frame(master)
        self.frame1.pack()
        self.frame2 = Frame(master)
        self.frame2.pack()

        # real grid size = 10
        # map editor grid size = 10 x 2
        self.gridSize = 20
        self.WID = 400
        self.HEI = 300

        if len(sys.argv) > 1:
            geoStr = sys.argv[1]
            geoStr_splited = geoStr.split("x")
            self.WID = int(geoStr_splited[0])
            self.HEI = int(geoStr_splited[1])

        self.vGrid = int(self.HEI / self.gridSize)
        self.hGrid = int(self.WID / self.gridSize)

        self.canvas = Canvas(self.frame1, width=self.WID, height=self.HEI)
        self.canvas.bind("<B1-Motion>", self.changeGridColor)
        self.canvas.bind("<Button-1>", self.changeGridColor)
        self.canvas.pack()

        self.grids = [[0 for _ in range(self.hGrid)] for _ in range(self.vGrid)]
        self.drawGrid()

        self.colorToDraw = "#333"
        self.toggleButton = Button(self.frame2, text="Toggle", command=self.toggleColor)
        self.toggleButton.grid(row=0, column=0)

        self.saveButton = Button(self.frame2, text="Save", command=self.saveGrid)
        self.saveButton.grid(row=0, column=1)

    def drawGrid(self):
        gLen = self.gridSize
        for i in range(self.vGrid):
            y = i * gLen
            for j in range(self.hGrid):
                x = j * gLen
                self.grids[i][j] = self.canvas.create_rectangle(x, y, x + gLen, y + gLen, fill="#efefef")

    def toggleColor(self):
        if self.colorToDraw == "#333":
            self.colorToDraw = "#efefef"
        else:
            self.colorToDraw = "#333"

    def changeGridColor(self, event):
        gLen = self.gridSize
        x = int(event.x / gLen)
        y = int(event.y / gLen)
        if 0 <= x < self.hGrid and 0 <= y < self.vGrid:  # Check if the coordinates are within the grid bounds
            self.canvas.itemconfig(self.grids[y][x], fill=self.colorToDraw)

    def countNeighbors(self, stateGrids, i, j):
        count = 0
        sideStr = ""
        fourSide = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
        for x in range(4):
            ni, nj = fourSide[x]
            if 0 <= ni < len(stateGrids) and 0 <= nj < len(stateGrids[0]):
                if stateGrids[ni][nj] != 0:
                    count += 1
                    sideStr += "1"
                else:
                    sideStr += "0"
            else:
                sideStr += "0"
        return (count, sideStr)

    def saveGrid(self):
        stateGrids = [[0 for i in range(self.hGrid)] for j in range(self.vGrid)]
        realGrids = [[0 for i in range(self.hGrid * 2)] for j in range(self.vGrid * 2)]

        for i in range(self.vGrid):
            for j in range(self.hGrid):
                fillColor = self.canvas.itemcget(self.grids[i][j], "fill")
                if fillColor == "#333":
                    stateGrids[i][j] = 1

        # dictionary for road
        roadDict = {
            "0001": "SNCC",
            "0010": "WCEC",
            "0100": "CCSN",
            "1000": "CWCE",
            "1010": "WWEE",
            "0101": "SNSN",
            "1100": "SWSE",
            "1001": "SNEE",
            "0110": "WWSN",
            "0011": "WNEN"
        }

        for i in range(self.vGrid):
            for j in range(self.hGrid):
                roadType = "%%%%"
                if stateGrids[i][j] == 1:
                    count, sideStr = self.countNeighbors(stateGrids, i, j)
                    if count >= 3:
                        roadType = "IIII"
                    elif sideStr in roadDict:
                        roadType = roadDict[sideStr]
                realGrids[i * 2][j * 2] = roadType[0]
                realGrids[i * 2 + 1][j * 2] = roadType[2]
                realGrids[i * 2][j * 2 + 1] = roadType[1]
                realGrids[i * 2 + 1][j * 2 + 1] = roadType[3]

        for i in range(self.vGrid * 2):
            for j in range(self.hGrid * 2):
                sys.stdout.write(realGrids[i][j])
            sys.stdout.write("\n")

        self.master.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title("Map Editor v1.0")
    app = App(root)
    root.mainloop()
