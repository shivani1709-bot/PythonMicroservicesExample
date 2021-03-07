from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'secret-key'


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test1.db"


@app.before_first_request
def create_tables():
    db.create_all()


db = SQLAlchemy(app)


class MyTableNew(db.Model):
    rule_name = db.Column(db.String(120), primary_key=True, nullable=False)
    country = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(120), nullable=False)
    group_id = db.Column(db.String(120), nullable=False)
    device_id = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(120), nullable=True)
    event_name = db.Column(db.String(120), nullable=False)
    fault_type = db.Column(db.String(120), nullable=True)
    resource_name = db.Column(db.String(120), nullable=True)
    operator = db.Column(db.String(120), nullable=True)
    resource_value = db.Column(db.String(120), nullable=True)
    action_type = db.Column(db.String(120), nullable=False)
    emails = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    email_content = db.Column(db.String(120), nullable=False)

    def __init__(self, rule_name, country, state, region, group_id, device_id, status, event_name,fault_type,resource_name,operator,resource_value,
                 action_type, emails,subject, email_content):
        self.rule_name = rule_name
        self.country = country
        self.state = state
        self.region = region
        self.group_id = group_id
        self.device_id = device_id
        self.state = status
        self.event_name = event_name
        self.action_type = action_type
        self.emails = emails
        self.subject = subject
        self.email_content = email_content
        self.fault_type = fault_type
        self.resource_value = resource_value
        self.resource_name = resource_name
        self.operator = operator


@app.route('/')
def hello():
    return jsonify('Hello Shivani, welcome!')


@app.route("/param", methods=['POST'])
def MyParam():
    print(request.json)
    data = request.json
    entry = MyTableNew(rule_name=data['rule_name'], country=data['country'], state=data['state'], region=data['region'], group_id=data['group_id'],
    device_id =data['device_id'], status=data['status'], fault_type=data['fault_type'], resource_value=data['resource_value'], resource_name=data['res_name'],operator=data['operator'], event_name=data['event_name'], action_type=data['action_type'], emails=data['emails'], subject=data['subject'], email_content=data['email_content'])
    db.session.add(entry)
    db.session.commit()
    return jsonify('Got the data!!!')
