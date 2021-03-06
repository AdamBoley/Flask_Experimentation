To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


Install Flask:<br>
`pip3 install Flask`
<br>

Install StartBootstrap Clean Blog theme:<br>
`wget https://github.com/StartBootstrap/startbootstrap-clean-blog/archive/refs/tags/v5.0.10.zip` <br>
Adds a zip file called v5.0.10.zip
<br>

Unzip Clean Blog zip file:<br>
`unzip v5.0.10.zip`
<br>

To run a developer server:<br>
`python3 run.py` 
<br>(python3 -m http.server does not work because there is no index.html in the root directory)

<br>

To install Heroku CLI:<br> 
`npm install -g heroku`

<br>

To login to Heroku:<br>
`heroku login -i`

<br>

To view Heroku apps:<br> 
`heroku apps`

<br>

Connect workspace to Heroku:<br>
`git remote add heroku https://git.heroku.com/mass-effect-flask-app.git`

<br>

Check that workspace is connected to heroku:<br>
`git remote -v` - should display 2 heroku remotes and 2 origin remotes


Create requirements.txt file to tell Heroku what language and dependencies are being used: <br>
`pip3 freeze --local > requirements.txt`

<br>

Push to Heroku:<br>
`git push -u heroku main`

The app won't work just yet...

Create Procfile:<br>
`echo web: python run.py > Procfile` (the capital P is important)

Create Config Vars:
IP: 0.0.0.0 (in run.py as well)
PORT: 5000 (in run.py as well)
Add SECRET_KEY from env.py

<br>

If Heroku ever needs to be disconnected:<br>
`git remote rm heroku`

<br>

Check Heroku logs if deployment fails:<br>
`heroku logs --tail --app <app-name>`
