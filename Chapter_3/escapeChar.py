import pyttsx3 #importing 
text = pyttsx3.init() #storing in variable
a = "Escape Sequence Characters are special combinations of characters used inside strings to represent characters that are difficult or impossible to type directly some examples are : "



print("Escape Sequence Characters are special combinations of characters used inside strings to represent characters that are difficult or impossible to type directly")

text.say(a) #line what to speak
text.runAndWait() # run

print("1. Backslash: \\")
print("2. Single quote: I\'m learning Python.")
print("3. Double quote: He said, \"Awesome!\"")
print("4. New Line:\nLine 1\nLine 2")
print("5. Tab: Column1\tColumn2")
print("6. Carriage Return: 12345\rAB")
print("7. Backspace: Hello\bWorld")
print("8. Bell (may beep): \a")
print("9. Vertical Tab: Hello\vWorld")
print("10. Octal (\\141 = a): \141")
print("11. Hex (\\x61 = a): \x61")
