from flask import Flask
import os
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    hostname = os.environ.get('HOSTNAME', 'unknown')
    visits = redis_client.incr('visits')
    return f'''
    <h1>¡Hola desde Docker!</h1>
    <p>Container ID: {hostname}</p>
    <p>Visitas: {visits}</p>
    <p>Esta aplicación está corriendo en un contenedor Docker 🐳</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

