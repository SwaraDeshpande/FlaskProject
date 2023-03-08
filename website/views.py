from flask import  jsonify, render_template, request , Blueprint
from . import db
from .models import Company

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/company', methods=['GET', 'PUT'])
def company():
    if request.method == 'GET':
        company = Company.query.first()
        if company:
            return jsonify({'name': company.name})
        else:
            return jsonify({'error': 'No company found'})
    else:
        company = Company.query.first()
        if company:
            company.name = request.json['name']
            db.session.commit()
            return jsonify({'name': company.name})
        else:
            new_company = Company(request.json['name'])
            db.session.add(new_company)
            db.session.commit()
            return jsonify({'name': new_company.name})

