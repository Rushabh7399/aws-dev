from fastapi import FastAPI, Form
import psycopg2

app = FastAPI()

DB_HOST = "database-1.cj2ccse0elz9.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "rashah99"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.get("/")
def form():
    return """
    <html>
        <body>
            <form action="/submit" method="post">
                Name: <input type="text" name="name"><br>
                Password: <input type="text" name="password"><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/submit")
def submit(name: str = Form(...), password: str = Form(...)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT);")
    cur.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Data inserted successfully"}
