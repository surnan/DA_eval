from urllib.request import urlopen
import re


google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

def print_message(google_doc_url):
    
    page = urlopen(google_doc_url)
    html = page.read().decode("utf-8")

    rows = html.split("<tr")[2:]    # [2:] start populating 'rows' from second element

    print("Number of rows:", len(rows))
    print("1 ======================")
    

    for i, row in enumerate(rows):     #start element 1 (instead of zero) and finish element 5
        values = []

        for column in row.split("<span")[1:]:
            after_gt = column.split(">")[1]
            value = after_gt.split("<")[0]
            values.append(value)

        print(f"values = {values}")

print_message(google_doc_url)
