def check_Text(fullText, serchString):
    if serchString in fullText:
        print(f"The element contains the {serchString}.")
    else:
        print(f"The element does not contain the search text: {serchString}.")
def print_Text(text):
    print(f"The element contains the {text}")