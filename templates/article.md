A dictionary is simply a book/electronic medium that outlines words particular to a language along with their meanings. Modern dictionaries also provide informations such as origin, transcription and use cases.

In this tutorial, we are going to build an English dictionary using the Django framework. To follow along with this tutorial, it is neceessary to have a basic knowledge of HTML5 and Bootstrap as they would be used in the frontend of this project. Before we delve into this tutorial in-depth i would like us to what Django is. Django is a python framework used for building web applications. For ease of use, i have outlined a table of content so the readercan keep track of his/her progress in the table. Below is the table of contents.

## Table of Contents

1. Creating the virtual environment
2. Activate the virtual environment
3. Installing Django
4. Creating the Project & Application
5. Setting up the App in the Project Folder
6. Configuring the App Urls
7. Creating Views
8. Creating the HTML Templates
9. Integrating the Word Search Fuctionality
10. Testing the Functionality
11. Conclusion

- #### Creating the Virtual Environment

  To start off, let us create a virtual environment for this project named `project` The essence of this is to create an isolated environment dedicated to our project.

  > $ python -m venv project

- #### Activate the virtual Environment

  Now activate the virtual environment using the following command:

  > $ .\project\Scripts\Activate

- #### Installing Django

  Next, we will then install the necessary libraries inside the virtual envionment including Django, as shown below

  > $ pip install django

- #### Creating the Project and Application

  Now that we have django installed successfully, let us create a Django project using django's default command `django-admin startproject`, run this command in your terminal :

  > $ django-admin startproject mydictionary

  The command above creates a folder called mydictionary. From this point, we will be working inside this folder. Now `cd` into the `mydictionary` folder. Our next line of action is to create a django app. To do that, run the below command:

  > $ python manage.py startapp dictionary

  After installing Django successfully and creating the new project, it is necessary to check if the installation was successful, to do that, run the below command:

  > $ python manage.py runserver

  Make sure you get this output:

  ![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/python_manage.py_runserver.png)

  Copy http://127.0.0.1:8000/ into your browser, if you get the below output then you installed Django successfully:

  ![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/Django_installed.png)



- #### Setting up the App in the Project Folder
  Next, we’ll need to let Django know about the dictionary app we just created. We do this by registering the app.

  To register the app, open mydictionary/settings.py file and add `dictionary.apps.DictionaryConfig` to the INSTALLED_APPS list. After adding this, INSTALLED_APPS should look like this:

  ![alt text](/static/Screenshot%202022-07-06%20224741.png)


- #### Configuring the URLs of the App
Let us now configure our URLs, in Django, we have two `urls.py` files, the first one comes with Django and is used for registering all the apps' URLs and it is found in the project root folder, while the second `urls.py` file is created inside the app’s folder by the programmer, in our case it will be created inside the dictionary folder.

First things first, let us register our app’s URLs, and open the `urls.py` file in the project root folder:
