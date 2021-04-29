# Kiwi Lingo: Your Guide to New Zealand Words & Phrases!

For my third milestone project (data centric) with The Code Institute, I decided to build a glossary database called Kiwi Lingo. It is an app intended to be accessible across all devices and used as a reference guide of commonly used words and phrases spoken by New Zealanders. 

![image](https://res.cloudinary.com/elerel/image/upload/v1619524355/amiresponsive_b9hz00.png)

## Contents

- [**User Experience**](#user-experience)
  - Strategy
    - Project Description
      - User Stories
      - First Time User Stories
      - Registered User Stories
      - Site Owner User Stories
  - Structure    
  - Scope: Design
  - Skeleton
    - Wireframes
  - Surface
    - Colour Scheme
    - Typography
    - Imagery

  
- [**Database Schema**](#database-schema)

- [**Features**](#features)
  - Existing Features
  - Features left to be implemented

- [**Technologies Used**](#technologies-used)
  - Languages Used
  - Frameworks, Libraries and Programs Used
  - Dependencies

- [**Testing**](#testing)

- [**Deployment**](#deployment)
  - GitHub
  - Heroku
  - Cloning the Repository

- [**Credits**](#credits)
  - Code
  - Content
  - Media
  - Acknowledgements

---

## User Experience

### Project Description

The aim behind Kiwi Lingo is to form an online dictionary/phrase reference guide to various words and phrases spoken in New Zealand. 

Each word or phrase in the dictionary will have a definition, a phonetic spelling to aid the pronunciation and an example of how the word or phrase is commonly spoken by locals.

Kiwi Lingo would be typically used for:

- First time visitors to New Zealand
- Visitors currently in New Zealand struggling to understand the locals
- Visitors or locals looking to brush up on their slang or use as a reference guide to teach others
- New Zealanders that would like to add their own words or phrases to help visitors to NZ
- People that have visited NZ that would like to keep a log of phrases/words/slang encountered on their visit and retain for future visits to NZ

Visitors to the site will be able to sign up for an account so they can easily add (CREATE) any words or phrases to the dictionary that might be missing. Upon registering, users will be able to edit (UPDATE) their additions and also be able to remove (DELETE) what they have added themselves. They can also view/search (READ) for words or phrases in the search tool bar.

A favourable outcome behind creating this site would be:
- With additions by new and existing users, it would allow growth to the site
- An opportunity for the site owner to encourage the user to book excursions/holidays highlighted in the links throughout the site


### User Stories

#### First Time User Stories
##### As a first time user:
-  I want to be able to fully understand the reasoning behind the site.
-  I want to be able to navigate easily throughout the site.
-  I want to be able to search for words and phrases commonly spoken in New Zealand.
-  I want to be able to set up my own account and add my own words or phrases to the site.
-  I want to be able to view popular sayings and phrases by viewing the most popular/least popular additions.


#### Registered User Stories
##### As a regular user:

- I want to be able to easily log in and out of the site.
- I want to be able to edit or delete my additions to the site.
- I want to be able to view additions by other users.
- I want to be able to edit or delete my profile.
- I want to be able to contact the site owners.


#### Site Owner User Stories

- To provide information on the site and who it is intended for.
- To allow the site to be accessible (viewing only) without creating an account.
- To be easily contacted should the user lose their log-in details.
- To allow users to only edit or delete their own additions.
- To be able to delete any inappopriate content added by a registered user.


---


### Overview

New Zealand English and their own slang can be quite hard to grasp if you're a first time visitor to New Zealand or in conversation with a Kiwi in a loud pub. Sometimes it can seem like Kiwi English is an entirely separate language! Which is why I decided to have a go in creating an online guide to some of the most common New Zealand phrases and lingo. Kiwi slang can be found just about anywhere, even in the likes of fancy restaurants and hotels. It includes some Maori phrases and Maori slang used in everyday life.

This app is designed as a complete guide on New Zealand slang and how to use it like a real Kiwi!  The phrases or words may look complicated but trust me once you get the hang of it, it’s easy as bro.





 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [MaterializeCSS](https://materializecss.com/)
    - I found using MaterializeCSS throughout the Mini Project easy to use and so adapted this into this project for the CRUD mechanisms and database access functionality

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

### Initial Steps

Kiwi Lingo was created using Gitpod and Git and Github to host the repository. Once an account is opened with Github as prerequisite for this project, and logged in under your unique username, I selected "New" and then selected the [CI Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template). From there, I chose the name **ms3-kiwi-lingo** as the repository name, selected it to be stored as a "public" repository and then selected "Create Repository".

From there, I navigated to my new repository on GitHub and clicked the green Gitpod button which built the Kiwi Lingo workspace. To access the workspace daily, I simply navigated to [Gitpod](https://gitpod.io/workspaces) where I could select its own unique workspace name and if not present, select "filter: all" :
![image](https://res.cloudinary.com/elerel/image/upload/v1619687098/gitpodworkspace_jzhgss.png) 

 For version control, I used the following commands mainly throughout the project:

git add filename/ git add -A/ git add . - Theses command were used to add files to the staging area before committing.

git commit -m "subject: commit message explaining the updates" - With reference to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), providing an easy set of rules for creating an explicit commit history,  this command was used to to commit changes to the local repository.

git push - This command is used to push all committed changes to the GitHub repository.

---
### Requirements

 In order to deploy, the following were installed:
- [PIP](https://pypi.org/project/pip/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

1. To install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type:
 ```bash
 pip3 install -r requirements.txt.
 ```
2. Create the project database with MongoDB:
    1. Signup Or Login For [MongoDB](https://www.mongodb.com/)
    2. Create a cluster as well as a database
    3. Create the following collections in the Database:
        1. categories
        2. users
        3. words

3. Create environment variables (env.py):
    1. Create a .gitignore file in the root directory of the project (which the CI Template already provides, otherwise type "touch .gitignore" )
    2. Create a file in the root directory called "env.py". This will contain all of your envornment variables. Your env.py file should look similar to the following:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")
```

 Note: It is important that the user updates the secret keys and passwords. These details are private and are not disclosed in this repository for security purposes. Before pushing the project to a public repository, add your env.py file to .gitignore.

  3. You can now run your application locally by typing the following command into your terminal:

```
python3 app.py
```

### Deploying To Heroku

To deploy our application on Heroku, first we need to create a requirements.txt file as well as a **Procfile**. These files will allow Heroku understand 
what dependencies are required to run the application, as well as tell Heroku which file to run, to launch the application.

#### Create a procfile:

Enter the following in the CLI:

```
python app.py > Procfile
```

**This new file if opened should look something like "web: python app.py"**

#### Create a requirements file:

```
pip freeze --local > requirements.txt
```

**Once created, this new file should simply be a list of all dependencies required**



 With the code required to run the app all stored in a repository with Github, deploying the app with Heroku can be done following these steps:

1. Sign in/sign up to Heroku.

2. Once signed in, click on the 'Create New App' button. 

3. Choose a name for your app, select your local region and click 'Create App'.

4. In the top menu, select the 'Deploy' tab, and then click 'Connect to GitHub' in the 'Deployment method' section.

5. Connect your GitHub account to your Heroku account by clicking on the 'Connect to GitHub' button (if already connected, move to step 6).

6. Search for the GitHub repository which contains the app you wish to deploy, and then click 'connect'.

7. Once connected, you can choose to automatically deploy any updates made in the GitHub repository or to do so manually by selecting the branch you wish to deploy and clicking on the appropriate button.

8. Following this, click on the 'Settings' tab and then click 'Reveal Config Vars'

9. Within the 'Reveal Config Vars' section, add the variables which would be found in your local 'env.py' file. These variables are saved here as they contain sensitive data such as the password to the MongoDB database and the secret key required to use some of Flask's functionality.

10. With all of the previous steps complete, as well as the prerequisites, the app will now run by clicking the 'Open app' button.


---





This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

### Forking This Project:
  If you wish to contribute to this website you can Fork it without affecting the main branch by following the procedure outlined below.
  1. Go to GitHub's website and log in.
  2. Locate the Kiwi Lingo's [Repository](https://github.com/elerel/ms3-kiwi-lingo) in the search field.
  3. On the right-hand side of the Repository name, you'll see the 'Fork' button. It's located on the top right hand corner of the page, next to the 'Star' and 'Watch' buttons.
  4. This will create a copy in your personal repository.
  5. Once you're finished making changes you can locate the 'New Pull Request' button just above the file listing in the original repository.

### Cloning This Project:
To create a clone, follow the following steps.

1. Log in to GitHub and go to the repository.
2. Click on the button with the text “Code”.
3. Click “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application or follow the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to see how to clone the repository in other ways.

---

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

- [Regional Slang Article](https://www.stuff.co.nz/national/99763866/hey-uce-heres-a-meanas-guide-to-kiwi-regional-slang)
- [W3 Resource](https://www.w3resource.com/mongodb/mongodb-field-update-operator-$inc.php) for help with likes and dislikes function
- [Stackoverflow](https://stackoverflow.com/questions/18574699/how-to-make-a-space-between-i-tags-icons-in-table/18574766) on rotating icons
- [Flask Mega Tutorial, Pt VII](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)- in reference to use of error functions


### Media
- The photos used in this site were obtained from ...

- [PXFuel](https://www.pxfuel.com/en/free-photo-ofpyp)
- [SeekLogo](https://seeklogo.com/vector-logo/195319/new-zealand-rugby-union-fern)- for use of Fern logo


### Acknowledgements

- I received inspiration for this project from X
