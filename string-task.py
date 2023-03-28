# For practice, write programs to do the following tasks.
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.
# Be sure to test the case where an empty list [] is passed to your function.

def to_string(spam_list):
    if not spam_list:
        return ""
    result = spam_list[0]
    for index, item in enumerate(spam_list[1:]):
        if index == len(spam_list) - 2:
            result = f'{result}, and {item}'  # 'apples, and tofu'
        else:
            result = f'{result}, {item}'
    return result


def main():
    assert "" == to_string([])
    assert 'apples' == to_string(['apples'])
    assert 'apples, and tofu' == to_string(['apples', 'tofu'])
    assert 'apples, bananas, tofu, and cats' == to_string(['apples', 'bananas', 'tofu', 'cats'])
    assert 'apples, bananas, tofu, cats, and bananas' == to_string(['apples', 'bananas', 'tofu', 'cats', "bananas"])


if __name__ == "__main__":
    main()
