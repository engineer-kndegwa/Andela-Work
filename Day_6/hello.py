from flask import Flask
from isprime import isPrime

app = Flask(__name__)

@app.route('/') 
def hundred_primes():
	return str(isPrime(10))
	
	
@app.route('/<int:n>',methods = ['GET'])

def get_first_n_primes(n):
	return str(isPrime(n))
	
if __name__ =="__main__":
	app.run(debug=True)
