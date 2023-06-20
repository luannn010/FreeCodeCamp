from time_calculator import add_time


def test_add_time():
    assert add_time("11:11 AM", "12:22") == "11:33 PM"
    assert add_time("03:30 AM", "04:45") == "8:15 AM"
def test_next_day():
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
    assert add_time("13:20 PM", "10:30") == "11:50 AM (next day)"
def test_n_days():
    assert add_time("12:10 PM", "30:50") == "7:00 AM (2 days later)"
    assert add_time("9:10 PM", "50:50") == "12:00 AM (3 days later)"
def test_date():
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"
    assert add_time("11:30 PM", "2:32", "Wednesday") == "2:02 AM, Thursday (next day)"

