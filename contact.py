#!/bin/bash

import os
from flask import Flask, render_template, request, redirect, url_for
import json
# import shelve
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


  # # With shelve 
  # with shelve.open("contacts") as db:
  #   # Add the new contact to the database.
  #   db[name] = {
  #     "name": name,
  #     "email": email,
  #     "phone": phone,
  #   }

  # Translate the form data to English.
  translated_data = googletrans.translate(name, email, phone, dest="en")

  # Return the translated data.
  yield translated_data

  # Save the data to a text file.
  with open("data.txt", "a") as f:
        f.write(json.dumps({
          "name": name,
          "email": email,
          "phone": phone,
          "message": message
        }))
        f.write(' End of the Line.')
        f.write('\n')
           
  # os.system('cat data.txt >> dados.txt') 

  # Redirect the user to a confirmation page.
  return redirect(url_for("confirm"))

@app.route("/confirm")
def confirm():
  return render_template("confirm.html")

# os.system('cat data.txt >> dados.txt \n')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
  # app.run(debug=False)
