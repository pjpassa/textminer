import re
if __name__ == "__main__":
    import validator as v
else:
    import textminer.validator as v


def words(test_string):
    if v.words(test_string):
        return test_string.split(" ")


def phone_number(test_string):
    if v.phone_number(test_string):
        match = re.search(r'.*(\d{3}).*(\d{3}).*(\d{4})', test_string)
        return {"area_code": match.group(1),
                "number": "{}-{}".format(match.group(2), match.group(3))}


def money(test_string):
    if v.money(test_string):
        test_string = re.sub(",", "", test_string)
        return {"currency": test_string[0], "amount": float(test_string[1:])}


def zipcode(test_string):
    if v.zipcode(test_string):
        zip5 = re.search(r'^\d{5}', test_string).group(0)
        plus4 = None
        if re.search(r'-\d{4}$', test_string):
            plus4 = re.search(r'\d{4}$', test_string).group(0)
        return {"zip": zip5, "plus4": plus4}


def date(test_string):
    if v.date(test_string):
        year = re.search(r'\d{4}', test_string).group(0)
        test_string = re.sub(r'\d{4}', "", test_string)
        month_day = re.search(r'(\d{1,2})[-/](\d{1,2})', test_string)
        return {"month": int(month_day.group(1)),
                "day": int(month_day.group(2)),
                "year": int(year)}


if __name__ == "__main__":
    print(date("1976-09-04"))
