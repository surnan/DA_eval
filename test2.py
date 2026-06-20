from urllib.request import urlopen
import re

def print_secret_message(doc_url):
    html = urlopen(doc_url).read().decode("utf-8")

    cells = re.findall(r"<td[^>]*>(.*?)</td>", html)
    clean = [re.sub("<.*?>", "", c).strip() for c in cells]

    points = []
    for i in range(0, len(clean), 3):
        try:
            x = int(clean[i])
            char = clean[i + 1]
            y = int(clean[i + 2])
            points.append((x, y, char))
        except:
            pass

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")