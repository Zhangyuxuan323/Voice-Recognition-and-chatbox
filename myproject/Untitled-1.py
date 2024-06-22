from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Input System</title>
    </head>
    <body>
        <header>
            <h1>Welcome to My Flask Webpage</h1>
        </header>
        <main>
           <form action="/submit" method="post">
                <label for="inputText">Enter some text:</label>
                <input type="text" id="inputText" name="inputText">
                <button type="submit">Submit</button>
            </form>

            



            <title>Container Box Example</title>
            <style>
                .container {
                    border: 1px solid #ddd;
                    padding: 20px;
                    margin: 20px;
                    background-color: #f9f9f9;
                    border-radius: 5px;
                }
            </style>






        </main>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(debug=True)