from flask import Flask,redirect,render_template,request,session,jsonify
import random
import time
app = Flask(__name__)
app.secret_key = 'NinjaGold'
@app.route('/')
def index():
	if not 'gold' in session:
		session['gold']=0
		session['activity']=[]
	return render_template('gold.html')
# @app.route('/process_money',methods=['post'])
# def submit():
# 	case = request.form['building']
# 	if case == 'farm':
# 		session['earned'] = random.randint(10,20)
# 		session['gold']+=session['earned']
# 		session['activity'].append("Earned {} golds from the farm!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
# 	elif case == 'cave':
# 		session['earned'] = random.randint(5,10)
# 		session['gold']+=session['earned']
# 		session['activity'].append("Earned {} golds from the cave!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
# 	elif case == 'house':
# 		session['earned'] = random.randint(2,5)
# 		session['gold']+=session['earned']
# 		session['activity'].append("Earned {} golds from the house!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
# 	elif case == 'casino':
# 		session['earned']=random.randint(-50,50)
# 		print session['earned']
# 		session['gold']+=session['earned']
# 		if session['earned'] >= 0:
# 			session['activity'].append("Entered a casino and lost {} golds... Ouch..({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
# 		else:
# 			session['activity'].append("Earned {} golds from the casino!({})".format(0-session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
# 	# return False
# 	return redirect('/')
# @app.route('/response')
# def res():
# 	response = {'gold':session['gold'],'activity': session['activity'],'earned':session['earned']}
# 	return jsonify(response)
@app.route('/response')
def res():
	case = request.args.get('building','',type=str)
	print case
	if case == 'farm':
		session['earned'] = random.randint(10,20)
		session['gold']+=session['earned']
		session['activity'].append("Earned {} golds from the farm!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
	elif case == 'cave':
		session['earned'] = random.randint(5,10)
		session['gold']+=session['earned']
		session['activity'].append("Earned {} golds from the cave!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
	elif case == 'house':
		session['earned'] = random.randint(2,5)
		session['gold']+=session['earned']
		session['activity'].append("Earned {} golds from the house!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
	elif case == 'casino':
		session['earned']=random.randint(-50,50)
		# print session['earned']
		session['gold']+=session['earned']
		if session['earned'] <= 0:
			session['activity'].append("Entered a casino and lost {} golds... Ouch..({})".format(0-session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
		else:
			session['activity'].append("Earned {} golds from the casino!({})".format(session['earned'],time.strftime('%y/%m/%d %I:%M %p')))
			print session['earned']
	response = {'gold':session['gold'],'activity': session['activity'],'earned':session['earned']}
	return jsonify(response)

@app.route('/reset')
def reset():
	session.pop('gold')
	session.pop('activity')
	session.pop('earned')
	return redirect('/')
	
app.run(debug=True)