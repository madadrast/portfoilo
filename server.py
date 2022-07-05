from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('./database.csv' , mode='a',newline='' ) as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"' , quoting = csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])
       
        
        
@app.route('/submitted_form' , methods = ['POST','GET'])
def submitted_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'The data not saved in database!'
    else:
        return 'Somthing went wrong, Trya again!!!'
    
    
    


#@app.route('/index.html')
#def home2():
#    return render_template('index.html')
#
#@app.route('/works.html')
#def works():
#    return render_template('works.html')
#
#
#@app.route('/about.html')
#def about():
#    return render_template('about.html')
#
#
#@app.route('/contact.html')
#def contact():
#    return render_template('contact.html')
#
#
#@app.route('/components.html')
#def components():
#    return render_template('components.html')