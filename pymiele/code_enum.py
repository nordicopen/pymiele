"""Enum class for Miele intergration."""

from enum import IntEnum
import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)
completed_warnings: set[str] = set()


class MieleEnum(IntEnum):
    """Miele Enum for codes with int values."""

    # Modify the behaviour of the class when detecting a missing value:
    # Set argument missing_to_none= True when creating the subclass in order to:
    # - Log a warning that the code is missing
    # - Return None as key name
    #
    # Deprecated variant - can be removed 2025.12
    # Add a member unknown_code in order to:
    # - Log a warning that the code is missing
    # - Return 'unknown_value' as key name

    def __init_subclass__(
        cls, /, missing_to_none: bool = False, **kwargs: dict[str, Any]
    ) -> None:
        """Add default member when setting up the subclass."""
        super().__init_subclass__(**kwargs)
        if missing_to_none:
            self = int.__new__(cls)
            self._name_ = None  # pylint: disable=W0201
            self._value_ = -9999  # A dummy code value
            cls._add_member_("missing_to_none", self)

    @property
    def name(self) -> str | None:  # pylint: disable=E0102, W0236
        """Force to lower case."""
        _name = super().name.lower() if super().name is not None else None
        return _name if _name != "missing_to_none" else None

    @classmethod
    def _missing_(cls, value: object) -> Any | None:
        """Handle missing enum values."""
        if hasattr(cls, "unknown_code") or hasattr(cls, "unknown"):
            warning = (
                f"Missing {cls.__name__} code: {value} - defaulting to 'unknown_code'"
            )
            if warning not in completed_warnings:
                completed_warnings.add(warning)
                _LOGGER.warning(warning)
            return cls.unknown_code  # pylint: disable=no-member

        if hasattr(cls, "missing_to_none"):
            if value is not None:
                warning = (
                    f"Missing {cls.__name__} code: {value} - defaulting to Unknown"
                )
                if warning not in completed_warnings:
                    completed_warnings.add(warning)
                    _LOGGER.warning(warning)
            return cls.missing_to_none  # pylint: disable=no-member

        return None

    def __new__(cls, value: int, *values: list[int]) -> Any:
        """Allow duplicate values."""
        self = int.__new__(cls)
        self._value_ = value
        for v in values:
            self._add_value_alias_(v)
        return self

    @classmethod
    def as_dict(cls) -> dict[str, int]:
        """Return a dict of enum names and values."""
        return {i.name: i.value for i in cls if i.name is not None}

    @classmethod
    def as_enum_dict(cls) -> dict[int, Any]:
        """Return a dict of enum values and enum names."""
        return {i.value: i for i in cls if i.name is not None}

    @classmethod
    def values(cls) -> list[int]:
        """Return a list of enum values."""
        return list(cls.as_dict().values())

    @classmethod
    def keys(cls) -> list[str]:
        """Return a list of enum names."""
        return list(cls.as_dict().keys())

    @classmethod
    def items(cls) -> Any:
        """Return a list of enum items."""
        return cls.as_dict().items()
