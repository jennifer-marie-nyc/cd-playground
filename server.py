from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template('index.html', level=1)

@app.route('/play/<int:num_boxes>')
def playNum(num_boxes):
    return render_template('index.html', level=2, num_boxes=num_boxes)

@app.route('/play/<int:num_boxes>/<color>')
def playNumColor(num_boxes=3, color='lightskyblue'):
    return render_template('index.html', level=3, num_boxes=num_boxes, color=color)

if __name__=='__main__':
    app.run(debug=True)