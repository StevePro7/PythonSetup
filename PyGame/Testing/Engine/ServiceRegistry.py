class ServiceRegistry:
    _services: dict = {}

    @classmethod
    def register(cls, name: str, service):
        cls._services[name] = service

    @classmethod
    def get(cls, name: str):
        return cls._services[name]

    @classmethod
    def clear(cls):
        cls._services.clear()
