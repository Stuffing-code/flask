from jinja2 import Template


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# per = Person("Федор", 33)
per = {'name': "Федор", "age": 34}

tm = Template("Мне {{ p['age'] }} лут и зовут {{ p['name'] }}")
msg = tm.render(p = per)

print(msg)
