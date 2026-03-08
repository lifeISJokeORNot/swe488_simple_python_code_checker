"""
Simple Flask web interface for the code checker
"""

from flask import Flask, request, render_template_string
import checker
import os

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Code Checker</title></head>
<body style="font-family: sans-serif; max-width: 800px; margin: 50px auto;">
<h1>🐍 Python Code Checker</h1>
<form method="post" enctype="multipart/form-data">
    <input type="file" name="file" accept=".py" required>
    <button type="submit">Check Code</button>
</form>
{% if issues %}
    <h2>Results:</h2>
    <ul style="background: #f0f0f0; padding: 20px;">
    {% for issue in issues %}
        <li>{{ issue }}</li>
    {% endfor %}
    </ul>
    <p><strong>Total: {{ issues|length }} issues</strong></p>
{% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    issues = []
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.py'):
            content = file.read().decode('utf-8').splitlines()
            issues = checker.check_code(content)
    return render_template_string(HTML, issues=issues)

if __name__ == '__main__':
    app.run(debug=True)
