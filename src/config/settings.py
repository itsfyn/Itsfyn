"""
Settings Configuration
Manages application configuration and settings.
"""

import json
from pathlib import Path

DEFAULT_CONFIG = {
    'privacy': {
        'scan_interval': 3600,  # seconds
        'risk_threshold': 'medium',
        'notify_on_exposure': True
    },
    'security': {
        'monitor_interval': 300,  # seconds
        'threat_sensitivity': 'high',
        'auto_block_threats': True
    },
    'identity': {
        'check_interval': 86400,  # seconds
        'monitor_social_media': True,
        'dark_web_monitoring': True
    },
    'system': {
        'log_level': 'INFO',
        'max_log_size': 1048576,  # 1MB
        'backup_count': 5
    }
}

def load_configuration():
    """Load configuration from file or create default."""
    config_file = Path('config/config.json')
    
    if config_file.exists():
        with config_file.open('r') as f:
            return json.load(f)
    
    # Create default configuration
    config_file.parent.mkdir(exist_ok=True)
    with config_file.open('w') as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    
    return DEFAULT_CONFIG

def save_configuration(config):
    """Save configuration to file."""
    config_file = Path('config/config.json')
    with config_file.open('w') as f:
        json.dump(config, f, indent=4)
