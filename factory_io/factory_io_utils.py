"""
Factory I/O scene and Modbus configuration utilities.
"""

import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional


def load_scene(scene_path: str) -> Dict[str, Any]:
    """
    Load and parse a Factory I/O scene file.
    
    Args:
        scene_path (str): Path to the scene file
        
    Returns:
        Dict: Scene configuration data
    """
    try:
        # Try XML format first
        tree = ET.parse(scene_path)
        root = tree.getroot()
        
        scene_data = {
            'format': 'xml',
            'root_tag': root.tag,
            'attributes': root.attrib,
            'components': []
        }
        
        # Extract components
        for element in root.findall('.//Component'):
            component = {
                'name': element.get('name'),
                'type': element.get('type'),
                'properties': element.attrib
            }
            scene_data['components'].append(component)
        
        return scene_data
        
    except ET.ParseError:
        # Try JSON format
        try:
            with open(scene_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Unable to parse scene file: {scene_path}")


def parse_modbus_config(config_path: str) -> Dict[str, Any]:
    """
    Parse Modbus configuration file.
    
    Args:
        config_path (str): Path to the Modbus configuration
        
    Returns:
        Dict: Modbus configuration
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Validate configuration
    required_keys = ['slave_id', 'registers']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")
    
    return config


def map_modbus_to_observation(modbus_data: Dict, register_map: Dict) -> Dict:
    """
    Map Modbus register values to environment observations.
    
    Args:
        modbus_data (Dict): Raw Modbus register values
        register_map (Dict): Mapping configuration
        
    Returns:
        Dict: Mapped observation values
    """
    observations = {}
    
    for obs_name, register_config in register_map.items():
        register_id = register_config.get('register')
        conversion = register_config.get('conversion', 1.0)
        offset = register_config.get('offset', 0)
        
        if register_id in modbus_data:
            value = modbus_data[register_id]
            observations[obs_name] = value * conversion + offset
    
    return observations


def map_action_to_modbus(action: int, action_map: Dict) -> Dict:
    """
    Map RL agent action to Modbus register writes.
    
    Args:
        action (int): Action from the RL agent (0-7)
        action_map (Dict): Mapping configuration
        
    Returns:
        Dict: Modbus register writes
    """
    writes = {}
    
    action_config = action_map.get(action, {})
    for register_id, value in action_config.items():
        writes[int(register_id)] = value
    
    return writes


class ModbusSimulator:
    """Simulate Modbus communication for testing."""
    
    def __init__(self, slave_id: int = 1):
        self.slave_id = slave_id
        self.registers = {}
    
    def read_register(self, address: int) -> int:
        """Read a register value."""
        return self.registers.get(address, 0)
    
    def write_register(self, address: int, value: int) -> bool:
        """Write to a register."""
        self.registers[address] = value
        return True
    
    def read_coil(self, address: int) -> bool:
        """Read a coil value."""
        return self.registers.get(address, False)
    
    def write_coil(self, address: int, value: bool) -> bool:
        """Write to a coil."""
        self.registers[address] = value
        return True
    
    def update_state(self, new_values: Dict[int, int]) -> None:
        """Update multiple register values."""
        self.registers.update(new_values)


class SceneComponent:
    """Represent a component in the Factory I/O scene."""
    
    def __init__(self, name: str, component_type: str, **properties):
        self.name = name
        self.type = component_type
        self.properties = properties
        self.state = {}
    
    def update(self, **kwargs) -> None:
        """Update component state."""
        self.state.update(kwargs)
    
    def __repr__(self):
        return f"SceneComponent({self.name}, {self.type})"
