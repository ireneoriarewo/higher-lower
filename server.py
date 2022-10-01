from flask import Flask
import random

ran_number = random.randint(0,11)
# print(ran_number)
app = Flask(__name__)

def page_style(function):
    def wrapper():
        return '<center>' + function() + '</center>'
    return wrapper


@app.route('/')
@page_style
def homepage():
    return '<h1>Guess a number between 0 and 10</h1>' \
           '<a href="https://im.ge/i/1REznT"><img src="https://i.im.ge/2022/10/02/1REznT.numbers.gif" alt="numbers" border="0"></a>'

@app.route('/<int:number>')
# @page
def guess_game(number):
    if number < ran_number:
        return '<center><h1 style="color: red">Too low, try again!</h1></center>' \
               '<center><img style="width: 40%" src="https://media2.giphy.com/media/eKfpB6WZeKC1DiGrj8/200w.webp?cid=ecf05e47qykdmnif04ct95yzrqq2yio3ft0zqtenz5hdphjp&rid=200w.webp&ct=g"></center>'
    if number > ran_number:
        return '<center><h1 style="color: purple">Too high, try again!</h1></center>' \
               '<center><img src="https://i.pinimg.com/originals/55/6d/1d/556d1d1e173d96835397f775cf96bd72.gif"</center>'
    if number == ran_number:
        return '<center><h1 style="color: purple">You found me</h1>' \
               '<img src="https://media0.giphy.com/media/Ie4CIIvQS0bk3zwZlM/200.webp?cid=ecf05e47te41ll4i4paq602thlb8vrv2n1adtsjsmehurk8g&rid=200.webp&ct=g"></center>'

if __name__ == "__main__":
    app.run(debug=True)
