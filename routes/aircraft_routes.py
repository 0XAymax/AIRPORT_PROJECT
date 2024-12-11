from flask import Blueprint, render_template, request
from models.aircraft import Aircraft

aircraft_routes = Blueprint('aircraft_routes', __name__)

@aircraft_routes.route('/aircraft/<int:numav>', methods=['GET'])

def get_aircraft(numav):
    aircraft = Aircraft.get_by_id(numav)
    if aircraft:
        return render_template('aircraft.html', aircraft=aircraft, search_results=None)
    return render_template('aircraft.html', aircraft=None, search_results=None)

@aircraft_routes.route('/aircraft/search', methods=['GET'])

def search_aircraft_by_type():
    name = request.args.get('aircraft_type')
    if name:
        search_results = Aircraft.get_by_name(name)
        return render_template('aircraft.html', aircraft=None, search_results=search_results)
    return render_template('aircraft.html', aircraft=None, search_results=[])

@aircraft_routes.route('/aircraft/<int:numav>/status', methods=['GET'])
def get_aircraft_status(numav):
    status = Aircraft.get_status(numav)
    aircraft = Aircraft.get_by_id(numav)
    return render_template('aircraft.html', aircraft=aircraft, search_results=None, status=status, nbhddrev=None, datems=None)

@aircraft_routes.route('/aircraft/<int:numav>/nbhddrev', methods=['GET'])
def get_aircraft_nbhddrev(numav):
    nbhddrev = Aircraft.get_nbhddrev(numav)
    aircraft = Aircraft.get_by_id(numav)
    return render_template('aircraft.html', aircraft=aircraft, search_results=None, status=None, nbhddrev=nbhddrev, datems=None)

@aircraft_routes.route('/aircraft/<int:numav>/datems', methods=['GET'])
def get_aircraft_datems(numav):
    datems = Aircraft.get_datems(numav)
    aircraft = Aircraft.get_by_id(numav)
    return render_template('aircraft.html', aircraft=aircraft, search_results=None, status=None, nbhddrev=None, datems=datems)

