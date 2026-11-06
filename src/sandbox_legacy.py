# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 The Linux Foundation

"""Deliberate findings for the findings-ratchet sandbox (not real code)."""


def to_int(value):
    """Parse an integer."""
    try:
        return int(value)
    except:
        return None


def to_float(value):
    """Parse a float."""
    try:
        return float(value)
    except:
        return None
