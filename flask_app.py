from flask import Flask, render_template
from launch import get_all_launch_objects, get_5_launches_after_now
app = Flask(__name__)
app.config["DEBUG"] = True

'''
Renders the index template.
'''
@app.route('/')
def index():
    launches_after_now = get_5_launches_after_now()
    return render_template('index.html',
                           launches = launches_after_now)

@app.route('/all_launches')
def all_launches():
    launches = get_all_launch_objects()
    return render_template('all_launches.html',
                           launches = launches)

if __name__ == '__main__':
    app.run(debug=True)