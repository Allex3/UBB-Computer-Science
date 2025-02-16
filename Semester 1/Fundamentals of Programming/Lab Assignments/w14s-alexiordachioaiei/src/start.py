from src.ui import Application
from src.services import Services
from src.repository import FlightsRepo

if __name__ == '__main__':
    repository = FlightsRepo("flights.txt")
    services = Services(repository)
    app = Application(services)
    app.run()