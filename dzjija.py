from jinja2 import Template

#MACRO
teg = [
    {'type': 'text', 'name': 'firstname', 'placeholder': 'Имя'},
    {'type': 'text', 'name': 'lastname', 'placeholder': 'Фамилия'},
    {'type': 'text', 'name': 'address', 'placeholder': 'Адрес'},
    {'type': 'tel', 'name': 'phone', 'placeholder': 'Телефон'},
    {'type': 'email', 'name': 'email', 'placeholder': 'Почта'}
]

html = '''
{% macro list_teg(list_user) %}
{%for t in list_user-%}
    <p><input type="{{ t['type'] }}" name="{{ t['name'] }}" placeholder="{{ t['placeholder'] }}"></p>
{% endfor %}
{% endmacro %}
{{ list_teg(user) }}
'''

tm = Template(html)
msg = tm.render(user=teg)
print(msg)

# NO MACRO
# teg = [
#     {'type': 'text', 'name': 'firstname', 'placeholder': 'Имя'},
#     {'type': 'text', 'name': 'lastname', 'placeholder': 'Фамилия'},
#     {'type': 'text', 'name': 'address', 'placeholder': 'Адрес'},
#     {'type': 'tel', 'name': 'phone', 'placeholder': 'Телефон'},
#     {'type': 'email', 'name': 'email', 'placeholder': 'Почта'}
# ]
#
# link = '''
# {% macro list_teg(list_user) %}
#
# {%for t in teg-%}
#     <p><input type="{{ t['type'] }}" name="{{ t['name'] }}" placeholder="{{ t['placeholder'] }}'"></p>
# {% endfor %}
#
# {% endmacro %}
#
# {{ list_teg(user) }}
# '''
#
# tm = Template(link)
# msg = tm.render(user=teg)
# print(msg)