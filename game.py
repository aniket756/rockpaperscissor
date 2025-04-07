import tkinter as tk
import random
import platform
import os

# Sound playback (optional)
def play_sound(result):
    if platform.system() == "Windows":
        import winsound
        sounds = {
            "win":  winsound.MB_ICONASTERISK,
            "lose": winsound.MB_ICONHAND,
            "tie":  winsound.MB_ICONQUESTION
        }
        winsound.MessageBeep(sounds[result])
    elif platform.system() == "Darwin":
        # macOS - uses `afplay`
        if result == "win":
            os.system("afplay /System/Library/Sounds/Glass.aiff &")
        elif result == "lose":
            os.system("afplay /System/Library/Sounds/Basso.aiff &")
        elif result == "tie":
            os.system("afplay /System/Library/Sounds/Pop.aiff &")

# Game logic
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "user" if wins[user] == computer else "computer"

def play(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"You: {emojis[user_choice]} ({user_choice})")
    computer_choice_label.config(text=f"Computer: {emojis[computer_choice]} ({computer_choice})")

    if result == "tie":
        result_label.config(text="🤝 It's a tie!", fg="gray")
        play_sound("tie")
    elif result == "user":
        result_label.config(text="🎉 You win!", fg="green")
        user_score += 1
        play_sound("win")
    else:
        result_label.config(text="💻 Computer wins!", fg="red")
        computer_score += 1
        play_sound("lose")

    score_label.config(text=f"Score 🧍‍♂️ {user_score} : {computer_score} 🤖")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="👊 Choose your move!", fg="black")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    score_label.config(text="Score 🧍‍♂️ 0 : 0 🤖")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#f0f0f0")

tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

result_label = tk.Label(root, text="👊 Choose your move!", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack()

user_choice_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
computer_choice_label.pack()

score_label = tk.Label(root, text="Score 🧍‍♂️ 0 : 0 🤖", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

for choice in choices:
    btn = tk.Button(
        button_frame,
        text=f"{emojis[choice]} {choice.capitalize()}",
        font=("Helvetica", 12),
        width=12,
        command=lambda c=choice: play(c)
    )
    btn.pack(side=tk.LEFT, padx=5)

# Reset Button
tk.Button(root, text="🔄 Restart", font=("Helvetica", 12), command=reset_game).pack(pady=10)

# Launch
root.mainloop()
