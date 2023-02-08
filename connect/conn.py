#virtual environment
#flask install
#create folder templates usme html css files

from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
#in ml file
#pickle.dump(log_reg,open('model.pkl','wb'))  log_reg=name of linear regression
#model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello():
    return render_template('html_file')

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features =[np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)


    return render_template('html_file',prediction_text='next exploe ${}'.format(output))
    


    #this function name will be the name of LinerRegression()




@app.route('/predict_api',methods=["POST"])
def predict_api():
  #For direct API calls trought request
  data =request.get_json (force=True)
  prediction =model.predict([np.array(list(data.values()))])
  output= prediction [0]
  return jsonify (output)


if __name__== "__main__":
    app.run(debug=True)
    
#for json ie importing data from excel use request.py filr in which
# import requests
# #url=''
    

##chatbot 
# import the response function of the model in flask app
# from chat import function_name    