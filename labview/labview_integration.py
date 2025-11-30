"""
LabVIEW data exchange utilities for integrating AI optimization with LabVIEW systems.
"""

import json
import csv
from typing import Dict, Any, List, Optional
from datetime import datetime
import os


def export_for_labview(data: Dict[str, Any], output_path: str, format: str = 'json') -> None:
    """
    Export data in a format compatible with LabVIEW.
    
    Args:
        data (Dict): Data to export
        output_path (str): Output file path
        format (str): Export format ('json' or 'csv')
    """
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    if format == 'json':
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    elif format == 'csv':
        # Flatten dictionary for CSV export
        flat_data = _flatten_dict(data)
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=flat_data.keys())
            writer.writeheader()
            writer.writerow(flat_data)
    
    print(f"Data exported to {output_path}")


def import_from_labview(input_path: str) -> Dict[str, Any]:
    """
    Import data from LabVIEW.
    
    Args:
        input_path (str): Input file path
        
    Returns:
        Dict: Imported data
    """
    if input_path.endswith('.json'):
        with open(input_path, 'r') as f:
            return json.load(f)
    
    elif input_path.endswith('.csv'):
        with open(input_path, 'r') as f:
            reader = csv.DictReader(f)
            return next(reader)
    
    else:
        raise ValueError(f"Unsupported file format: {input_path}")


def _flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flatten nested dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(_flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


class LabVIEWDataHandler:
    """Handle data exchange with LabVIEW systems."""
    
    def __init__(self, data_dir: str = 'labview/ai_integration_examples'):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
    def prepare_ai_decision(self, action: int, confidence: float, 
                           power_savings: float, metadata: Optional[Dict] = None) -> Dict:
        """
        Prepare AI decision payload for LabVIEW.
        
        Args:
            action (int): Action selected by AI
            confidence (float): Confidence score (0-1)
            power_savings (float): Estimated power savings
            metadata (Dict, optional): Additional metadata
            
        Returns:
            Dict: Formatted payload
        """
        payload = {
            'timestamp': datetime.now().isoformat(),
            'ai_decision': {
                'action': int(action),
                'confidence': float(confidence),
                'power_savings_kw': float(power_savings)
            },
            'metadata': metadata or {}
        }
        return payload
    
    def prepare_system_status(self, power_data: Dict, efficiency: float, 
                             throughput: float) -> Dict:
        """
        Prepare system status for export to LabVIEW.
        
        Args:
            power_data (Dict): Power consumption data
            efficiency (float): System efficiency
            throughput (float): System throughput
            
        Returns:
            Dict: Status payload
        """
        return {
            'timestamp': datetime.now().isoformat(),
            'system_status': {
                'power': power_data,
                'efficiency': efficiency,
                'throughput': throughput
            }
        }
    
    def save_ai_decision(self, decision: Dict, filename: Optional[str] = None) -> str:
        """Save AI decision to file."""
        if not filename:
            filename = f"ai_decision_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        filepath = os.path.join(self.data_dir, filename)
        export_for_labview(decision, filepath, format='json')
        return filepath
    
    def save_status_report(self, status: Dict, filename: Optional[str] = None) -> str:
        """Save system status to file."""
        if not filename:
            filename = f"status_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        filepath = os.path.join(self.data_dir, filename)
        export_for_labview(status, filepath, format='json')
        return filepath


def create_labview_handshake_payload(status: str, timestamp: Optional[str] = None) -> Dict:
    """
    Create a handshake payload for LabVIEW communication.
    
    Args:
        status (str): Status message
        timestamp (str, optional): Custom timestamp
        
    Returns:
        Dict: Handshake payload
    """
    return {
        'handshake': {
            'status': status,
            'timestamp': timestamp or datetime.now().isoformat(),
            'version': '1.0',
            'protocol': 'TCP_JSON'
        }
    }
