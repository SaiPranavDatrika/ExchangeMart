from pyravendb.store import document_store
import os
from flask import Flask,request ,render_template , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Set up RavenDB document store
class USERS:
     def __init__(self,username,password,email) -> None:
          self.username=username
          self.password=password
          self.email=email

class Items:
      def __init__(self,Itemid,productname,productprice) -> None:
            self.Itemid=Itemid
            self.productname=productname
            self.productprice=productprice
class Reviews:
      def __init__(self,ReviewId,Username,Description) -> None:
            self.ReviewId=ReviewId
            self.username=Username
            self.Description=Description
class Shares:
      def __init__(self,username,Itemshared,itemreference) -> None:
             self.username=username
             self.Itemshared=Itemshared
             self.itemreference=itemreference 

certificate="/Users/sunilachandu/Desktop/ExchangeMart/free.exchangemart.client.certificate/free.exchangemart.client.certificate.pfx"
cloud_cert="/Users/sunilachandu/Desktop/ExchangeMart/free.exchangemart.client.certificate/PEM/free.exchangemart.client.certificate.pem"
pass_key="71CC4A8860EB5292567D33763E48145"
database_name="Exchangemart"
client_cert = {
    "cert_file": os.path.abspath(cloud_cert),
    "password": "71CC4A8860EB5292567D33763E48145"
}
urls=["https://a.free.exchangemart.ravendb.cloud"]

store = document_store.DocumentStore(urls,database_name,cloud_cert)

store.initialize()
session = store.open_session()

@app.route("/members")
def members():
    print("pranav")
    return ({"name":["pranav","LOVE"]})

@app.route('/process', methods=['POST'])
def process():
      data = request.get_json()
      name=data.get('name')
      email=data.get('email')
      password=data.get('password')
    # Process the data or perform any backend tasks
    # ...

      # Return a response back to the frontend
      users=USERS(name,password,email)
      session.store(users)
      session.save_changes()

      response = {
        "status": "success",
        "message": "Data received successfully!"
      }
    
      return jsonify(response)

@app.route('/validate', methods=['POST'])
def validate():
      data=request.get_json()
      email=data.get('email')
      password=data.get('password')
      query = session.query(USERS).where_equals("email", email)
      print(query)
      
      if query and query.password == password:
        return jsonify({'valid': True}), 200
      else:
        return jsonify({'valid': False}), 401

        
if __name__ == '__main__':
    app.run(debug=True,port=5000)



# Perform operations with the document store
# For example, store.open_session(), store.execute_index(), etc.

# Don't forget to dispose of the store when done

