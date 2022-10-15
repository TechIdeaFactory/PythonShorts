
# pip3 install wikipedia-api

import wikipediaapi

wiki = wikipediaapi.Wikipedia("en")

while True:
    req_info = input(
        "Please enter a subject or name"
        " to look up in wikipedia or Q to quit"
    )

    if req_info.lower().strip() == "q":
        break
    else:
        page_py = wiki.page(
            req_info
        )
        if page_py.exists():
            print(
                "Page - Summary: %s"
                % page_py.summary
            )
        else:
            print(
                "Unable to find page on Wikipedia "
                + "for " + req_info
            )



