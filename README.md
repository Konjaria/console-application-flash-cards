# 🧠 Vocabulary Builder & Practice Tool

Boost your vocabulary in a fun and simple way!  
This tool helps you:

- 📖 Look up new words  
- ✍️ Save and review definitions  
- 🎯 Practice guessing words  
- 📊 Track your progress  

---

## ✨ What You Can Do

- ✅ Find word meanings and example sentences  
- ✅ Save words to your personal vocabulary file  
- ✅ Practice by guessing words based on definitions  
- ✅ Get feedback and learn from your mistakes  
- ✅ View synonyms if you answer incorrectly  

---

## 📥 How to Get Started (Step-by-Step)

### 🔹 Step 1: Download the Tool

1. Click the green **"Code"** button on the repository page (top right)  
2. Select **"Download ZIP"**  
3. Once downloaded, **unzip the folder**  
   - Right-click → "Extract All" on Windows  
   - Double-click on Mac  

You’ll now see a folder with several files inside — including `main.py`.

---

### 🔹 Step 2: Install Python (if not already installed)

If you're unsure whether Python is installed:

- Open a terminal (Command Prompt on Windows or Terminal on Mac)  
- Type:

  ```bash
  python --version
  ```
- If it shows a version like `Python 3.11.5`, you're good to go.  
- If not, download and install Python from [https://www.python.org/downloads](https://www.python.org/downloads)

---

### 🔹 Step 3: Install Required Tools

Only once — run this in your terminal:

```bash
pip install requests pydash pandas tabulate
```
This command installs the necessary Python packages that the tool needs to work properly.

---

### 🔹 Step 4: Run the Tool

1. Open the folder you just unzipped.
2. Double-click the file named **`main.py`** to run it.  
   *(If that doesn’t work, open your terminal or command prompt, navigate to the folder, and type:)*

   ```bash
   python main.py
   ```
---

## 🧩 How It Works

### 📘 Add New Words

When prompted:

```
Wanna upgrade vocab? :
```

- Type `yes` to look up and add new words.  
- Type `no` to skip directly to practice mode.

For each word you enter:

- The tool will display its definitions, parts of speech, and example sentences.  
- You can choose whether to save the word for later practice.  
- Saved words are stored in your personal vocabulary file (`vocabulary.csv`).

---

### 🧠 Practice Mode

After adding words or skipping, you'll see:

```
Amazing! Now, do you want to practice? :
```

- Type `yes` to start practicing.  
- The program will show a word’s definition and part of speech.  
- Try to guess the word based on the clues.  
- You’ll receive immediate feedback:
  - ✅ Correct guesses will be acknowledged.  
  - ❌ Incorrect guesses will reveal the correct word and synonyms.  
- Your score will update with each guess.

---

## 📁 Where Your Words Are Stored

All saved words are stored in: vocabulary.csv

Each entry contains:

- The word  
- Its meaning  
- Part of speech  
- Example sentence  

You can open this file using Excel, Google Sheets, or any text editor.

---

## 💡 Coming Soon (Future Features)

Planned improvements include:

- Difficulty levels (easy, medium, hard)  
- A review mode for focused learning  
- A simple visual interface (no typing needed!)  
- Score streaks and detailed performance tracking  

---

## 🤝 Want to Contribute?

If you're familiar with Python, contributions and suggestions are welcome! Feel free to submit pull requests or open issues.

---

## ❓ Need Help?

If you have any questions or run into issues, don’t hesitate to ask for help.  
You don’t need to be a tech expert to use this tool!
