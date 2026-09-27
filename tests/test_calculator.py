from calculator import calculate_total


def test_total_marks():
    subject = {
        "name": "Problem Solving and Programming",
        "code": "CSE1021",
        "cat1": 40,
        "cat2": 42,
        "tee": 75
    }

    assert calculate_total(subject) == 157

def test_total_marks_with_zero():
    subject = {
        "name": "Python",
        "code": "CSE1021",
        "cat1": 0,
        "cat2": 0,
        "tee": 0
    }

    assert calculate_total(subject) == 0