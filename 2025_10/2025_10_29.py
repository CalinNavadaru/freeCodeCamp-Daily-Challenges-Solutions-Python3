def sort(emails: list[str]) -> list[str]:
    def key(email: str):
        local, domain = email.split("@")
        return domain.lower(), local.lower()
    return sorted(emails, key=key)
