import requests
from pydash import camel_case
import pandas as pd
from tabulate import tabulate


def define_single_word(word) -> None | list:
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if response.status_code != 200:
        print(response.json()["message"])
        return None
    response_data = response.json()
    return_data = []
    item_counter = 1
    for item in response_data:
        print(f"Source #{item_counter}")
        for _, definition in item.items():
            if _ == 'meanings':
                for definition_item in definition:
                    for definition_subitem in definition_item['definitions']:
                        print(f"({camel_case(definition_item['partOfSpeech'])}) {definition_subitem["definition"]}")
                        example = ""
                        if 'example' in definition_subitem.keys():
                            print(f"Example: {definition_subitem['example']}")
                            example = definition_subitem['example']

                        if input(" -- wanna save for note-taking? ").lower() == "yes":
                            return_data.append({
                                "part of speech": definition_item['partOfSpeech'],
                                "word": word,
                                "definition": definition_subitem['definition'],
                                "example": example
                            })
                            print("amazing, saved in the buffer, ready for note-taking!")
                        print()
        item_counter += 1
    return return_data


def words_guessing(words_data) -> int:
    entry = words_data.sample(n=1).iloc[0]
    part_of_speech = entry['part of speech']
    definition = entry['definition']
    answer = entry['word'].lower()
    example = entry['example'] if pd.notna(entry['example']) else "No example available."

    print(f"\nGuess the word!")
    table = [
        ["Part of Speech", part_of_speech],
        ["Definition", definition]
    ]
    print(tabulate(table, headers=["Info", "Value"], tablefmt="fancy_grid"))

    guess = input("Your guess: ").strip().lower()
    if guess == answer:
        print("🎉 Correct!\n")
        return 1
    else:
        print(f"❌ Incorrect. The word was: **{answer}**\n")
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{answer}")
    if response.status_code == 200:
        synonyms = response.json()[0]["meanings"][0]["definitions"][0]["synonyms"]
        len_synonyms = len(synonyms)
        if len_synonyms > 0:
            print("Synonyms: ", end="")
            for item in synonyms:
                print(item, ",", end=", ")
    print(example)
    return 0


df = pd.read_csv('vocabulary.csv')
prompt = input("Wanna upgrade vocab? : ").lower()
while prompt != 'no':
    current_df = define_single_word(input("Word: "))

    if current_df is not None:
        current_df = pd.DataFrame(current_df)
        wants_note = input("Do you want to keep notes updated to the file? (Yes/No): ")
        if wants_note.lower() == 'yes':
            current_df.to_csv('vocabulary.csv', mode='a', header=False, index=False)
            print("Note saved!")
    prompt = input("Continue? (Yes/No): ").lower()


practice_prompt = input("Amazing! Now, do you want to practice? (Yes/No) ")
total_words = 0
guessed_words = 0
while practice_prompt.lower() != 'no':
    total_words += 1
    guessed_words += words_guessing(df)
    print(f"{guessed_words}/{total_words} words guessed. It is {round((guessed_words/total_words)*100,2)}%")
    practice_prompt = input(" -- Wanna play again (if no - game ends): ").strip().lower()
    if practice_prompt == 'no':
        print("Thanks for playing!")
        break

print("Have a wonderful day!")
