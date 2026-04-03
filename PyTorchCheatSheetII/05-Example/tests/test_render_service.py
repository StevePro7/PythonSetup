# tests/test_render_service.py
import numpy as np
from unittest.mock import MagicMock
from app.services.render_service import RenderService


def test_render_calls_renderer():
    service = RenderService(device="cpu")

    # Mock renderer
    mock_renderer = MagicMock()
    fake_tensor = MagicMock()

    # Simulate torch tensor chain:
    # renderer(mesh)[0].detach().cpu().numpy()
    fake_tensor.__getitem__.return_value = fake_tensor
    fake_tensor.detach.return_value.cpu.return_value.numpy.return_value = np.ones((128, 128, 3))

    mock_renderer.return_value = fake_tensor
    service.renderer = mock_renderer

    mesh = MagicMock()

    result = service.render(mesh)

    assert result.shape == (128, 128, 3)
    mock_renderer.assert_called_once_with(mesh)
