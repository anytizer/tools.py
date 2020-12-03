from CAPITALIZER import CAPITALIZER

cap = CAPITALIZER()

if __name__ == "__main__":
    c = cap.capitalize('id')
    d = cap.capitalize('country')
    e = cap.capitalize('country_id')
    assert c == "ID", "Not capitalized properly"
    assert d == "Country", "Wrongly capitalized"
    assert e == "Country ID", "Splitting not managed"

    print(c, d, e, sep=" | ")
