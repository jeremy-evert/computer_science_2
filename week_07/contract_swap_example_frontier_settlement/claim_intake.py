from abc import ABC, abstractmethod


class ClaimIntake(ABC):
    """Contract: file a new claim into whichever office handles it. Every
    concrete intake must return a confirmation that actually names the
    claimant and the amount -- the caller below depends on that, not on
    which office recorded it."""

    @abstractmethod
    def file_claim(self, claimant: str, gallons_per_day: int) -> str:
        raise NotImplementedError


class WellBoardIntake(ClaimIntake):

    def file_claim(self, claimant: str, gallons_per_day: int) -> str:
        return f"Well Board record: {claimant} claims {gallons_per_day} gal/day"


class TradePostIntake(ClaimIntake):

    def file_claim(self, claimant: str, gallons_per_day: int) -> str:
        return f"Trade Post ledger: {claimant} - {gallons_per_day} gal/day allocation logged"


def register_claim(intake: ClaimIntake, claimant: str, gallons_per_day: int) -> str:
    return intake.file_claim(claimant, gallons_per_day)
