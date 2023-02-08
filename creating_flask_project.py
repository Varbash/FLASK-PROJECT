# pipenv flask
# pipenv shell

#rest api

from flask import Flask,render_template,abort,jsonify,url_for,redirect,request
from model import db,save_db

app = Flask(__name__)

#decorator it converts function below to veiw

@app.route('/')
def welcome():
    return render_template('home.html',questions=db)


@app.route('/questions/<int:index>')
def questions_view(index):

    try:

        questions_db = db[index]

        return render_template('quiz.html',questions=questions_db,index=index,max_index=len(db)-1)

    except IndexError:
        abort(404)



@app.route('/add_new_question',methods=['GET','POST'])
def add_question():
    if request.method == 'POST':

        question_dict={
            "question":request.form['question'],
            "answer":request.form['answer']
        }

        db.append(question_dict)
        save_db()

        return redirect(url_for('questions_view',index=len(db)-1))

    else:
        return render_template('add_question.html')     
          


    







#import jsonify
#create a rest api for project
@app.route('/api/questions/')
def api_question_list():
    return jsonify(db)


@app.route('/api/questions/<int:index>')
def api_question_detail(index):
    try:
        return db[index]

    except IndexError:
        abort(404)  


         





if __name__=='__main__':
    app.run(debug=True)
