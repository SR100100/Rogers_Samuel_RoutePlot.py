def routePlot(file):
    #initialise grid
    grid = [[" "] * 12 for i in range(12)]
    try:
        route = open(file, "r")
    except OSError:
        print("File not found")
        main()
        
    lines = []
    for line in route:
        lines.append(line.strip('\n'))

    #starting position
    x_co = int (lines[0])-1
    y_co = int (lines[1])-1
    grid[y_co][x_co] = "x"

    for i in range(2,len(lines)):
        if lines[i] == "N" and y_co != 11:
            y_co += 1
            grid[y_co][x_co] = "x"
        elif lines[i] == "E" and x_co != 11:
            x_co += 1
            grid[y_co][x_co] = "x"
        elif lines[i] == "S" and y_co != 0:
            y_co -= 1
            grid[y_co][x_co] = "x"
        elif lines[i] == "W" and x_co != 0:
            x_co -= 1
            grid[y_co][x_co] = "x"
        else:
            print("Error: The route is outside of the grid.")
            break
                
    grid.reverse()      

    for y in range (len(grid)):
        print("{:3}{:}{:}".format((len(grid)-y),": ",' : '.join(grid[y])))
        print("---:---:---:---:---:---:---:---:---:---:---:---:---")
    print("   : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 :10 :11 :12")

def main():
    file = input("Enter file name: ")
    if file != "STOP":
        routePlot(file)
        main()
main()

