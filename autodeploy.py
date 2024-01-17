import os
import json

from multiprocessing import Process

from aiohttp import web


def load_json_config(path_to_file="git_config.json"):
    with open(path_to_file, "r") as json_file:
        params = json.load(json_file)

    return params


app = web.Application()
router = web.RouteTableDef()

config = load_json_config()

os.putenv("GITHUB_USER", config["GITHUB_USER"])
os.putenv("GITHUB_TOKEN", config["GITHUB_TOKEN"])
os.putenv("GITHUB_REPOSITORY", config["GITHUB_REPOSITORY"])

GITHUB_REPOSITORY_PATH = config["GITHUB_REPOSITORY"].split("/", 1)[1]
os.putenv("GITHUB_REPOSITORY_PATH", GITHUB_REPOSITORY_PATH)

app_proc = None


@router.post("/repo-is-updated")
async def webhook_endpoint(request):
    global app_proc

    if app_proc != None:
        # Kill the process
        app_proc.terminate()
        # Wait for the process to finish
        app_proc.join()

    os.system("cd .. && bash ./git-clone-repo-with-token.sh")

    command = config["ENTRYPOINT"]
    start_app = lambda: os.system(command)
    # Create and start the app process
    app_proc = Process(target=start_app)
    app_proc.start()

    return web.Response()


def main():
    app.add_routes(router)
    web.run_app(app)


if __name__ == "__main__":
    main()
