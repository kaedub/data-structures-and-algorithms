def gather_strings(obj):
    strings = []
    for k,v in obj.items():
        if isinstance(v, dict):
            strings.extend(gather_strings(v))
        elif isinstance(v, str):
            strings.append(v)
    return strings

nested_obj = {
    'firstName': 'Lester',
    'favoriteNumber': 22,
    'moreData': {
        'lastName': 'Testowitz'
    },
    'funFacts': {
        'moreStuff': {
            'anotherNumber': 100
        },
        'favoriteString': 'nice!'
    }
}

nested_obj2 = {
    'firstName': 'Lester',
    'favoriteNumber': 'not a number',
    'moreData': {
        'lastName': 'Tester'
    },
    'funFacts': {
        'moreStuff': {
            'anotherNumber': '24 is a number'
        },
        'favoriteString': 'nice!'
    }
}

nested_obj3 = {}


print(gather_strings(nested_obj))
print(gather_strings(nested_obj2))
print(gather_strings(nested_obj3))