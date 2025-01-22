#!/usr/bin/env python3

"""
ItsFyn - Main Application Entry Point
This is the core file that initializes and runs the ItsFyn privacy and security system.
"""

import logging
from datetime import datetime
from modules.privacy import PrivacyScanner
from modules.security import SecurityMonitor
from modules.identity import IdentityProtection
from utils.logger import setup_logging
from config.settings import load_configuration

class ItsFyn:
    """Main application class for ItsFyn privacy and security system."""
    
    def __init__(self):
        """Initialize the ItsFyn system."""
        # Setup logging
        self.logger = setup_logging()
        self.logger.info("Initializing ItsFyn system...")
        
        # Load configuration
        self.config = load_configuration()
        
        # Initialize core modules
        self.privacy_scanner = PrivacyScanner()
        self.security_monitor = SecurityMonitor()
        self.identity_protection = IdentityProtection()
        
        self.logger.info("ItsFyn system initialized successfully")
    
    def start(self):
        """Start the ItsFyn system and all its components."""
        try:
            self.logger.info("Starting ItsFyn services...")
            
            # Start core services
            self.privacy_scanner.start()
            self.security_monitor.start()
            self.identity_protection.start()
            
            self.logger.info("All services started successfully")
            
        except Exception as e:
            self.logger.error(f"Error starting ItsFyn: {str(e)}")
            raise
    
    def stop(self):
        """Gracefully stop all ItsFyn services."""
        try:
            self.logger.info("Stopping ItsFyn services...")
            
            # Stop core services
            self.privacy_scanner.stop()
            self.security_monitor.stop()
            self.identity_protection.stop()
            
            self.logger.info("All services stopped successfully")
            
        except Exception as e:
            self.logger.error(f"Error stopping ItsFyn: {str(e)}")
            raise

def main():
    """Main entry point for the application."""
    itsfyn = ItsFyn()
    
    try:
        # Start the system
        itsfyn.start()
        
        # Keep the system running
        while True:
            # Main application loop
            pass
            
    except KeyboardInterrupt:
        # Handle graceful shutdown on Ctrl+C
        print("\nShutting down ItsFyn...")
        itsfyn.stop()
    
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        itsfyn.stop()
        raise

if __name__ == "__main__":
    main()
