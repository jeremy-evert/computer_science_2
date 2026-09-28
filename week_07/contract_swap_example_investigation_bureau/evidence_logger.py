from abc import ABC, abstractmethod


class EvidenceLogger(ABC):
    """Contract: log an item into whichever record actually receives it.
    Every concrete logger must return a message that names the item id
    and the description -- intake_evidence below depends only on that,
    never on which division wrote it down."""

    @abstractmethod
    def log_intake(self, item_id: str, description: str) -> str:
        raise NotImplementedError


class RecordsDivisionLogger(EvidenceLogger):

    def log_intake(self, item_id: str, description: str) -> str:
        return f"CASE RECORDS: item {item_id} logged - {description}"


class FieldUnitLogger(EvidenceLogger):

    def log_intake(self, item_id: str, description: str) -> str:
        return f"[FIELD REPORT #{item_id}] {description} (pending records review)"


def intake_evidence(logger: EvidenceLogger, item_id: str, description: str) -> str:
    return logger.log_intake(item_id, description)
