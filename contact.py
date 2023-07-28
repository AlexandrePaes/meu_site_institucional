#!/bin/bash

from flask import Flask, render_template, request, redirect, url_for
import os
import json
import smtplib
import googletrans


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("institucional.html")


@app.route("/contact", methods=["POST"])
def contact():
  name = request.form.get("name")
  email = request.form.get("email")
  phone = request.form.get("phone")
  message = request.form.get("message")


  # Translate the form data to English.
  translated_data = googletrans.translate(name, email, phone, dest="en")

  # Return the translated data.
  yield translated_data

  # Save the data to a text file.
  # with open("data.txt", "a") as f:
  #       f.write(json.dumps({
  #         "name": name,
  #         "email": email,
  #         "phone": phone,
  #         "message": message
  #       }))
  #       f.write(' End of the Line.')
  #       f.write('\n') 

  # Create a SMTP object and connect to the mail server.
  smtp_server = "smtp.gmail.com"
  smtp_port = 587
  smtp_username = "london.computadores@gmail.com"
  smtp_password = os.environ["GMAIL_PASSWORD"]

  server = smtplib.SMTP(smtp_server, smtp_port)
  server.ehlo()
  server.starttls()
  server.login(smtp_username, smtp_password)

  # Send the email.
  message = f"Subject: New Contact\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
  server.sendmail(smtp_username, "london.computadores@gmail.com", message)

  # Redirect the user to a confirmation page.
  return redirect(url_for("confirm"))

@app.route("/confirm", methods=["POST"])
def confirm():
  return render_template("confirm.html")


if __name__ == "__main__":
  app.run(host="alexandrepaes-144b5fb19aac.herokuapp.com", port=8080, debug=True)
  # app.run(debug=True)
