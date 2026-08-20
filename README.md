# 💧 Hydration Habit Tracker

A simple desktop app built with **Python** and **PyQt5** that helps you track how much water you've been drinking and gives you friendly feedback with emojis. This was my first project — built to learn GUI programming with PyQt5!

---

## 📋 What It Does

You type in how many cups of water you've had today, click **"Get advice"**, and the app responds with an emoji and a short message telling you whether you need to drink more, you're doing great, or you've had too much.

---

## 🛠️ Built With

- **Python 3**
- **PyQt5** — for building the graphical user interface (GUI)

---

## 📦 Installation

1. Make sure Python 3 is installed.
2. Install PyQt5:
   ```bash
   pip install PyQt5
   ```
3. Run the app:
   ```bash
   python Water_project.py
   ```

---

## 🧠 How the Code Works

### 1. Imports

```python
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
```

**Significance:** PyQt5 is split into modules. `QtWidgets` has all the visual building blocks (windows, buttons, text boxes, labels), and `QtCore` has core, non-visual functionality — here it's used for `Qt.AlignCenter`, which controls text alignment.

---

### 2. The Main Window Class

```python
class HabitApp(QWidget):
    def __init__(self):
        super().__init__()
```

**Significance:** Every PyQt5 app needs at least one `QWidget` (or a subclass of it) to act as a window. By inheriting from `QWidget`, `HabitApp` *becomes* a window and automatically gets all of `QWidget`'s built-in behavior (showing, resizing, closing, etc.). `super().__init__()` runs `QWidget`'s own setup code before you add your own.

---

### 3. Creating the Widgets

```python
self.water_label = QLabel("Enter amount of water you drank (cups): ", self)
self.water_amount_input = QLineEdit(self)
self.advice_button = QPushButton("Get advice", self)
self.emoji_label = QLabel("💧😊 ")
self.description_label = QLabel("Getting hydrated enough?")
```

**Significance:** These are the actual pieces the user sees and interacts with:
- `QLabel` → displays text (instructions, emoji, description)
- `QLineEdit` → a text box where the user types their water intake
- `QPushButton` → a clickable button that triggers the advice logic

Storing them as `self.xxx` (instance attributes) is important — it lets you access and update them later from *any* method in the class, like `give_advice()`.

---

### 4. Connecting the Button to a Function (Signals & Slots)

```python
self.advice_button.clicked.connect(self.give_advice)
```

**Significance:** This is PyQt5's **signal and slot** system — the heart of how GUIs respond to user actions. `clicked` is a *signal* emitted whenever the button is pressed, and `.connect()` tells PyQt5 to run `self.give_advice` (the *slot*) whenever that signal fires. Without this line, clicking the button would do nothing.

---

### 5. Laying Out the Widgets

```python
vbox = QVBoxLayout()
vbox.addWidget(self.water_label)
vbox.addWidget(self.water_amount_input)
vbox.addWidget(self.advice_button)
vbox.addWidget(self.emoji_label)
vbox.addWidget(self.description_label)
self.setLayout(vbox)
```

**Significance:** `QVBoxLayout` stacks widgets vertically, one below the other, and automatically handles spacing and resizing so you don't have to manually calculate pixel positions. `self.setLayout(vbox)` applies this layout to the window itself.

---

### 6. Styling with a Stylesheet (CSS-like syntax)

```python
self.setStyleSheet("""
    QLabel#water_label{
        font-size: 40px;
        font-style: italic;
    }
""")
```

**Significance:** PyQt5 supports **Qt Style Sheets (QSS)**, which work a lot like CSS. Setting `setObjectName("water_label")` on a widget lets you target that *specific* widget with `#water_label` in the stylesheet, rather than styling every `QLabel` the same way. This is what gives each widget its own custom font size and style.

---

### 7. The Core Logic — `give_advice()`

```python
def give_advice(self):
    text = self.water_amount_input.text()

    try:
        amount = float(text)
    except ValueError:
        self.emoji_label.setText("⚠️")
        self.description_label.setText("Please enter a valid number!")
        return

    if amount <= 4:
        self.emoji_label.setText("😞")
        self.description_label.setText("Please drink more water!")
    elif amount <= 9:
        self.emoji_label.setText("😄")
        self.description_label.setText("You're doing great, keep it up!")
    elif amount > 10:
        self.emoji_label.setText("😳")
        self.description_label.setText("Chill out dude too much hydration")

    self.water_amount_input.clear()
```

**Significance:** This is the "brain" of the app.
- `self.water_amount_input.text()` reads whatever the user typed (always returns a **string**).
- The `try/except ValueError` block protects the app from crashing if the user types something that isn't a number (like "abc"). This is a simple but important form of **input validation**.
- The `if/elif` chain compares the number to set ranges and updates the emoji/description labels accordingly, giving the user instant visual feedback.
- `self.water_amount_input.clear()` resets the input box so it's ready for the next entry.

> ⚠️ **Small bug to be aware of:** the range `4 < amount <= 9` covers 5–9, and `amount > 10` only fires above 10 — so entering exactly `10` won't match any condition and the labels won't update. You could fix this by changing the last check to `elif amount > 9:`.

---

### 8. Running the App

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Habit_app = HabitApp()
    Habit_app.show()
    sys.exit(app.exec_())
```

**Significance:**
- `QApplication` manages the overall application (event loop, settings, etc.) — every PyQt5 app needs exactly one.
- `Habit_app.show()` makes the window visible (widgets are hidden by default until shown).
- `app.exec_()` starts the **event loop**, which continuously listens for things like clicks and keypresses. `sys.exit()` ensures the app closes cleanly with the correct exit code.
- The `if __name__ == "__main__":` guard ensures this code only runs when the file is executed directly, not if it's imported elsewhere.

---

## 🚀 Possible Improvements

- Fix the `amount == 10` edge case mentioned above
- Add a daily goal/progress bar
- Save water intake history to a file
- Add unit selection (cups, liters, oz)

---

## 📖 What I Learned

Building this project taught me the fundamentals of:
- Creating GUI windows and widgets with PyQt5
- Using layouts to organize the interface
- Handling user input and validating it
- Connecting signals (events) to functions (slots)
- Styling widgets with Qt Style Sheets
