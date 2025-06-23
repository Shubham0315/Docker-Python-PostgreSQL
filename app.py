from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

@app.route('/')
def hello():
  cur.execute("SELECT 'Hello, World!'")
  result = cur.fetchone()
  return result[0]
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
