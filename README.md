Intreatment project - is one page app for making a doctor appointments, also allowes to get information about all appointments through admin panel.

App url:

    http://{{ hostname }}/

Admin panel url and login: 

    http://{{ hostname }}/admin
    login: admin
    password: pass1234

Project requirments:

      python==3.*
      Django==1.10.7
      selenium==3.4.1
      
      Firefox browser
      https://www.mozilla.org
      
      Geckodriver
      https://github.com/mozilla/geckodriver/releases
      
Untit tests:

    python manage.py test
    
functional_tests.py:

    runs project functional testing.

    Two varibles must be redefined with relevant values:
    
        GECKODRIVER_PATH = r'geckodriver/geckodriver.exe'
        HOST_NAME = 'http://127.0.0.1:8000'
      

populate_with_staff_dummy.py :

    populates database with fictional Staff data, must be run with
    python virtual environment activated.
