
from __future__ import annotations  # ✅ allows using | in type hints even in Python <3.10

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get values from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase() -> Client:
    """
    Returns a Supabase client instance using credentials from .env.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase credentials are missing. Check your .env file.")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

