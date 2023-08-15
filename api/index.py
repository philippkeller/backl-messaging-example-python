from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """<h4>Your backl.io messaging API is running! 🥳</h4>
    <p>Use {yourdomain}/message in the backlink builder to start using it.</p>
    <p>To adapt it, edit ✍️ <code>api/index.py</code></p>
    """

@app.route('/message')
def message():
    from pprint import pprint
    p = request.get_json()
    pprint(p)
    subject = 'Links on your site "{prospect_title}"'.format(**p)
    email = p["email_address"]
    if '.' in email.split('@')[0]:
        name = email.split('@')[0].split('.')[0].capitalize()
    else:
        name = 'there'

    if p['prospect_title_above_link']:
        extra_section = ' under the section "{prospect_title_above_link}"'.format(**p)
    else:
        extra_section = ''
    body = """Hi {name},

My name is {my_first_name} and I'm the founder of {my_domain}: {my_claim}.

I found your site "{prospect_title}" and noticed that you link to similar tools.

Question: would you mind adding a link to {my_domain}{extra_section}? It would mean the world to me!

Greets
{my_first_name}
""".format(name=name, extra_section=extra_section, **p)
    return dict(subject=subject, body=body)