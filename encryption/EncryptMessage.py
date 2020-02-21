from Encryption import Encryption


class EncryptMessage:

    # ord() function gets the integer value of a character, chr returns a character from the integer value, extends encryption to punctuation.
    def format_message(self, message):
        message_ints = [ord(character) for character in message]
        return message_ints

    def unformat_message(self, message):
        message_str = ""
        for i in range(len(message)):
            message_str += chr(message[i])
        return message_str


instance = EncryptMessage()
encrypt = Encryption()

formatted_message = instance.format_message("hello, world!")
encrypted_message = encrypt.encryption(formatted_message)
encrypted_unformatted_message = instance.unformat_message(encrypted_message)
unencrypted_message = encrypt.decryption(encrypted_message)
formatted_unencrypted_message = instance.unformat_message(unencrypted_message)

print(formatted_message)
print(encrypted_message)
print(encrypted_unformatted_message)
print(unencrypted_message)
print(formatted_unencrypted_message)
