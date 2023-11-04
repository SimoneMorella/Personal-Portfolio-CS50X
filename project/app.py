from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_name = request.form['sender_name']
    sender_email = request.form['sender_email']
    subject = request.form['subject']
    message = request.form['message']
    # print(sender_name, sender_email, subject, message)

    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = 'ec5affedd2b1df'
    password = 'd7e7f3075a225c'

    sender_email1 = 'mailtrap@example.com'
    receiver_email = "flasktrial2117@gmail.com"
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email1
    msg["To"] = receiver_email
    text_part = MIMEText(f'Hi, you received a message from {sender_name} that indicated email is {sender_email}. Here the text it was written:\n\n {message}', 'plain')
    msg.attach(text_part)
    try:
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login(login, password)
            server.sendmail(
                sender_email1, receiver_email, msg.as_string()
            )
            flash("Email sent successfully!", "success")
            server.quit()
    except Exception as e:
        flash(f"Error in sending the email: {str(e)}", "error")


    return redirect('/#contact')
    