from flask import Flask, render_template, request, redirect
from markupsafe import escape
import csv
# app = Flask(__name__)

app = Flask(
    __name__,
    template_folder="templates"  # this is also default template folder name
)


@app.route('/favicon.ico')
def favicon():
    return './static/assets/favicon.ico'


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<page>")
def my_custom_page(page):
    return render_template(page)


""" @app.route("/project.html")
def my_project():
    return render_template('project.html')


@app.route("/components.html")
def my_components():
    return render_template('components.html')

@app.route("/blog")
@app.route("/blog.html")
def blog():
    return render_template('blog.html')


 """


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Data is not saved'
    else:
        return 'something went wrong'


@app.route('/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
