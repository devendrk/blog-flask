

## Set up virtual environment
we use pipenv  to setup the virtual environment.For more info about pipenv read [here](https://realpython.com/pipenv-guide/#pipenv-introduction
)
 ## Steps to start with
- Fork the this repo ( frok button on the top right corner)
- Now you should see it on the list of your repos. 
- cd to your desired folder or (desktop) you want to clone.
- In your terminal type:   ``` git clone <githublink> ```
- cd to the cloned directory
- Install pipenv ( if you do not have pipenv): ``` pip install pipenv ```
-  ```pipenv shell``` command  starts the virtual env. you can do it incase you turn off( exit ) your virtual env.
- Type: ``` pipenv install --dev ```  to  install all the depencies that are in pipfile. (use this command if you are cloning this repo ) .
 
- Execute the run.py with: ``` python run.py ``` command in terminal. Type  ``` localhos:5000```  on your browser

## Create branch before you add your code for the first time
- Create new branch :  ``` git checkout -b <your branch name> ```
- Now you  should be on your branch :  ```<branchname> ```
- Start to add your code

## Commit push and pull request
1. ```git status ``` check status ( red text indicates its not stagged yet.) 
2.  ```git add . ```  your code goes to staging area.
3. ```git status ``` check status ( text should be green )
4. ``` " git commit -m "< your commit message here>" ``` saves the changes.
5.  ``` git push -u origin <branch> ```
-  Repeat this step 1- 4  each time you want to commit. step 5 to upload your working code in git hub.
-  Goto your git hub  and send the pull request.

# reference links 

- Learn more about jinja2 [here](https://www.fullstackpython.com/jinja2.html)
- For hello world python follow this [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
