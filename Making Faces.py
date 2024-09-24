def main():
    # Get user input
    msg = input("Enter your message: ")

    # Call convert function
    result = convert(msg)

    # Print the result
    print(result)

def convert(msg):
    # Replace :) with happy emoji and :( with sad emoji
    msg = msg.replace(":)", '😊')
    msg = msg.replace(":(", '😞')

    # Return the modified string
    return msg

main()
