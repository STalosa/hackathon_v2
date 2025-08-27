"""
S-5 Contested Logistics Tool
Simulates logistics scenarios under contested conditions.
"""

from typing import Dict
from agents import function_tool
from .monitoring import monitor_tool

@function_tool(strict_mode=False)
@monitor_tool('s5_contested_logistics', 'S-5')
def s5_contested_logistics(unit: str, scenario_type: str) -> Dict:
    """Simulate contested logistics scenario for a unit.
    scenario_type: e.g., 'logistics', 'operations', 'intelligence', etc.
    """
    scenarios = {
        "counter-intel": "Enemy has intercepted supply routes. Increased risk of ambush.",
        "intelligence_failure": "Supply convoy rerouted due to faulty threat assessment.",
        "sabotage": "Critical supplies destroyed by insider threat.",
        "supply_interdiction": "Aerial resupply blocked by enemy air defense.",
        "cyber_attack": "Logistics tracking systems compromised.",
        "natural_disaster": "Flooding has made primary supply routes impassable.",
        "political_unrest": "Local population hostility delaying supply convoys.",
        "infrastructure_failure": "Bridge collapse on main supply route.",
        "weather_event": "Severe weather delaying air and ground resupply.",
        "enemy_activity": "Increased enemy patrols causing supply delays.",
        "resource_scarcity": "Fuel shortages impacting vehicle availability.",
        "communication_blackout": "Loss of comms hindering coordination of logistics.",
        "mechanical_failure": "Vehicle breakdowns reducing convoy effectiveness.",
        "terrain_challenge": "Difficult terrain slowing down supply deliveries.",
        "loss_of_personnel": "Key logistics personnel unavailable due to illness.",
        "equipment_shortage": "Lack of necessary equipment for supply handling.",
        "security_breach": "Convoy security compromised leading to supply losses.",
        "logistical_error": "Mismanagement leading to supply misallocation.",
        "enemy_infiltration": "Enemy agents within unit disrupting logistics.",
        "allied_miscommunication": "Allied forces miscommunicating supply needs.",
        "unexpected_demand": "Sudden increase in supply needs due to operational changes.",
        "transportation_delay": "Delays in transportation assets affecting supply timelines.",
        "fuel_shortage": "Fuel supplies critically low, impacting vehicle operations.",
        "medical_emergency": "Medical emergencies diverting supplies from primary needs.",
        "evacuation": "Emergency evacuation disrupting normal supply chains.",
        "training_exercise": "Training exercises consuming unexpected supply resources.",
        "cybersecurity_breach": "Cyber breach causing delays in logistics software systems.",
        "intelligence_lapse": "Failure in intelligence leading to supply route ambushes.",
        "enemy_sabotage": "Enemy sabotage causing significant life losses.",
    }
    result = scenarios.get(scenario_type, "Unknown scenario. Minimal impact.")
    return {
        "unit": unit,
        "scenario_type": scenario_type,
        "impact": result,
        "recommendation": "Review alternate supply routes and increase convoy security."
    }