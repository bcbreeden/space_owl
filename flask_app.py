from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

'''
Renders the index template.
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all_launches')
def all_launches():
    return render_template('all_launches.html')

if __name__ == '__main__':
    app.run(debug=True)