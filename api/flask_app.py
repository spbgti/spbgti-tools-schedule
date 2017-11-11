from datetime import datetime

from flask import Flask, request, jsonify
from main.views import get_pairs_query_by_date, get_pairs_query_for_a_week, fill_pairs

app = Flask(__name__)


FILLPAIRS_KEYS = {'group_number', 'pair_name', 'pair_duration', 'pair_start_date', 'days', 'pair_end_date'}


@app.route('/api/getPairsByDate')
def get_pairs_by_date():
    """Route to get all pairs by date
    ;arg group_number: number of group
    ;arg date: date in format %Y-%m-%d"""
    response = {'pairs': []}
    group_number = request.args.get('group_number')
    date = request.args.get('date')
    date = datetime.strptime(date, '%Y-%m-%d')
    pairs_query = get_pairs_query_by_date(group_number, date)
    if pairs_query:
        for pair in pairs_query:
            response['pairs'].append(pair.to_dict())
    return jsonify(response)


@app.route('/api/getPairsForWeek')
def get_pairs_for_a_week():
    """Route to get all pairs for a week
    ;arg group_number: number of group
    ;arg date: date in format %Y-%m-%d"""
    response = {'pairs': []}
    group_number = request.args.get('group_number')
    date = request.args.get('date')
    date = datetime.strptime(date, '%Y-%m-%d')
    pairs_query = get_pairs_query_for_a_week(group_number, date)
    if pairs_query:
        for pair in pairs_query:
            response['pairs'].append(pair.to_dict())
    return jsonify(response)


@app.route('/api/fillPairs', methods=['POST'])
def fill_pairs():
    """Route to fill pairs"""
    pair_data = request.get_json(silent=True)
    # Keys validation
    current_keys = set(pair_data.keys())
    current_keys.add('pair_end_date')  # Optional argument

    if current_keys == FILLPAIRS_KEYS:
        status = fill_pairs(**pair_data)
        if status:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})
