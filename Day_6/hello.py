from flask import Flask
from isprime import isPrime

app = Flask(__name__)

@app.route('/') 
def hundred_primes():
	return str(isPrime(10))
	
if __name__ =="__main__":
	app.run(debug=True)
