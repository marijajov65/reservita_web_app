from application import init_app
from config import Config

app = init_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT)
