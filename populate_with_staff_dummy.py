import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'intreatment_project.settings'
                      )

import django
django.setup()

from appointments_app.models import Staff




def populateStaff():
    """ Populates database with set of fictional names and
    medical specialties.
    """
    
    
    data = {'Терапевт': ['Мамонтов Пантелеймон Филатович',
                         'Панов Протасий Валентинович',
                         'Лазарева София Макаровна'
                         ],
             'Педиатр': ['Якушев Авксентий Геласьевич',
                        'Михайлов Валерьян Кимович',
                        'Баранова Виктория Созоновна'
                         ],
             'Генетик': ['Рогов Виктор Федосеевич',
                        'Самсонов Даниил Аристархович',
                        'Русакова Жанна Иринеевна'
                         ]
            }
    for speciality in data:
        for name in data[speciality]:
            obj = Staff.objects.get_or_create(name=name, speciality=speciality)[0]
            obj.name = name
            obj.speciality = speciality
            obj.save()
            



if __name__ == '__main__':
    print('Starting population script ... ', end='')
    populateStaff()
    print('DONE!')
