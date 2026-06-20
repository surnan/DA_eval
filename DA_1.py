from urllib.request import urlopen
import re


google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

def print_message(google_doc_url):
    
    page = urlopen(google_doc_url)
    html = page.read().decode("utf-8")

    rows = html.split("<tr")[2:]    # [2:] start populating 'rows' from second element

    print("======================")
    print("======================")
    print("Number of rows:", len(rows))
    print("======================")

    max_x = 0
    max_y = 0
    points = []

    for i, row in enumerate(rows):     #start element 1 (instead of zero) and finish element 5
        values = []

        for column in row.split("<span")[1:]:
            after_gt = column.split(">")[1]
            value = after_gt.split("<")[0]
            values.append(value)

        # print(f"values = {values}")

        x = int(values[0])
        char = values[1]
        y = int(values[2])
        
        points.append((x,char,y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    grid = []

    for y in range(max_y + 1):
        row = []

        for x in range(max_x + 1):
            row.append(" ")

        grid.append(row)

    for x, char, y in points:
        grid[y][x] = char
    
    # for temp in range(max_x+1):
    #     grid[0][temp] = "S"
    #     grid[1][temp] = "T"
    #     grid[2][temp] = "V"
    #     grid[3][temp] = "W"
    #     grid[4][temp] = "X"
    #     grid[5][temp] = "Y"
    #     grid[6][temp] = "Z"

    
    # grid[0][0] = "!"
    # grid[6][0] = "@"

    # grid[0][max_x] = "#"
    # grid[6][max_x] = "$"





    # for row in grid:
    for row in reversed(grid):
        print("".join(row))
    
    print(f"max_x = {max_x}")
    print(f"max_y = {max_y}")

print_message(google_doc_url)
