from api import init_api
from job.job import create_jobs

application = init_api()

# --
# a process that runs in the background
# create_jobs()
# --

def main():
    app = init_api()
    app.run(port=5000, debug=False)


if __name__ == "__main__":
    main()