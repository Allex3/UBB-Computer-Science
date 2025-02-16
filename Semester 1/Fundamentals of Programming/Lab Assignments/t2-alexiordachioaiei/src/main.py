from src.services import Services
from src.ui import ApplicationUI
from src.repository import TextRepo

if __name__ == '__main__':
    text_repo = TextRepo()
    services = Services(text_repo)
    app = ApplicationUI(services)
    app.run()