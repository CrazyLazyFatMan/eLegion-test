# e-Legion test task

## Run project

Open terminal in eLegion-test folder

#### Requirements

* To install all necessary requirements type in opened terminal `pip3 install requirements.txt`

#### Database
* Create postgres DB:
    `
    'NAME': 'elegion',
    'USER': 'postgres',
    'PASSWORD': 'postgres,
    'HOST': '5432'
    `

* Run command `cd elegion_test`

#### Migrations

* Apply migrations by running command `python3 manage.py migrate`

#### Run server

* Run server with command `python3 manage.py runserver`


## Endpoints

* Url `/api/` gives you access to Api Root and list of all available endpoints such as:
    * `/authors/` - list of all created authors
    * `/books/` - list of all created books 
    * `/liblary/` - paginated view for all books and their authors. There is also available search filter which accepts `book title` and `author name/surname` for filtering results 

* You can navigate through api by using url string or by using Django REST interface. 
    * If you want to use search filter by url link please type `localhost/api/library/?search=<book_title/author_name/author_surname/author_name+author_surname>/`
    * For navigate between `/library/` pages use interface or type `/localhost/api/library/?page=<next_page_number/previous_page_number>/`
 
## Tests 

* To run tests type command in opened terminal `python3 manage.py test`. There are 10 tests for different methods (POST, GET, PUT, DELETE)