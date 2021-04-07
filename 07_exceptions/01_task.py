items = [13, "string", 2.45, 0, "e", True, False, [], {'key': 3}, (), {}]
collected_errors = []

for value in items:
    try:
        result = 10 / value
    except TypeError as e:
        result = 0
        collected_errors.append(e)
    except ZeroDivisionError as e:
        result = 1
        collected_errors.append(e)

    print(result)

for err in collected_errors:
    print(f'- {err}')