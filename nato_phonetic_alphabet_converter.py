# NATO Phonetic Alphabet Converter

# NATO phonetic alphabet dictionary
nato_phonetic_dict = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

def convert_to_nato(phrase):
    phrase = phrase.upper()
    nato_translation = []

    # To-Do: Write a loop to iterate through each character in the input phrase
    # To-Do: Check if the character is an alphabet letter
    # To-Do: Append the corresponding NATO word to the translation list
    # To-Do: Check if the character is a digit and append it to the translation list
    

    # Ignore spaces and special characters
    return ' '.join(nato_translation) 

def main():
    # To-Do: Prompt the user for input
    # To-Do: Convert the input to NATO phonetic alphabet
    # To-Do: Print the translation

    # TO-DO: Save the output to a text file
            
            # To-Do: Inform the user that the translation has been saved

    # Read from an input file and translate its content
        # To-Do: Prompt the user for the input file name
        # To-Do: Implement a try-except block to handle file not found errors
        # To-Do: Open the input file
            # To-Do: Read the content of the file
            # To-Do: Convert the file content to NATO phonetic alphabet
            # To-Do: Print the file translation
            # To-Do: Handle the file not found error
            # To-Do: Inform the user that the file was not found

    if __name__ == "__main__":
        main()