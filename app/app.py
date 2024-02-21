from app import create_app

if __name__ == '__main__':
    app = create_app("prd")
    app.run(host='0.0.0')