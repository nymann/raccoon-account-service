from raccoon_account_service.core.config import Config


class ServiceContainer:
    def __init__(self, config: Config) -> None:
        self.config = config
