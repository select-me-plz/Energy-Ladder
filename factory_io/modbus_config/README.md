# Factory I/O Modbus Configuration

## Register Mapping

This file defines the Modbus register mapping for Factory I/O components.

```json
{
  "slave_id": 1,
  "registers": {
    "conveyor_power": {
      "register": 100,
      "type": "holding",
      "size": 1,
      "conversion": 0.1,
      "offset": 0,
      "description": "Total conveyor power consumption (kW)"
    },
    "pusher_power": {
      "register": 101,
      "type": "holding",
      "size": 1,
      "conversion": 0.1,
      "offset": 0,
      "description": "Total pusher power consumption (kW)"
    },
    "robot_power": {
      "register": 102,
      "type": "holding",
      "size": 1,
      "conversion": 0.1,
      "offset": 0,
      "description": "Total robot power consumption (kW)"
    },
    "total_power": {
      "register": 103,
      "type": "holding",
      "size": 1,
      "conversion": 0.1,
      "offset": 0,
      "description": "Total factory power consumption (kW)"
    },
    "conveyor_load": {
      "register": 104,
      "type": "holding",
      "size": 1,
      "conversion": 0.01,
      "offset": 0,
      "description": "Conveyor load percentage (0-100%)"
    },
    "pusher_load": {
      "register": 105,
      "type": "holding",
      "size": 1,
      "conversion": 0.01,
      "offset": 0,
      "description": "Pusher load percentage (0-100%)"
    },
    "robot_load": {
      "register": 106,
      "type": "holding",
      "size": 1,
      "conversion": 0.01,
      "offset": 0,
      "description": "Robot load percentage (0-100%)"
    },
    "system_efficiency": {
      "register": 107,
      "type": "holding",
      "size": 1,
      "conversion": 0.01,
      "offset": 0,
      "description": "System efficiency percentage (0-100%)"
    },
    "total_energy": {
      "register": 108,
      "type": "holding",
      "size": 2,
      "conversion": 0.01,
      "offset": 0,
      "description": "Total energy consumed (kWh)"
    },
    "ai_decision": {
      "register": 200,
      "type": "holding",
      "size": 1,
      "conversion": 1,
      "offset": 0,
      "description": "AI decision (0-7 representing different actions)"
    },
    "ai_confidence": {
      "register": 201,
      "type": "holding",
      "size": 1,
      "conversion": 0.01,
      "offset": 0,
      "description": "AI decision confidence (0-100%)"
    }
  }
}
```

## Communication Protocol

- **Protocol**: Modbus TCP
- **Port**: 502 (default)
- **Slave ID**: 1
- **Polling Interval**: 100ms (recommended)

## Implementation Example

```python
from factory_io.factory_io_utils import parse_modbus_config, ModbusSimulator

config = parse_modbus_config('factory_io/modbus_config/config.json')
modbus = ModbusSimulator(slave_id=1)

# Read power values
conveyor_power = modbus.read_register(100)
pusher_power = modbus.read_register(101)
robot_power = modbus.read_register(102)

# Write AI decision
modbus.write_register(200, 5)  # Action 5
modbus.write_register(201, 92) # 92% confidence
```
