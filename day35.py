def handle_request(method):
    if method == "GET":
        return "Viewing car inventory"

    elif method == "POST":
        return "Adding a new car"

    elif method == "PUT":
        return "Updating car details"

    elif method == "DELETE":
        return "Deleting a car"
    else:
        return "Unknown HTTP method"


method = input("Enter HTTP method:").strip().upper()

result = handle_request(method)

print(result)