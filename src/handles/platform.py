class Platform:
    def is_available(self, username: str) -> bool:
        raise NotImplementedError

    def are_available(self, usernames: list[str]) -> list:
        return list(filter(self.is_available, usernames))
