from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)


@app.route('/')
def home():
    return "Hello, Flask!"

#--------------------------

#MODELS
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    description=db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"
#EMPLOYEE ROUTE
@app.route('/employees')
def employee():
    employees=Employee.query.all()
    output=[]
    
    for employee in employees:
        employee_data={'name':employee.name, 'description': employee.description}
        output.append(employee_data) 

    return{"employee":output}

#PRIMARY KEY ROUTE
@app.route('/employees/<id>')
def get_employees(id):
    employee=Employee.query.get_or_404(id)
    return ({"name":employee.name, "description": employee.description})

#POST EMPLOYEE
@app.route('/employees',methods=["POST"])
def add_employees():
    employee=Employee(name=request.json['name'], description=request.json['description'])
    db.session.add(employee)
    db.session.commit()
    return {'id': employee.id}   

#DELETE ROUTE
@app.route('/employees/<id>', methods=['DELETE'])
def delete_employee(id):
    employee=Employee.query.get(id)
    
    if employee is None:
        return {"employee not found"},404
    db.session.delete(employee)
    db.session.commit()
    return{"message": "yeet"},200




#----------------------------------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    