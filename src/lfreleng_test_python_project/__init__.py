# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation

"""Sample/test module."""

try:
    from lfreleng_test_python_project._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["__version__"]
