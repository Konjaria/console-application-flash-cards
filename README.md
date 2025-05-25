# Vocabulary Builder and Practice Tool

This Python script helps you expand your vocabulary by allowing you to look up word definitions, save them for later review, and practice guessing the words based on their definitions.
![image](https://github.com/user-attachments/assets/aa885683-b873-4802-8634-c4c30e5c88cb)
![image](https://github.com/user-attachments/assets/46a99a26-78da-401a-a901-60ad1370afed)


## Features

* **Word Definition Lookup:** Uses the [Free Dictionary API](https://dictionaryapi.dev/) to fetch definitions, part of speech, and example sentences for a given word.
* **Note-Taking:** You can choose to save the word, its part of speech, definition, and example to a `vocabulary.csv` file for future reference.
* **Vocabulary Practice:** Presents you with definitions and parts of speech of words from your saved `vocabulary.csv` file and allows you to guess the word.
* **Score Tracking:** Keeps track of the number of words you've guessed correctly and displays your current score as a percentage.
* **Synonym Display:** If you guess a word incorrectly, the script attempts to fetch and display synonyms for that word.

## Prerequisites

* **Python 3.x** installed on your system.
* **Required Python Libraries:**
    * `requests`: For making HTTP requests to the dictionary API.
    * `pydash`: For converting strings to camel case.
    * `pandas`: For working with data in a tabular format (CSV file).
    * `tabulate`: For creating nicely formatted tables in the console.

    You can install these libraries using pip:
    ```bash
    pip install requests pydash pandas tabulate
    ```

## Setup

1.  **Clone the repository** (if you have one) or **save the Python script** (`your_script_name.py`) to your local machine.
2.  **Ensure `vocabulary.csv` exists:** The script will automatically create this file if it doesn't exist when you start saving words.

## How to Use

1.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
2.  **Upgrade Vocabulary:**
    * The script will first ask: `Wanna upgrade vocab? :`. Type `yes` to look up and save new words, or `no` to skip this step.
    * If you choose `yes`, you will be prompted to enter a `Word:`.
    * The script will then display the definitions, part(s) of speech, and example sentences for the word.
    * For each definition, you'll be asked: `-- wanna save for note-taking?`. Type `yes` to save the word details or `no` to skip.
    * You'll then be asked: `Do you want to keep notes updated to the file? (Yes/No):`. Type `yes` to append the saved words to `vocabulary.csv`.
    * Finally, you'll be asked: `Continue? (Yes/No):`. Type `yes` to look up more words or `no` to proceed to the practice session.
3.  **Practice:**
    * After the vocabulary upgrade phase (or if you chose `no` initially), the script will ask: `Amazing! Now, do you want to practice? (Yes/No)`. Type `yes` to start practicing.
    * You will be presented with a definition and part of speech of a randomly selected word from your `vocabulary.csv` file.
    * Enter your guess: `Your guess:`.
    * The script will tell you if your guess is correct or incorrect. If incorrect, it will display the correct word and attempt to show synonyms.
    * Your current score will be displayed.
    * You'll be asked: `-- Wanna play again (if no - game ends):`. Type `yes` to continue practicing or `no` to end the session.

## Data Storage

The vocabulary words you choose to save are stored in a simple CSV file named `vocabulary.csv`. Each row in this file represents a saved word and contains the "part of speech", "word", "definition", and "example".

## Potential Improvements

* **More sophisticated scoring:** Implement different scoring methods or track streaks.
* **Difficulty levels:** Allow users to filter words based on difficulty.
* **Review mode:** Implement a mode to specifically review previously saved words and their details.
* **Error handling:** Add more robust error handling for API requests and file operations.
* **User interface:** Consider using a graphical user interface (GUI) for a more interactive experience.
* **Word categories:** Allow users to categorize words.

## Contributing

Contributions to this project are welcome! Feel free to submit pull requests with bug fixes or new features.