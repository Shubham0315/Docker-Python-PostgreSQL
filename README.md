# Docker-Python-PostgreSQL
To create simple python web application using Flask that connects to PostgreSQL database. Use docker to containerize both the Python and PostgreSQL, and docker compose to manage them together

Key Concepts
-
- Flask : A lightweight Python web framework
- PostgreSQL : A relational DB to store data
- Docker : A tool to containerize applications for portability
- Docker Compose : A tool to run multi container apps

- By the end of project, we'll have Flask app connected to PostgreSQL running inside docker container

--------------------------------------------------------------

Create app.py - Python application
-
![image](https://github.com/user-attachments/assets/18450cbe-66ba-4d87-8e98-7371c634a25b)

- Flask :- Web framework for the app
- psycopg2 :- Connects Python to PostgreSQL
- DATABASE_URL :- Gets DB URL from env variable

--------------------------------------------------------------

Write dockerfile
-
![image](https://github.com/user-attachments/assets/0067df09-8b30-4fe9-9ba1-02b6697d65b0)

- FROM :- Uses lightweight python image
- COPY :- Copies necessary files into container
- RUN pip install :- Installs required python packages
- CMD :- Runs FLASK app when container starts

--------------------------------------------------------------

Write requirements.txt
-
Flask
psycopg2-binary

- Flask :-For the web framework
- psycopg2-binary :- To connect to PostgreSQL

--------------------------------------------------------------

Write docker compose
-
![image](https://github.com/user-attachments/assets/845a5c46-0f23-463a-ad3d-8a5de0c4e38f)

- web :- builds app from dockerfile, expose port 5000, env sets DB URL
- db :- postgreSQL image used, stores DB data persistently

--------------------------------------------------------------

Run the application
-
- Command :- docker-compose up --build
- Open browser and open http://localhost:5000 to access
