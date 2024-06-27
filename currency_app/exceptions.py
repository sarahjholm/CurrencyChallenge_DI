
class ValidationError(Exception):
    status_code = 400
    def __init__(self, reasons: str):
        super(ValidationError, self).__init__()
        self.reasons = reasons

    def serialize(self) -> str:
        return self.reasons

class APICommunicationError(Exception):
    status_code = 400
    def __init__(self, reasons: str):
        super(APICommunicationError, self).__init__()
        self.reasons = reasons

    def serialize(self) -> str:
        return self.reasons