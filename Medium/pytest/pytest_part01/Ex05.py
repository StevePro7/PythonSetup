from unittest.mock import MaigcMock


def test_inventory_manager() -> None:
    stub_inventory_repository = MagicMock()
    stub_inventory_repository.get_items.return_value = [
        InventoryItem(sku=123, name="Banana", stock_count=10),
        InventoryItem(sku=456, name="Potato", stock_count=2)
    ]
    inventory_manager = InventoryManager(stub_inventory_repository)
    assert inventory_manager.total_stock_count() == 17