"""
Privacy Scanner Tests
Unit tests for the privacy scanner module.
"""

import unittest
from datetime import datetime
from src.modules.privacy import PrivacyScanner

class TestPrivacyScanner(unittest.TestCase):
    """Test cases for PrivacyScanner class."""
    
    def setUp(self):
        """Set up test cases."""
        self.scanner = PrivacyScanner()
    
    def test_initialization(self):
        """Test scanner initialization."""
        self.assertFalse(self.scanner.is_running)
        self.assertIsNone(self.scanner.scan_thread)
    
    def test_start_stop(self):
        """Test starting and stopping the scanner."""
        self.scanner.start()
        self.assertTrue(self.scanner.is_running)
        self.assertIsNotNone(self.scanner.scan_thread)
        
        self.scanner.stop()
        self.assertFalse(self.scanner.is_running)
    
    def test_privacy_report(self):
        """Test privacy report generation."""
        report = self.scanner.generate_privacy_report()
        self.assertIsInstance(report, dict)
        self.assertIn('generated_at', report)
        self.assertIn('overall_score', report)
        self.assertIn('findings', report)

if __name__ == '__main__':
    unittest.main()
