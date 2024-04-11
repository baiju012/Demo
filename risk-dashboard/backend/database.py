from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['risk_db']
collection = db['risks']

def get_risks_data(filters=None):
    query = {}
    if filters:
        if 'end_year' in filters:
            query['published'] = {'$regex': f'.*{filters["end_year"]}.*'}
        if 'topics' in filters:
            query['topic'] = {'$in': filters['topics']}
        if 'sector' in filters:
            query['sector'] = {'$in': filters['sector']}
        if 'region' in filters:
            query['region'] = {'$in': filters['region']}
        if 'pest' in filters:
            query['pestle'] = {'$in': filters['pest']}
        if 'source' in filters:
            query['source'] = {'$in': filters['source']}
        if 'swot' in filters:
            query['swot'] = {'$in': filters['swot']}
        if 'country' in filters:
            query['country'] = {'$in': filters['country']}
        if 'city' in filters:
            query['city'] = {'$in': filters['city']}
    risks = collection.find(query)
    return list(risks)
