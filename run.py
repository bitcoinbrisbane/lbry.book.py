from app import init_app
import os

if __name__ == '__main__':
    app = init_app()
    app.run(os.environ['IP_ADDRESS'], port=os.environ['PORT'], debug=os.environ['DEBUG'])