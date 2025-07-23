import Magic8Ball as m

userHasQuestions = True

while userHasQuestions:
    print("Ask the magic 8 ball a question: ")
    input()
    m.magic8Ball()
    print("\nDo you have any more questions? (Y/N) ")
    a = input().upper()
    if a != 'Y':
        userHasQuestions = False