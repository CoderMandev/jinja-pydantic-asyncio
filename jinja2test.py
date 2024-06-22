import jinja2
from pydantictest import my_books

env = jinja2.Environment()
template = env.from_string("""
My favorite books are:
{% for title in my_books -%}
                           
- {{ title }}
{% endfor %}
""")

print(template.render(my_books=my_books))