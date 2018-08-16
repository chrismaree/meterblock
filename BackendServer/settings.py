import os

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://142.93.131.22:27017/') 

RESOURCE_METHODS = ['GET', 'POST']

MONGO_DBNAME = 'meterBlockReadings'


DOMAIN = {
    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
        }
    }
}