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

![alt text](/static/urls.py2.png)

Open the `urls.py` file, and make sure it looks like below

![alt text](https://i.stack.imgur.com/nU0Sj.png)

- #### Creating Views
  Now, we have to create our view. In our case we would have two views `HomeView` and the `SearchView`

  ![alt text](/static/1.png)
  
  


  - #### Creating the HTML Templates
  It is time to take a little break from Django and build our HTML pages. We will use HTML for rendering the content and Bootstrap for styling the content.

  In the `mydictionary` folder, create a folder called `templates` and inside this `templates` folder create another folder called `mydictionary`, this enables Djngo to locate the HTML files.
  For this project, we need three html files, `base.html`, `home.html` and `search.hmtl`, the two files `home.html` and `search.html` will inherit from the `base.html`. This operation is called template inheritance and is very vital in Django programming as it ensures we adhere to the **DRY(Don't Repeat Yourself)** principle.

  Now let's create our HTML files:

  ![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/HTML_files.png)

  Copy and paste the following code into you base.html

        <!DOCTYPE html>
        <html lang="en">
      
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dictionary</title>
            <!-- CSS only -->
            <!-- we are getting bootstrap5 from the CDN -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
      
        <body>
          <div class="container mt-4">
            <div class="row">

            <div class="mt-4 p-5 bg-success text-white rounded mb-3">
                <h1>ThePythonCode.com Dictionary</h1>
            </div>

            <div class="col-md-12">
                {% block content %}
                <!-- here we will inject the content of every page that 
                    inherits from the base page -->
                {% endblock %}
            </div>
          </div>
          </div>
        </body>
        </html>


The next phase is to create the `index.html` file which will inherit from the `base.html` file, To do that:

    <!-- the index page is inheriting from the base page -->
    <!-- the extends tags are used for inheriting from the base page -->
    {% extends 'dictionary/base.html' %}

    <!-- the block content tags for containing content of the page -->
    {%  block content %}

    <form action="search">
        <div class="input-group">
            <input type="text" required class="form-control" name="search" placeholder="Search your favorite word.......">
            <div class="input-group-append">
                <button class="btn btn-success" type="submit">
                    Search
                </button>
            </div>
        </div>

    </form>

    {% endblock %}

I know we are eager to have a feel of how our website is coming along. Let us test it by running the server: 
> `python manage.py runserver`

Once the server is started, go to the browser and refresh the http://127.0.0.1:8000/ page, you should be able to get the below page:

![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/image9.png)

- #### Implementing the Search Functionality
We are now at the climax of this tutorial. In order to get the meaning of words input in by our users, we would be using a programming concept known as web scraping. Web scraping simply entails obtaining large amount of data from websites. In our case, once the user inputs a word in the search form on the home page, the backend code automatically transfers the word to another website, gets the meaning of the word and returns the word back to the user on our own website.
  To do this, let's update the code in our SearchView like this.

    def SearchView(request):
      word = request.GET['word']

      response = requests.get('https://www.dictionary.com/browse/'+word)
      response2 = requests.get('https://www.thesaurus.com/browse/'+word)

      if response:
          soup_1 = bs4.BeautifulSoup(response.text, 'lxml')

          meaning = soup_1.find_all('div', {'value': '1'})
          meaning_1 = meaning[0].getText()
      else:
          word = f"Sorry we couldn't find your word {word} in our records."
          meaning = ''
          meaning_1 = ''

      if response2:
          soup_2 = bs4.BeautifulSoup(response2.text, 'lxml')

          synonyms = soup_2.find_all('a', {'class': 'css-r5sw71-ItemAnchor etbu2a31'})
          synonym_list = []
          for b in synonyms[0:]:
              re = b.text.strip()
              synonym_list.append(re)
          main_synonym_list = synonym_list

          antonyms = soup_2.find_all('a', {'class': 'css-lqr09m-ItemAnchor etbu2a31'})
          antonyms_list = []
          for c in antonyms[0:]:
              r = c.text.strip()
              antonyms_list.append(r)
          main_antonym_list = antonyms_list
      else:
          main_synonym_list = ''
          main_antonym_list = ''


      results = {
          'word' : word,
          'meaning' : meaning_1,
      }

    return render(request, 'mydictionary/serach.html', {'main_synonym_list': main_synonym_list, 'main_antonym_list': main_antonym_list, 'results': results})


- #### Testing the Functionality
Now that we have successfully implemented the search word functionality in the searchView() function, let us take our website on a spin. Copy the http://127.0.0.1:8000 in the browser, to get the output below:

![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/image8.png)

Always ensure that the server is running, if not then re-run this command:

> `python manage.py runserver`

Now that the application is running, we will search for the word "coding", enter the word in the input field and click the search button. After the search is completed, you will be redirected to the search page where all the results are displayed, as below:

![alt text](https://www.thepythoncode.com/media/articles/build-dictionary-app-with-django-and-pydictionary-api-python/image10.png)

- #### Conclusion
That’s it for this tutorial, we have successfully built a Django dictionary web application.  we now hope you know how to play around with the Django framework and the web-scraping operation.










