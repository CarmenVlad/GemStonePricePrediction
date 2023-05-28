from flask import Flask,render_template,jsonify,request
import util_gemstone

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict_price():
    carat=float(request.form['carat'])
    cut=request.form['cut']
    clarity=request.form['clarity']
    depth=float(request.form['depth'])
    table=float(request.form['table'])
    color=request.form['color']
    x=float(request.form['x'])
    y=float(request.form['y'])
    z=float(request.form['z'])
    return render_template('index.html',prediction_text=f'Estimted price : {str(float(util_gemstone.get_estimated_price(carat,cut,color,clarity,depth,table,x,y,z)))}')
if __name__ == "__main__":
    util_gemstone.load_saved_artifacts()
    app.run(debug=True)

