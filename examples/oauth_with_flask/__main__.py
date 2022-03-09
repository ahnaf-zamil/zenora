from .app import app
from .config import PORT

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
