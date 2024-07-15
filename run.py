# the entry point to run our flask web app. it starts the flask server so we can view our app in the browser.


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

