from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"
    
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        desc = request.form.get('desc', '').strip()
        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        return redirect("/")
        
    allTodo = Todo.query.all() 
    return render_template('index.html', allTodo=allTodo)

@app.route("/products")
def products():
    allTodo = Todo.query.all() 
    return "<p>This is products page</p>"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first() 
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect("/")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first() 
    if not todo:
        return redirect("/")
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        desc = request.form.get('desc', '').strip()
        if title and desc:
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
        return redirect("/")
    return render_template('update.html', todo=todo)

@app.route("/show")
def show_todos():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8000)

