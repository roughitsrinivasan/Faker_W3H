from ss import  screenshot
from faker import Faker
import json 
from flask import Flask, render_template ,send_file 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html") 

@app.route("/id", methods=['POST','GET'])
def start():
    fake = Faker()
    name = "Name : "+fake.name()
    email_id = "Email-id : "+fake.email()
    address = "Address : "+fake.address()
    city = "City : "+fake.city()
    phone = "Phone Number : "+fake.phone_number()
    print(name)
    print(email_id)
    print(address)
    print(city)
    return render_template("index.html",result=name,result2=address,result1=email_id,result3=city,result4=phone)



@app.route('/take_screenshot',methods = ['GET'])
def download():
    text = "info"
    screenshot(text)
    filename = text +'.png'
    return send_file(filename,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)