from urllib.request import urlopen


def print_message(google_doc_url):

    max_x = 0
    max_y = 0
    points = [] # Array of x-coord, char, y-coord
    grid = []   # 2d Array returning to user

    page = urlopen(google_doc_url)
    html = page.read().decode("utf-8")
    rows = html.split("<tr")[2:]    # First row is table header.  Not data


    for row in rows:     #start element 1 (instead of zero) and finish element 5
        values = []

        for column in row.split("<span")[1:]:
            after_gt = column.split(">")[1]
            value = after_gt.split("<")[0]
            values.append(value)

        x = int(values[0])
        char = values[1]
        y = int(values[2])
        
        points.append((x,char,y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    

    # Create 2D array with every cell blank of maximum x & y
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(" ")
        grid.append(row)

    # Update grid with points array
    for x, char, y in points:
        grid[y][x] = char
    

    # for row in grid:
    for row in reversed(grid):
        print("".join(row))
    
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_message(google_doc_url)
