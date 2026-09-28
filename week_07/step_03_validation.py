"""Step 3: small validation helpers used by the stateful objects."""

def normalize_item_name(item_name: str) -> str:
    """
    Normalize an item name for inventory lookups.
    """

    return item_name.strip().lower()


def validate_object_name(name: str, object_description: str) -> str:
    """
    Validate and normalize the name of a domain object.
    """

    if not isinstance(name, str):
        raise TypeError(f"{object_description} name must be a string.")

    normalized_name = name.strip()

    if not normalized_name:
        raise ValueError(
            f"{object_description} name must not be empty."
        )

    return normalized_name


def validate_item_name(item_name: str) -> str:
    """
    Validate and normalize an inventory item name.
    """

    if not isinstance(item_name, str):
        raise TypeError("Item name must be a string.")

    normalized_item = normalize_item_name(item_name)

    if not normalized_item:
        raise ValueError("Item name must not be empty.")

    return normalized_item


def validate_positive_quantity(quantity: int) -> int:
    """
    Require a positive integer quantity.

    Boolean values are rejected because bool is technically a subclass of int
    in Python, but True and False are not sensible supply quantities here.
    """

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_inventory(inventory: dict[str, int]) -> dict[str, int]:
    """
    Validate inventory and return a normalized copy.
    """

    if not isinstance(inventory, dict):
        raise TypeError("Inventory must be provided as a dictionary.")

    validated_inventory: dict[str, int] = {}

    for item_name, quantity in inventory.items():
        normalized_item = validate_item_name(item_name)

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(
                f"Inventory quantity for {normalized_item} "
                "must be an integer."
            )

        if quantity < 0:
            raise ValueError(
                f"Inventory quantity for {normalized_item} "
                "cannot be negative."
            )

        validated_inventory[normalized_item] = quantity

    return validated_inventory


# ============================================================
# FIRST CONFORMING COLLABORATOR
# ============================================================

