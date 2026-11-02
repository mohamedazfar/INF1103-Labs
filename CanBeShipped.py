from abc import ABC, abstractmethod

# CanBeShipped Abstract Base Class (Interface)
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass