# autodeploy
Simple code for automatic deploy of your application on server. It pulls latest updates from your github repo and your restarts application.
## Usage
```
git clone https://github.com/va1ngvarr/autodeploy
```
Edit config at `autodeploy/git_config.json`. Put there your github access token, reponame, username and entrypoint command.
```
cd autodeploy && python3 install.py
curl -X POST http://hostname:port/repo-is-updated
```
Your application should has been running.
### Good practices
Use github webhooks to deploy application when repo updated.
Create webhook at _*Your-Repo -> Settings -> Webhooks -> add webhook*_
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/a38838f3-c0cf-4dd1-a889-33462cb941d3)
Then fill Payload URL like this and keep trigger as is:
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/7b71adb6-2a53-4059-b0d4-45e0b82d91a6)
![image](https://github.com/va1ngvarr/autodeploy/assets/93223722/7b305274-00fc-469d-8251-9eef421351f5)
