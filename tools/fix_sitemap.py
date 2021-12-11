import sys

import pandas as pd
from lxml import etree

if __name__ == "__main__":
    tree = etree.parse(sys.argv[1])
    urls = []

    for row in tree.getroot():
        url = row.getchildren()[0].text.replace("_build/html/book/index.html/", "")
        if "__build" in url:
            continue
        else:
            urls.append({"loc": url})

    df = pd.DataFrame(urls)
    df.to_xml(sys.argv[2], root_name="urlset", index=False, row_name="url")
