import string

# Display the instructions
print("\n\t\t\tWelcome to CodeCrypt Cipher Encoder and Decoder!")
print("\t\t\t================================================")
print("\t\t\t\t\t\t\tInstructions: ")
print("\n- This program allows you to encode and decode messages using a shift cipher.")
print("- Enter 'encode' to encode a message, or 'decode' to decode a message.")
print("- For the shift value, enter a positive integer.")
print(
    "- If you choose to encode a message, each letter in the message will be shifted by the specified amount in the forward direction.")
print(
    "- If you choose to decode a message, each letter in the message will be shifted by the specified amount in the backward direction.")
print("- For example, with a shift of 3: 'a' becomes 'd' when encoding and 'd' becomes 'a' when decoding.")
print("- Non-alphabetic characters will remain unchanged in the encoded/decoded message.")
print("- To continue using the program, type 'continue'. To end the program, type 'end'.")
print("\n\t\t\t================================================")


# Function to process text according to the chosen cipher direction and shift
def text_processing(cipher_direction, start_text, shift):
    alphabets = list(string.ascii_lowercase)
    end_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for char in start_text:
        if char in alphabets:
            old_index = alphabets.index(char)
            new_index = (old_index + shift) % len(alphabets)
            end_text += alphabets[new_index]
        else:
            end_text += char
    print(f"\nMessage {cipher_direction}d successfully! "
          f"\n{cipher_direction.capitalize()}d message: " + end_text)


# Main program loop
should_continue = True
while should_continue:
    # Ask the user to choose encoding or decoding
    direction = input("\nType 'encode' to encode a message, type 'decode' to decode a message: ").lower()

    # Process the user's choice
    if direction == "encode" or direction == "decode":
        user_input = input("Enter a message to " + direction + ": ").lower()
        shift_amount = int(input("Enter the shift: "))
        text_processing(direction, user_input, shift_amount)
    else:
        print("Invalid input. Please make sure you are using the correct spellings i.e 'encode' or 'decode'.")

    # Ask if the user wants to continue or end the program
    check = True
    while check:
        choice = input("\nType 'continue' if you want to continue, type 'end' to end the program: ").lower()
        if choice == "continue":
            check = False
        elif choice == "end":
            print("Program ended. Thanks for using the CodeCrypt Cipher Encoder and Decoder. Have a good day!")
            check = False
            should_continue = False
        else:
            print("Invalid input. Please make sure you are using the correct spellings i.e 'continue' or 'end'.")
