"""
Model architecture and utilities for the RL energy optimizer.
"""

import pickle
import os
import numpy as np
from typing import Any, Dict, Union, Optional


class ModelArchitecture:
    """Define neural network architecture for the RL agent."""
    
    def __init__(self, input_size=10, hidden_layers=None, output_size=8):
        """
        Initialize model architecture.
        
        Args:
            input_size (int): Size of input observation space
            hidden_layers (list): Sizes of hidden layers
            output_size (int): Size of action space
        """
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layers = hidden_layers or [256, 256, 128]
        
        self.architecture = {
            'input_layer': input_size,
            'hidden_layers': self.hidden_layers,
            'output_layer': output_size,
            'activation': 'relu',
            'output_activation': 'softmax'
        }
    
    def get_config(self):
        """Get architecture configuration."""
        return self.architecture
    
    def __repr__(self):
        return f"ModelArchitecture(input={self.input_size}, hidden={self.hidden_layers}, output={self.output_size})"


def load_model(model_path: str) -> Any:
    """
    Load a saved RL model from disk.
    
    Args:
        model_path (str): Path to the saved model
        
    Returns:
        Any: Loaded model object
        
    Raises:
        FileNotFoundError: If model file not found
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    return model


def save_model(model: Any, model_path: str) -> None:
    """
    Save an RL model to disk.
    
    Args:
        model (Any): Model object to save
        model_path (str): Path where model will be saved
    """
    os.makedirs(os.path.dirname(model_path) or '.', exist_ok=True)
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {model_path}")


def get_model_info(model: Any) -> Dict:
    """
    Get information about a loaded model.
    
    Args:
        model (Any): Model object
        
    Returns:
        Dict: Model information
    """
    info = {
        'type': type(model).__name__,
        'size_bytes': pickle_size(model),
        'has_policy': hasattr(model, 'policy'),
        'has_buffer': hasattr(model, 'replay_buffer')
    }
    return info


def pickle_size(obj: Any) -> int:
    """
    Calculate size of object when pickled.
    
    Args:
        obj (Any): Object to measure
        
    Returns:
        int: Size in bytes
    """
    return len(pickle.dumps(obj))


class ModelVersioning:
    """Handle model versioning and checkpointing."""
    
    def __init__(self, model_dir: str = 'models'):
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)
    
    def save_checkpoint(self, model: Any, version: int, metadata: Optional[Dict] = None) -> str:
        """
        Save a model checkpoint with version number.
        
        Args:
            model (Any): Model to save
            version (int): Version number
            metadata (Dict, optional): Additional metadata
            
        Returns:
            str: Path to saved checkpoint
        """
        checkpoint_dir = os.path.join(self.model_dir, f'v{version}')
        os.makedirs(checkpoint_dir, exist_ok=True)
        
        model_path = os.path.join(checkpoint_dir, 'model.pkl')
        save_model(model, model_path)
        
        if metadata:
            import json
            metadata_path = os.path.join(checkpoint_dir, 'metadata.json')
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f)
        
        return model_path
    
    def load_checkpoint(self, version: int) -> Any:
        """
        Load a specific model checkpoint.
        
        Args:
            version (int): Version number
            
        Returns:
            Any: Loaded model
        """
        model_path = os.path.join(self.model_dir, f'v{version}', 'model.pkl')
        return load_model(model_path)
    
    def list_checkpoints(self) -> list:
        """List all available checkpoints."""
        checkpoints = []
        for item in os.listdir(self.model_dir):
            if item.startswith('v') and os.path.isdir(os.path.join(self.model_dir, item)):
                version = int(item[1:])
                checkpoints.append(version)
        return sorted(checkpoints)
