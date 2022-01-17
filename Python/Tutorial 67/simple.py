from jinja2 import Template

name = "Jonathan"
number = 11

tm = Template("My name is {{ name }} and I like the number {{ number }}")
msg = tm.render(name=name, number=number)

print(msg)
