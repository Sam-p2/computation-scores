@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Your logic here
        # Collect input from the form and process it
    return render_template('index.html', result=result)

