import model

message = "SOS We have hit an iceberg and need help quickly"

# `morse` is a list which will eventually contain the 
# strings for each morse code letter in the message.

print(f"Incoming message: {message}")
print(f"   Morse encoded: {model.encode(message)}")

message2 = '... . -.-. .-. . - / -- . ... ... .- --. .'

print(f'decode: {model.decode(message2)}')