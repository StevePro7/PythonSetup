def apply_deadzone(value, deadzone=0.15, inv_range=None):
    """
    Apply deadzone + rescale to full range.

    value: raw axis value (-1.0 to 1.0)
    deadzone: size of deadzone (0.1–0.2 typical)
    inv_range: precomputed 1 / (1 - deadzone)
    """

    if abs(value) < deadzone:
        return 0.0

    if inv_range is None:
        inv_range = 1.0 / (1.0 - deadzone)

    # Normalize while preserving sign
    if value > 0:
        return (value - deadzone) * inv_range
    else:
        return (value + deadzone) * inv_range