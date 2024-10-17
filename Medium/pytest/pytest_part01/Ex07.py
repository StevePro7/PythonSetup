from unittest.mock import Mock


def test_widget_activator() -> None:
    dummy_widget_loader = None
    mock_widget_publisher = Mock()
    widget_activator = WidgetActivator(dummy_widget_loader, mock_widget_publisher)
    # Test the activator using the dummy widget loader