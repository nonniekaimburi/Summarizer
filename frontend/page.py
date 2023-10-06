from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def get_summary():
    text = request.form['text']
    summary = summarize(text)
    return render_template('summary.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
