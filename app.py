from flask import Flask, request, send_file, render_template
import pandas as pd
from io import StringIO, BytesIO

app = Flask(__name__)

@app.route('/process_csv', methods=['POST'])
def process_csv():
  if 'csv_file' not in request.files:
    return "No file part", 400
    
  file = request.files['csv_file']
  
  if file.filename == '':
    return "No selected file", 400
  
  if file and file.filename.endswith('.csv'):
    # Read the CSV file
    df = pd.read_csv(file)
    return df.shape
  

if __name__ == "__main__":
  app.run(debug=True)