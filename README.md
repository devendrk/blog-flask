This is my first  Flask web app.  
This is a basic blog where user can register, set their  profile picture, write their blog, udpdate the blog, update the user name, password and so on.

## setting up the virtual environment.
we use pipenv the latest way os setting up the virtual environment.For more info about pipenv read [here](https://realpython.com/pipenv-guide/#pipenv-introduction
)
1. create a project folder and cd to that folder
2. install pipenv
3. install flask pipenv install flask
4. create run.py file 
5. create app folder and templates folder

- below command is to install pipenv, install flask and start the virtual env
- ```pipenv shell``` starts the virtual env. you can do it incase you turn off( exit ) your virtual env.
```Python
 pip install pipenv
# cd to the project folder
 pipenv flask
 pipenv shell # starts the virtual env
 

 pipenv install --dev # installs all the depencies that are in pipfile. use this command if you are cloning this repo in your desktop.

```
- for hello world python follow this [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 

- create init.py insidethe app folder
-in run.py write following code
```Python
from flask import Flask, render_template

app = Flask(__name__)
posts = [
  {
    'author':'Don',
    'title': "Test post 1",
    'content': "Test content 1"
  }
]
app.route('/')
def home():
    return render_template('home.html', posts = posts)




if __name__ == "__main__":
    app.run(debug = True)
```

- crete templates folder inside app and  create home.html file.
- similarly create register.html, login.html and layout.html inside template
- layout.html contains the frame fo the ui and all other pages inherits the layout. we use jinja2 to execute the functionality of the app.
- in home.html the code is written insde the jinja2 block as in the code above.

- learn more about jinja2 [here](https://www.fullstackpython.com/jinja2.html)

- execute the run.py with ``` python run.py ``` command in terminal. type  ``` localhos:5000``` to se the changes
- ``` pipenv install flask-wtf ``` WTForms, and Flask WTF is used to handle the registration form validation.

