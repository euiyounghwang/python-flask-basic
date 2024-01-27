from api import init_api

application = init_api()

def main():
    app = init_api()
    app.run(port=5000, debug=False)


if __name__ == "__main__":
    main()