from database import DatabaseProvider
from models import StoreModel
from views import AppView
from controllers import AppController

def main():
    # Initialize Database Provider
    db_provider = DatabaseProvider(
        host="localhost", 
        user="root", 
        password="", 
        database="tech_store"
    )

    # Inject DB Provider into the Model
    model = StoreModel(db_provider)

    # Initialize the View
    view = AppView()

    # Inject Model and View into the Controller
    controller = AppController(model, view)

    # Start the application
    controller.run()

if __name__ == "__main__":
    main()