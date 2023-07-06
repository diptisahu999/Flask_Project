from flask import Flask,render_template,redirect,request

from models import db,StudentModel

app = Flask(__name__)

# @app.route("/hello/")
# def hello():
#     return "Hello World!!"

# app.run(host="localhost", port=5000)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()
    
    
@app.route("/add_employee")
def add_employee():
    return render_template('insert.html')


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        students = StudentModel.query.all()
        return render_template('create.html',students=students)
    elif request.method == 'POST':
        # Retrieve the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        mobile = request.form['mobile']
        country = request.form['country']
        gender = request.form['hobbies']
        gender = request.form['gender']
        
        
        
        # Create a new student object
        new_student = StudentModel(first_name,last_name, email, password, mobile, country,gender,gender)
        
        # Add the new student to the database
        db.session.add(new_student)
        db.session.commit()
        
        students = StudentModel.query.all()
        
        return render_template('create.html', students=students)
    return render_template('insert.html')


@app.route("/edit/<int:student_id>", methods=['GET', 'POST'])
def edit_student(student_id):
    # Find the student to be edited
    student = StudentModel.query.get(student_id)
    
    if student:
        if request.method == 'POST':
            # Retrieve the form data
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            mobile = request.form['mobile']
            country = request.form['country']
            gender = request.form['gender']
            
            # Update the student object
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.password = password
            student.mobile = mobile
            student.country = country
            student.gender = gender
            
            # Commit the changes
            db.session.commit()
            
            students = StudentModel.query.all()
        
            return render_template('create.html', students=students)
        
        students = StudentModel.query.all()
        return render_template('edit.html', students=students, student=student)
    else:
        return redirect('/create')
    

@app.route("/delete/<int:student_id>", methods=['POST'])
def delete(student_id):
    student = StudentModel.query.get(student_id)
    
    if student:
        # Delete the student from the database
        db.session.delete(student)
        db.session.commit()
        
        students = StudentModel.query.all()
    
    return render_template('create.html', students=students)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
