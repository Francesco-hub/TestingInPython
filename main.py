from Website import create_app

app = create_app('Release')
if __name__ == '__main__':
    app.run(debug=True)
