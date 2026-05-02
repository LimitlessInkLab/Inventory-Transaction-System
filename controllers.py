from models import StoreModel
from views import AppView

class AppController:
    """Orchestrates interaction between View and Model."""
    def __init__(self, model: StoreModel, view: AppView):
        self.model = model
        self.view = view

        # Bind view callbacks to controller methods
        self.view.on_refresh = self.refresh_inventory
        self.view.on_transaction = self.process_sale

    def run(self):
        self.refresh_inventory() # Load initial data
        self.view.mainloop()

    def refresh_inventory(self):
        try:
            products = self.model.get_all_products()
            self.view.update_inventory_list(products)
        except Exception as e:
            self.view.show_error(f"Failed to fetch data: {e}")

    def process_sale(self, cust_id: int, prod_id: int, qty: int):
        try:
            result_msg = self.model.process_transaction(cust_id, prod_id, qty)
            self.view.show_message("Transaction Complete", result_msg)
            self.refresh_inventory() # Automatically update UI after sale
        except Exception as e:
            self.view.show_error(str(e))