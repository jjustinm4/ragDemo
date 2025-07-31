"""
Author: Justin M
Date: 2025-07-23

File: config.py
Description: Stores constants and paths.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
VECTOR_STORE_DIR = os.path.join(BASE_DIR, "vector_store")

EMBEDDING_DIM = 1536  # OpenAI ada-002
