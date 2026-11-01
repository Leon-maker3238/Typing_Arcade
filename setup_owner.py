"""Configure the requested local Owner account without deleting game progress."""
import os
from werkzeug.security import generate_password_hash
import app

username=os.environ.get('OWNER_USERNAME')
password=os.environ.get('OWNER_PASSWORD')
if not username or not password:
    raise SystemExit('Missing Owner settings')
app.init()
with app.db() as conn:
    owner=conn.execute("SELECT id,username FROM users WHERE role='owner' ORDER BY id LIMIT 1").fetchone()
    if owner is None:
        conn.execute("INSERT INTO users(username,first_name,passhash,role,status,coins) VALUES(?,?,?,'owner','approved',5000)", (username,username,generate_password_hash(password)))
        print('Owner account created.')
    elif owner['username'] != username:
        collision=conn.execute('SELECT id FROM users WHERE username=? AND id!=?',(username,owner['id'])).fetchone()
        if collision:
            raise SystemExit('Username is already taken by another account. No changes made.')
        conn.execute("UPDATE users SET username=?,first_name=?,passhash=?,status='approved',blocked=0 WHERE id=?",(username,username,generate_password_hash(password),owner['id']))
        print('Existing Owner account updated; game progress preserved.')
    else:
        conn.execute("UPDATE users SET passhash=?,status='approved',blocked=0 WHERE id=?",(generate_password_hash(password),owner['id']))
        print('Owner password updated; game progress preserved.')
