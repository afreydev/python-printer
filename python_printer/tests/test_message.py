from python_printer import printer


def test_print_message():
    message = "Hello Angel!"
    formatted_message = f"This is printing this: {message}"
    assert formatted_message == printer.print_this_message(message)
