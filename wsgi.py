"""
WSGI wrapper for Render deployment.
This allows Render to find the app object easily.
"""

from agentic_trust_dashboard import app

# Export app as the WSGI application object
# This is what gunicorn looks for when you specify wsgi:app
__all__ = ['app']
