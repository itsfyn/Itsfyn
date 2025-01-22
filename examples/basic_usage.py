"""
Basic Usage Example
Demonstrates how to use the ItsFyn system.
"""

from src.main import ItsFyn

def main():
    """Example implementation of ItsFyn."""
    # Initialize ItsFyn
    itsfyn = ItsFyn()
    
    try:
        # Start the system
        print("Starting ItsFyn...")
        itsfyn.start()
        
        # Get security status
        status = itsfyn.security_monitor.get_security_status()
        print(f"\nCurrent Security Status:")
        print(f"Status: {status['status']}")
        print(f"Threats Detected: {status['threats_detected']}")
        
        # Generate privacy report
        report = itsfyn.privacy_scanner.generate_privacy_report()
        print(f"\nPrivacy Report:")
        print(f"Generated at: {report['generated_at']}")
        print(f"Overall Score: {report['overall_score']}")
        
        # Generate identity report
        id_report = itsfyn.identity_protection.generate_identity_report()
        print(f"\nIdentity Protection Report:")
        print(f"Timestamp: {id_report['timestamp']}")
        print(f"Exposure Risk: {id_report['exposure_risk']}")
        
        input("\nPress Enter to stop ItsFyn...")
        
    finally:
        # Stop the system
        print("Stopping ItsFyn...")
        itsfyn.stop()
        print("ItsFyn stopped successfully")

if __name__ == "__main__":
    main()
