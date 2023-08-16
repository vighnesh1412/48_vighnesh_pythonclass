from guizero import App, Text, TextBox, PushButton
import random

class GuessingGame:
    def __init__(self, app):
        self.app = app
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.message = Text(app, text="Guess a number between 1 and 100:")
        self.guess_input = TextBox(app, width=10)
        self.result_message = Text(app, text="")
        
        self.submit_button = PushButton(app, text="Submit Guess", command=self.check_guess)
        self.play_again_button = PushButton(app, text="Play Again", command=self.play_again)
        self.play_again_button.disable()
    
    def check_guess(self):
        guess = int(self.guess_input.value)
        self.attempts += 1
        
        if guess < self.secret_number:
            self.result_message.value = "Too low! Try again."
        elif guess > self.secret_number:
            self.result_message.value = "Too high! Try again."
        else:
            self.result_message.value = f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts."
            self.submit_button.disable()
            self.play_again_button.enable()
    
    def play_again(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.message.value = "Guess a number between 1 and 100:"
        self.result_message.value = ""
        self.submit_button.enable()
        self.play_again_button.disable()
        self.guess_input.value = ""

app = App("Guessing Game", width=300, height=200)
game = GuessingGame(app)
app.display()
