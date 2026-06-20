from urllib.request import urlopen
import re
import html

def print_secret_message(doc_url):
    page = urlopen(doc_url).read().decode("utf-8")

    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.DOTALL)

    points = []

    for row in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)

        if len(cells) != 3:
            continue

        values = []

        for cell in cells:
            text = re.sub(r"<[^>]+>", "", cell)
            text = html.unescape(text).strip()
            values.append(text)

        try:
            x = int(values[0])
            char = values[1]
            y = int(values[2])
            points.append((x, y, char))
        except:
            pass

    if not points:
        print("No data found.")
        return

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        #grid[y][x] = char
        grid[y][x] = "#"

    print("\n--- OUTPUT ---\n")

    for row in grid:
        print("".join(row))

    with open("output.txt", "w", encoding="utf-8") as f:
        for row in grid:
            f.write("".join(row) + "\n")

    print("\nSaved output to output.txt")


print_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)