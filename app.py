from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Tutorial AI",
        "description": "Tutorial AI made using Mistral LLM model",
        "url": "https://github.com/thebigbone/tutai",
    },
    {
        "title": "Sentiment Analysis",
        "description": "sentiment of the text (positive, negative or neutral) with nlp api",
        "url": "https://github.com/thebigbone/sentiment-analysis",
    },
    {
        "title": "MoveAPI",
        "description": "MovieAPI written in Go",
        "url": "https://github.com/thebigbone/MovieAPI",
    }
]


@app.route('/')
def display_projects():
    return render_template('projects.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
