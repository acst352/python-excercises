# Does replace only work with words or also phrases?
string = "Does replace only work with words or also phrases?"
modified_string_word = string.replace("words", "phrases")
modified_string_phrase = string.replace(
    "Does replace only work with words or also phrases?", "No, but yes :)"
)
print(modified_string_word)
print(modified_string_phrase)