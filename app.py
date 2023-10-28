from flask import Flask, render_template
from forms import Registrationform, Loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b409f3d6a632f93c0c1c6c99217ff1ff'
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$60,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Remote'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '$65,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$75,000'
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/products.html")
def products():
    return render_template('products.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registrationform()
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form =  Loginform()
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)