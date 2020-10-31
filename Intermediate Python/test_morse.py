import morse

message = 'sos ahahahaha'

code = morse.encode(message)
decode = morse.decode(code)

print(message == decode)