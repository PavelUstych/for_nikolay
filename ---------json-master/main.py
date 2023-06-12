import modules.create_json as m_json
import turtle

dict1 = {
    'name' : 'Павел',
    'surname' : 'Устич',
    'age' : 12
}
m_json.create_json(dict1) 
dict2 = m_json.read_json(dict1)

t1 = turtle.Turtle()

t1.write(dict2['name'], move=False, align="left")
t1.penup()
t1.forward(70)
t1.write(dict2['surname'], move=False, align="left")
t1.penup()
t1.forward(70)
t1.write(dict2['age'], move=False, align="left")
t1.penup()
t1.forward(70)

turtle.done()