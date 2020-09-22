from app import app
from app.main.config.settings import Config
app.config.from_object(Config)
if __name__ == "__main__":
    app.run(debug=False)