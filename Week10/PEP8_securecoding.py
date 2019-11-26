import re


def get_choice():
    choice = input("Enter encrypt or decrypt: ")
    while not (re.search("encrypt", choice) or re.search("decrypt", choice)):
        print("You entered:", choice, "this is not a valid option")
        choice = input("Enter encrypt or decrypt: ")
    if choice[0] == 'e' or choice[0] == 'E':
        return -3
    else:
        return 3


def do_conversion(inputText, shiftValue):
    resultingText = ""

    inputTextPosition = 0
    while (inputTextPosition < len(inputText)):
        inputTextChar = inputText[inputTextPosition]

        ASCIIValue = ord(inputTextChar)
        ASCIIValue += shiftValue
        resultingText = resultingText + chr(ASCIIValue)
        inputTextPosition += 1

    return resultingText


def write_to_file(resultingText):
    while True:
        try:
            filename = input("Enter a filename:")
            fh = open(filename, "x")
            fh.write(resulting_text)
            fh.close()
            break
        except IOError:
            print("Something went wrong, perhaps file already exists?")


def main():
    shiftValue = get_choice()
    inputText = input('Input text: ')
    resultingText = do_conversion(inputText, shiftValue)
    text_choice = input('Enter \'wf\' to write to file ' +
                        ' or \'ds\' to display on screen: ')
    while not (re.search("wf", text_choice) or re.search("ds", text_choice)):
        print("You entered:", text_choice, "this is not a valid option")
        text_choice = input('Enter \'wf\' to write to file ' +
                            ' or \'ds\' to display on screen: ')
    if text_choice == 'w':
        write_to_file(resultingText)
    else:
        print(resultingText)
main()
