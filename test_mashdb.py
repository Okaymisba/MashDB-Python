#!/usr/bin/env python3
"""
Test script for MashDB Python interface.
"""

from mashdb import query

def test_queries():
    """Test basic queries with MashDB."""
    try:
        # Test a simple query
        print("Testing simple query...")
        result = query("SELECT * FROM Users;", as_json=True)
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_queries()
