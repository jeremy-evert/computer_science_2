from abc import ABC, abstractmethod


class SubsystemReporter(ABC):
    """Contract: report a subsystem's status into the ship's log. Every
    concrete reporter must return a message that names the subsystem --
    log_subsystem_status below depends only on that, never on which
    generation of hardware produced the reading."""

    @abstractmethod
    def report_status(self, subsystem_name: str) -> str:
        raise NotImplementedError


class LegacySensorArray(SubsystemReporter):

    def report_status(self, subsystem_name: str) -> str:
        return f"LOG :: {subsystem_name} :: NOMINAL"


class NextGenSensorArray(SubsystemReporter):

    def report_status(self, subsystem_name: str) -> str:
        return f"{{'subsystem': '{subsystem_name}', 'status': 'nominal'}}"


def log_subsystem_status(reporter: SubsystemReporter, subsystem_name: str) -> str:
    return reporter.report_status(subsystem_name)
