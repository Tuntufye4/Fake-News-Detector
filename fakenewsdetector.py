import pickle

var = input("Please enter the news text you want to verify:")
print("You entered: "+ str(var))

def fakenews(var):

 load_model = pickle.load(open('c:\data\model.sav','rb'))
 prediction = load_model.predict([var])
 prob = load_model.predict_proba([var])


 return (print("The given statement is ",prediction[0]),("The truth probability score is",prob[0][1]))


if_name_=='_main_':
   fakenews(var)