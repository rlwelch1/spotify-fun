def get_active_device(sp):
    """
    Returns the ID of the active device.
    """
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            return device['id']
    return None