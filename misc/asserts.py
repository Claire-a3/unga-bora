def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "empty string"
assert count_upper_case("T") == 1,  "1 UC"
assert count_upper_case("a") == 0, "1 char no UC"
assert count_upper_case("!@##$%#&%^&#") == 0, "SPecial character"

print("All tests passed")