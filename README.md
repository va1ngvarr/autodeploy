# autodeploy
Simple code for automatic deploy of your application on your linux-server.
It pulls latest updates from your github repo and restarts your application.

## Pre-dependencies
```
python3
python3-pip
git
```
## Usage
```
git clone https://github.com/va1ngvarr/autodeploy
```
Edit config at `autodeploy/git_config.json`. Put there your github access token, reponame, username and entrypoint command.
```
cd autodeploy && pip install -r requirements.txt
python3 install.py
curl -X POST http://hostname:port/repo-is-updated
```
Your application should has been running.
### Good practices
You may use github webhooks to deploy application when repo updated.

Create webhook at *Your-Repo -> Settings -> Webhooks -> add webhook*
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/a38838f3-c0cf-4dd1-a889-33462cb941d3)


Then fill Payload URL like this and keep trigger as is:
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/e37f4a6f-51c3-4847-a252-e65cb0c3211c) 
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/7b305274-00fc-469d-8251-9eef421351f5)
