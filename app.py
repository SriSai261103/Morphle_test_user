from flask import Flask, jsonify
import os
import time
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get your full name (replace with your actual name)
    name = "Your Full Name"
    
    # Get system username
    username = os.getlogin()
    
    # Get server time in IST
    server_time_ist = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Run top command and capture output
    top_output = subprocess.getoutput('top -b -n 1')
    
    # Format the data as a dictionary
    data = {
        "Name": name,
        "Username": username,
        "Server Time (IST)": server_time_ist,
        "TOP output": top_output
    }
    
    # Return data as JSON
    return jsonify(data)

if _name_ == '_main_':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
