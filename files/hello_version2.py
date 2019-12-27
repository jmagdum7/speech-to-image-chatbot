from flask import Flask, redirect, url_for, render_template, session, escape, request, jsonify
# from flask_mysqldb import MySQL
# import numpy as np
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from collections import defaultdict
# from surprise import Dataset
# from surprise import SVDpp
# from surprise import accuracy
# from surprise.model_selection import train_test_split
# from surprise import Reader

#chatbot import starts
import numpy as np
import tensorflow as tf
import pickle
import json
import tflearn
import nltk
import json
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import random
#chatbot import ends





app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'elearn'

# mysql = MySQL(app)

app.secret_key = 'secretkey' 

#chatbot setup starts
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

with open('new_intents.json') as json_data:
    intents = json.load(json_data)

tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('./model.tflearn')
#chatbot setup ends



@app.route('/')
def index():
	return redirect(url_for('login'))	

@app.route('/newbox')
def newboxes():
	return render_template('newbox.html')

# @app.route('/receiver', methods = ['POST'])
# def worker():
# 	data = request.body.decode('utf-8') 
# 	received_json_data = json.loads(data)
# 	item = received_json_data['a']
# 	print(item)
# 	return item

@app.route('/chatbot',methods=['GET','POST'])
def chatbots():
	return render_template('chatbot.html')

@app.route('/intents', methods=['GET', 'POST'])
def intents_add():
	return render_template('add_intents.html')


@app.route('/add_intent', methods=['GET', 'POST'])
def add_intent():
	data = request.form
	tag = data['tag']
	pattern = data['pattern'].split(',')
	resp = data['response'].split(',')
	with open('new_intents.json') as json_data:
		intents1 = json.load(json_data)
	for intent in intents1['intents']:
		if intent['tag'] == tag:
			return render_template('add_intents.html')
	intents1['intents'].append({'tag': tag, 'patterns': pattern, 'responses': resp})
	# with open('new2.json', 'w') as w:
	# 	w.write(str(intents))
	new_intent = json.dumps(intents1)
	f = open("new_intent.json","w")
	f.write(new_intent)
	f.close()
	return render_template('add_intents.html')
    

@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()
    print (data)
    data['location'] = response(data['location'])
    if data['location'] != None:
    	data['length'] = len(str(data['location']).split(','))
    else:
    	data['length'] = 0
    return jsonify(data)

# @app.route('/profile',methods=['GET','POST'])
# def profile():
# 	if 'username' in session:
# 		username = session['username']
# 		#return str(username)
# 		if username == 0:
# 			return redirect(url_for('login'))

# 		if request.method == 'POST':
# 			session['username'] = request.form['user_name']
# 			username = session['username']
# 			email = request.form['user_email']
# 			rollno = request.form['user_rollno']
# 			password = request.form['user_password']
# 			year = request.form['year']
# 			dept = request.form['dept']
# 			langlist = request.form.getlist('language')
# 			intlist = request.form.getlist('interests')
			
# 			print(langlist)
# 			language = ' '.join(langlist)
# 			print(language)
			
# 			print(intlist)
# 			interest = ' '.join(intlist)
# 			print(interest)

# 			cur = mysql.connection.cursor()
# 			cur.execute("update users set rollno={},name='{}',year={},dept='{}',language='{}',interest='{}',password='{}',email='{}';".format(rollno,username,year,dept,language,interest,password,email))
			


# 		cur = mysql.connection.cursor()
# 		cur.execute("select * from users where name = '{}';".format(username))
# 		userdata = cur.fetchone()
# 		langlist = list(userdata[4].split(" "))
# 		intlist = list(userdata[5].split(" "))

# 		print(userdata)
# 		print(langlist)
# 		print(intlist)
# 		return render_template('profile.html',userdata=userdata,langlist=langlist,intlist=intlist)	
			
# 	return redirect(url_for('login'))
	
 
# @app.route('/login',methods=['GET','POST'])
# def login():
# 	if 'username' not in session:
# 		session['username'] = 0

# 	if request.method == 'POST':
# 		session['username'] = request.form['username']
# 		passwordform = request.form['password']

# 		if 'username' in session:
# 			username = session['username']
# 			#print str(username)
# 			if username == 0:
# 				return redirect(url_for('login'))
			
# 			cur = mysql.connection.cursor()
# 			cur.execute("select count(1) from users where name = '{}';".format(username))
# 			#return str(cur.fetchone()[0])
# 			rollno = cur.fetchone()[0]
# 			if not rollno:
# 				return 'Invalid Username'

# 			cur.execute("select password from users where name = '{}';".format(username))
# 			password = cur.fetchone()
# 			#print str(password[0])
# 			if passwordform == password[0]:

# 				#return str(session['username']+' '+password)
# 				return redirect(url_for('home'))
	
# 	return render_template('login.html')

# @app.route('/logout')
# def logout():
# 	session.pop('username',None)
# 	return redirect(url_for('login'))

# @app.route('/register',methods=['GET','POST'])
# def register():
# 	if request.method == 'POST':
# 		session['username'] = request.form['user_name']
# 		username = session['username']
# 		email = request.form['user_email']
# 		rollno = request.form['user_rollno']
# 		password = request.form['user_password']
# 		year = request.form['year']
# 		dept = request.form['dept']
# 		language = request.form.getlist('language')
# 		interest = request.form.getlist('interest')

# 		cur = mysql.connection.cursor()
# 		cur.execute("insert into users values({},'{}',{},'{}','{}','{}','{}','{}');".format(rollno,username,year,dept,language,interest,password,email))

# 	return render_template('register.html')

# @app.route('/home')
# def home():
# 	if 'username' in session:
# 		username = session['username']
# 		#return str(username)
# 		if username == 0:
# 			return redirect(url_for('login'))

# 		return render_template('home.html',uname=username)	
			
# 	return redirect(url_for('login'))

# @app.route('/courses')
# def courses():
# 	if 'username' in session:
# 		username = session['username']
# 		#return str(username)
# 		if username == 0:
# 			return redirect(url_for('login'))

# 		courselist = []
# 		ratelist = []
# 		cur = mysql.connection.cursor()
# 		cur.execute("select * from cources;")
# 		rv = cur.fetchall()
# 		for item in rv:
# 			courselist.append(item)
# 			cur.execute("select avg(rating) from globalhist where id='{}';".format(item[0]))
# 			value = cur.fetchone()
# 			print(value)
# 			ratelist.append(value)

# 		data = dict(zip(courselist,ratelist))
# 		return render_template('allcourses.html',uname=username,data=data)	
			
# 	return redirect(url_for('login'))

# @app.route('/singlecourse/<cid>',methods=['GET','POST'])
# def singlecourse(cid):
# 	if 'username' in session:
# 		username = session['username']
# 		#return str(username)
# 		if username == 0:
# 			return redirect(url_for('login'))
		
# 		cur = mysql.connection.cursor()

# 		cur.execute("select rollno from users where name = '{}';".format(username))
# 		uid = cur.fetchone()

# 		if request.method == 'POST':
# 			rating = request.form['rating']
# 			status = request.form['status']
# 			print(rating)
# 			print(status)
# 			cur.execute("select * from globalhist where id='{}' and rollno = '{}';".format(cid,uid[0]))
# 			rv = cur.fetchone()
# 			if not rv:
# 				cur.execute("insert into globalhist values ({},'{}','{}',{});".format(uid[0],cid,status,rating))
# 			else:
# 				cur.execute("update globalhist set rollno = {},id = '{}',status = '{}',rating = {} where rollno = {} and id = '{}';".format(uid[0],cid,status,rating,uid[0],cid))
		

		
# 		#print(uid)

# 		cur.execute("select * from cources where id = '{}';".format(cid))
# 		cc = cur.fetchone()
# 		#print(cc)

# 		cur.execute("select * from globalhist where id = '{}' and rollno = '{}';".format(cid,uid[0]))
# 		gh = cur.fetchone()
# 		#print(gh)

# 		recommend1 = []
# 		recommend1=findrec1(cc[1])
# 		reclist1 = []
# 		for title in recommend1:
# 			cur.execute("select * from cources where title='{}';".format(title))
# 			item=cur.fetchone()
# 			reclist1.append(item)

# 		return render_template('singlecourse.html',uname=username,cc=cc,gh=gh,r1=reclist1)
# 	return redirect(url_for('login'))

# @app.route('/recommend')
# def recommend():
# 	if 'username' in session:
# 		username = session['username']
# 		#return str(username)
# 		if username == 0:
# 			return redirect(url_for('login'))
		
# 		# cur = mysql.connection.cursor()
# 		# cur.execute("select count(1) from users where name = '{}';".format(username))
# 		# #return str(cur.fetchone()[0])
# 		# rollno = cur.fetchone()[0]
# 		# if not rollno:
# 		# 	return 'Invalid Username'

# 		# cur.execute("select password from users where name = '{}';".format(username))
# 		# password = cur.fetchone()
# 		# #return str(password[0])
# 		# if request.args.get('pwd') == password[0]:
			
# 		# activecourse = []
# 		# cur.execute("select id from globalhist where rollno = {} and status != 100;".format(rollno))
# 		# rv = cur.fetchall()
# 		# for cid in rv:
# 		# 	cur.execute("select title from cources where id = '{}';".format(str(cid[0])))
# 		# 	title = cur.fetchone()
# 		# 	activecourse.append(title)ffff
# 		# 	#print(activecourse[0])
# 		# recommend1 = []
# 		# recommend1=findrec1(str(activecourse[-1][0]))
# 		cur = mysql.connection.cursor()
		
# 		recommend2 = []
# 		recommend2=findrec2(username)
# 		reclist2 = []
# 		for title in recommend2:
# 			cur.execute("select * from cources where title='{}';".format(title))
# 			item=cur.fetchone()
# 			reclist2.append(item)

# 		recommend3 = []
# 		recommend3=findrec3(username)
# 		reclist3 = []
# 		for title in recommend3:
# 			cur.execute("select * from cources where title='{}';".format(title))
# 			item=cur.fetchone()
# 			reclist3.append(item)

# 		return render_template('recommend.html',uname=username,r2=reclist2,r3=reclist3)
# 	return redirect(url_for('login'))

# @app.route('/test')
# def test():
# 	return render_template('user_history.html')



# def findrec1(ac):
# 	cur = mysql.connection.cursor()
	
# 	cur.execute("select title,year,dept,language from cources;")
# 	rv = cur.fetchall()
# 	souplist = []
# 	for item in rv:
# 		souplist.append(str(item[0])+' '+str(item[1])+' '+str(item[2])+' '+str(item[3]))
	
# 	cur.execute("select title from cources;")
# 	rv = cur.fetchall()
# 	titlelist = []
# 	for item in rv:
# 		titlelist.append(str(item[0]))

# 	listdata = [('title',titlelist),('soup',souplist)]
# 	data = pd.DataFrame.from_items(listdata)

# 	count = CountVectorizer(stop_words='english')
# 	count_matrix = count.fit_transform(data['soup'])
# 	cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
# 	data = data.reset_index()
# 	indices = pd.Series(data.index, index=data['title'])

# 	def get_recommendations(title, cosine_sim=cosine_sim2):
    
# 	    idx = indices[title]
# 	    print(idx)
# 	    sim_scores = list(enumerate(cosine_sim[idx]))
# 	    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# 	    sim_scores = sim_scores[1:5]
# 	    course_indices = [i[0] for i in sim_scores]
# 	    return data['title'].iloc[course_indices]

# 	rec=get_recommendations(ac,cosine_sim2)
# 	#print(type(rec))
# 	recommend1 = []
# 	recommend1.append(rec.iloc[0])
# 	recommend1.append(rec.iloc[1])
# 	recommend1.append(rec.iloc[2])
# 	recommend1.append(rec.iloc[3])
# 	return recommend1

# def findrec2(un):
# 	cur = mysql.connection.cursor()
	
# 	cur.execute("select year,dept,language from cources;")
# 	rv = cur.fetchall()
# 	coursesouplist = []
# 	for item in rv:
# 		coursesouplist.append(str(item[0])+' '+str(item[1])+' '+str(item[2]))

# 	cur.execute("select year,dept,language from users;")
# 	rv = cur.fetchall()
# 	usersouplist = []
# 	for item in rv:
# 		usersouplist.append(str(item[0])+' '+str(item[1])+' '+str(item[2]))
	
# 	cur.execute("select name from users;")
# 	rv = cur.fetchall()
# 	userlist = []
# 	for item in rv:
# 		userlist.append(str(item[0]))

# 	cur.execute("select title from cources;")
# 	rv = cur.fetchall()
# 	titlelist = []
# 	for item in rv:
# 		titlelist.append(str(item[0]))

# 	courselistdata = [('soup',coursesouplist),('title',titlelist)]
# 	coursedata = pd.DataFrame.from_items(courselistdata)

# 	userlistdata = [('soup',usersouplist),('name',userlist)]
# 	userdata = pd.DataFrame.from_items(userlistdata)

# 	# print(coursedata['soup'])
# 	# print(userdata['soup'])
	

# 	count = CountVectorizer(stop_words='english')
# 	course_matrix = count.fit_transform(coursedata['soup'])
# 	user_matrix = count.fit_transform(userdata['soup'])
# 	# print(course_matrix.shape)
# 	# print(user_matrix.shape)
# 	cosine_sim2 = cosine_similarity(user_matrix,course_matrix)
# 	userdata = userdata.reset_index()
# 	indices = pd.Series(userdata.index, index=userdata['name'])

# 	def get_recommendations(name, cosine_sim=cosine_sim2):
    
# 	    idx = indices[name]
# 	    sim_scores = list(enumerate(cosine_sim[idx]))
# 	    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# 	    sim_scores = sim_scores[1:5]
# 	    course_indices = [i[0] for i in sim_scores]
# 	    return coursedata['title'].iloc[course_indices]

# 	rec=get_recommendations(un,cosine_sim2)
# 	#print(type(rec))
# 	recommend2 = []
# 	recommend2.append(rec.iloc[0])
# 	recommend2.append(rec.iloc[1])
# 	recommend2.append(rec.iloc[2])
# 	recommend2.append(rec.iloc[3])
# 	return recommend2

# def findrec3(un):

# 	def get_top_n(predictions, n=10):
# 	    '''Return the top-N recommendation for each user from a set of predictions.

# 	    Args:
# 	        predictions(list of Prediction objects): The list of predictions, as
# 	            returned by the test method of an algorithm.
# 	        n(int): The number of recommendation to output for each user. Default
# 	            is 10.

# 	    Returns:
# 	    A dict where keys are user (raw) ids and values are lists of tuples:
# 	        [(raw item id, rating estimation), ...] of size n.
# 	    '''

# 	    # First map the predictions to each user.
# 	    top_n = defaultdict(list)
# 	    for uid, iid, true_r, est, _ in predictions:
# 	        top_n[uid].append((iid, est))

# 	    # Then sort the predictions for each user and retrieve the k highest ones.
# 	    for uid, user_ratings in top_n.items():
# 	        user_ratings.sort(key=lambda x: x[1], reverse=True)
# 	        top_n[uid] = user_ratings[:n]

# 	    return top_n

# 	cur = mysql.connection.cursor()
	
# 	cur.execute("select rollno,id,rating from globalhist;")
# 	rv = cur.fetchall()
# 	surpriselist = []
# 	for item in rv:
# 		surpriselist.append(item)
# 	#print(surpriselist)
# 	labels = ['userid','courseid','rating']
# 	df = pd.DataFrame.from_records(surpriselist,columns=labels)

# 	cur.execute("select id,title from cources;")
# 	rv = cur.fetchall()
# 	courselist = []
# 	for item in rv:
# 		courselist.append(item)
# 	#print(courselist)
# 	labels = ['id','title']
# 	coursedf = pd.DataFrame.from_records(courselist,columns=labels)

# 	print(coursedf.index)
# 	reader = Reader(rating_scale=(1, 5))

# 	data = Dataset.load_from_df(df[['userid','courseid','rating']],reader)

# 	trainset, testset = train_test_split(data, test_size=.50)

# 	algo = SVDpp()

# 	algo.fit(trainset)
# 	predictions = algo.test(testset)
# 	print(predictions)

# 	top_n = get_top_n(predictions,n=4)
# 	print(top_n.items())
	
# 	cur.execute("select rollno from users where name = '{}';".format(un))
# 	rv=cur.fetchone()
# 	givenid=rv[0]
# 	#print(givenid)
# 	for uid,user_ratings in top_n.items():
# 		if(givenid == uid):
# 			rec3 =  [coursedf.iloc[coursedf[coursedf['id']==iid].index.item(),1] for (iid, _) in user_ratings]
# 			print(rec3)
# 			return rec3


#chatbot utilities starts
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))
#chatbot utilities ends

#chatbot main starts
# create a data structure to hold user context
context = {}
flag = 0
ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    flag = 0
    results = classify(sentence)
#     print(results)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
#                         return print(random.choice(i['responses']))
                        if i['responses']=="":
                            print("no rating")
                        if i['tag']=="greeting" or i['tag']=="goodbye":
                            flag = 1
                            return random.choice(i['responses'])
                        else:
                            flag = 1
                            return i['responses']
            results.pop(0)
#chatbot main ends            


if __name__ == '__main__':
   app.run(debug=True)
   
