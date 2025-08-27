"""
S-5 Contested Logistics Tool
Simulates logistics scenarios under contested conditions, grouped by sector of influence.
"""

import random
from typing import Dict, Optional
from agents import function_tool
from .monitoring import monitor_tool

@function_tool(strict_mode=False)
@monitor_tool('s5_contested_logistics', 'S-5')
def s5_contested_logistics(
    unit: str,
    sector: str = "logistics",
    scenario_type: Optional[str] = None
) -> Dict:
    """
    Simulate contested logistics scenario for a unit.
    sector: 'intelligence', 'operations', or 'logistics'
    scenario_type: optional, if provided will use that scenario, otherwise pick randomly from sector
    """
    scenarios_by_sector = {
        "intelligence": [
            ("counter-intel", "Enemy has intercepted supply routes. Increased risk of ambush."),
            ("intelligence_failure", "Supply convoy rerouted due to faulty threat assessment."),
            ("intelligence_lapse", "Failure in intelligence leading to supply route ambushes."),
            ("enemy_infiltration", "Enemy agents within unit disrupting logistics."),
            ("security_breach", "Convoy security compromised leading to supply losses."),
            ("false_flag", "Enemy uses false flag operations to mislead logistics movements."),
            ("signal_jamming", "Enemy jamming disrupts intelligence gathering on supply routes."),
            ("decoy_convoy", "Enemy deploys decoy convoys to mislead surveillance."),
            ("satellite_blackout", "Loss of satellite imagery over supply corridor."),
            ("spoofed_orders", "Fake orders issued to reroute supplies."),
            ("traitor_tipoff", "Insider tips enemy to convoy departure times."),
            ("misidentified_unit", "Friendly unit misidentified as hostile, delaying supplies."),
            ("leaked_manifest", "Supply manifest leaked, enemy targets high-value items."),
            ("intercepted_comms", "Enemy intercepts radio traffic, predicts supply movements."),
            ("compromised_agent", "Intelligence agent compromised, reveals supply plans."),
            ("map_tampering", "Enemy alters digital maps, causing navigation errors."),
            ("drone_surveillance", "Enemy drones track supply convoys."),
            ("cyber_espionage", "Enemy hacks into logistics planning software."),
            ("planted_evidence", "Enemy plants false evidence of route safety."),
            ("misleading_reports", "Enemy spreads false reports of road conditions."),
            ("forged_documents", "Fake supply documents cause confusion at checkpoints."),
            ("double_agent", "Double agent provides conflicting supply route info."),
            ("sensor_spoofing", "Enemy spoofs ground sensors to mask ambushes."),
            ("intel_overload", "Flood of false intelligence overwhelms analysts."),
            ("missing_recon", "Recon team fails to report, supply route status unknown."),
            ("enemy_psyops", "Enemy psychological ops lower convoy morale."),
            ("disinformation_campaign", "Enemy spreads rumors of contaminated supplies."),
            ("lost_surveillance_asset", "Surveillance drone lost over supply area."),
            ("encrypted_traffic", "Enemy switches to encrypted comms, masking intentions."),
            ("unverified_tip", "Unverified tip causes unnecessary reroute."),
            ("friendly_spy", "Ally's intelligence gathering disrupts own logistics."),
            ("enemy_listening_post", "Enemy listening post discovered near supply route."),
            ("compromised_checkpoint", "Checkpoint staff bribed to allow enemy access."),
            ("intel_blackout", "No intelligence updates for 48 hours."),
            ("enemy_decoy", "Enemy sets up fake supply drop to lure convoy."),
            ("misplaced_trust", "Trusted local guide turns out to be enemy collaborator."),
            ("forged_clearance", "Enemy uses forged clearance to access supply depot."),
            ("enemy_human_terrain", "Enemy blends with civilians to observe logistics."),
            ("unreliable_source", "Key intelligence source proven unreliable."),
            ("enemy_signal_intel", "Enemy uses signal intelligence to track convoys."),
            ("compromised_network", "Intelligence network compromised, all plans exposed."),
            ("enemy_propaganda", "Enemy claims supply convoy destroyed (untrue)."),
            ("intel_lag", "Intelligence updates lag behind real-time events."),
            ("enemy_roadblocks", "Enemy sets up fake roadblocks based on intel."),
            ("friendly_fire_warning", "False report of enemy presence delays convoy."),
            ("enemy_misinformation", "Enemy spreads misinformation about supply schedules."),
            ("lost_contact", "Lost contact with forward intelligence team."),
            ("enemy_surveillance", "Enemy maintains persistent surveillance on supply hub."),
            ("intel_confusion", "Conflicting intelligence reports on enemy activity."),
            ("enemy_deception", "Enemy uses deception to mask true intentions."),
        ],
        "operations": [
            ("sabotage", "Critical supplies destroyed by insider threat."),
            ("enemy_activity", "Increased enemy patrols causing supply delays."),
            ("supply_interdiction", "Aerial resupply blocked by enemy air defense."),
            ("evacuation", "Emergency evacuation disrupting normal supply chains."),
            ("training_exercise", "Training exercises consuming unexpected supply resources."),
            ("unexpected_demand", "Sudden increase in supply needs due to operational changes."),
            ("medical_emergency", "Medical emergencies diverting supplies from primary needs."),
            ("enemy_sabotage", "Enemy sabotage causing significant life losses."),
            ("roadside_bomb", "Improvised explosive device damages convoy."),
            ("bridge_demolition", "Key bridge destroyed, rerouting required."),
            ("convoy_ambush", "Enemy ambushes supply convoy."),
            ("vehicle_breakdown", "Multiple vehicles break down en route."),
            ("route_blocked", "Main supply route blocked by debris."),
            ("hostage_situation", "Convoy crew taken hostage."),
            ("fuel_dump_fire", "Fuel dump catches fire, reducing reserves."),
            ("supply_drop_missed", "Airdropped supplies land outside safe zone."),
            ("friendly_fire", "Supply convoy mistakenly targeted by friendly forces."),
            ("riot", "Local unrest blocks supply movement."),
            ("checkpoint_delay", "Delays at checkpoints due to paperwork issues."),
            ("weather_delay", "Severe weather halts convoy movement."),
            ("lost_convoy", "Convoy gets lost due to poor navigation."),
            ("minefield", "Undetected minefield damages vehicles."),
            ("airstrike", "Enemy airstrike damages supply depot."),
            ("sniper_threat", "Sniper activity delays unloading."),
            ("power_outage", "Depot power outage disrupts loading."),
            ("water_shortage", "Unexpected water shortage for personnel."),
            ("medical_outbreak", "Disease outbreak among convoy crew."),
            ("civilian_interference", "Civilians block convoy demanding aid."),
            ("animal_hazard", "Wildlife on route causes delays."),
            ("fuel_contamination", "Contaminated fuel damages engines."),
            ("equipment_misallocation", "Supplies sent to wrong unit."),
            ("overloaded_vehicles", "Vehicles overloaded, causing breakdowns."),
            ("navigation_error", "GPS malfunction leads convoy off course."),
            ("late_orders", "Late operational orders cause supply confusion."),
            ("enemy_decoy", "Enemy sets up decoy to lure convoy."),
            ("friendly_unit_block", "Friendly unit blocks route unintentionally."),
            ("airspace_denied", "Airspace closure prevents resupply flights."),
            ("hazmat_spill", "Hazardous material spill delays operations."),
            ("lost_manifest", "Lost supply manifest causes confusion."),
            ("equipment_shortage", "Shortage of critical equipment for mission."),
            ("fuel_rationing", "Fuel rationing limits operational reach."),
            ("communications_failure", "Comms failure between convoy and HQ."),
            ("late_arrival", "Supplies arrive too late for operation."),
            ("enemy_psyops", "Enemy psychological ops lower crew morale."),
            ("civilian_protest", "Protesters block access to supply depot."),
            ("enemy_roadblocks", "Enemy sets up roadblocks on main route."),
            ("friendly_miscommunication", "Miscommunication causes supply duplication."),
            ("enemy_spy", "Enemy spy embedded in operations staff."),
        ],
        "logistics": [
            ("cyber_attack", "Logistics tracking systems compromised."),
            ("natural_disaster", "Flooding has made primary supply routes impassable."),
            ("infrastructure_failure", "Bridge collapse on main supply route."),
            ("weather_event", "Severe weather delaying air and ground resupply."),
            ("resource_scarcity", "Fuel shortages impacting vehicle availability."),
            ("communication_blackout", "Loss of comms hindering coordination of logistics."),
            ("mechanical_failure", "Vehicle breakdowns reducing convoy effectiveness."),
            ("terrain_challenge", "Difficult terrain slowing down supply deliveries."),
            ("loss_of_personnel", "Key logistics personnel unavailable due to illness."),
            ("equipment_shortage", "Lack of necessary equipment for supply handling."),
            ("logistical_error", "Mismanagement leading to supply misallocation."),
            ("allied_miscommunication", "Allied forces miscommunicating supply needs."),
            ("transportation_delay", "Delays in transportation assets affecting supply timelines."),
            ("fuel_shortage", "Fuel supplies critically low, impacting vehicle operations."),
            ("cybersecurity_breach", "Cyber breach causing delays in logistics software systems."),
            ("warehouse_fire", "Fire in warehouse destroys supplies."),
            ("port_closure", "Port closure delays overseas shipments."),
            ("customs_hold", "Customs hold at border delays critical parts."),
            ("labor_strike", "Labor strike halts loading operations."),
            ("container_loss", "Shipping container lost at sea."),
            ("supply_mislabel", "Supplies mislabeled, causing confusion."),
            ("inventory_mismatch", "Inventory records do not match physical stock."),
            ("expired_supplies", "Expired supplies discovered in storage."),
            ("theft", "Supplies stolen from depot."),
            ("fuel_leak", "Fuel leak reduces available reserves."),
            ("power_failure", "Power failure at logistics hub."),
            ("software_bug", "Software bug causes order duplication."),
            ("overstock", "Overstock of non-essential items fills warehouse."),
            ("understaffed", "Insufficient staff for unloading operations."),
            ("vehicle_shortage", "Not enough vehicles for scheduled deliveries."),
            ("route_closure", "Road closure forces long detour."),
            ("supply_spoilage", "Perishable supplies spoil in transit."),
            ("container_damage", "Damaged containers lead to supply loss."),
            ("unplanned_inspection", "Surprise inspection delays shipments."),
            ("fuel_diversion", "Fuel diverted to higher-priority units."),
            ("equipment_recall", "Critical equipment recalled for defects."),
            ("maintenance_backlog", "Maintenance backlog grounds vehicles."),
            ("supply_duplication", "Duplicate orders waste resources."),
            ("manual_override", "Manual override causes inventory errors."),
            ("untrained_personnel", "Untrained staff mishandle supplies."),
            ("hazmat_incident", "Hazardous materials incident delays operations."),
            ("lost_shipment", "Shipment lost in transit."),
            ("container_shortage", "Shortage of containers for shipping."),
            ("unsecured_load", "Unsecured load causes damage in transit."),
            ("fuel_misallocation", "Fuel sent to wrong unit."),
            ("supply_backorder", "Critical supplies on backorder."),
            ("vehicle_accident", "Accident damages supply vehicle."),
            ("late_payment", "Late payment delays vendor shipments."),
            ("supply_chain_attack", "Supply chain targeted by cyber attack."),
        ]
    }

    sector = sector.lower()
    if sector not in scenarios_by_sector:
        sector = "logistics"  # default

    scenarios = scenarios_by_sector[sector]

    # If scenario_type is provided and matches, use it; else pick randomly
    scenario = None
    if scenario_type:
        for s_type, desc in scenarios:
            if s_type == scenario_type:
                scenario = (s_type, desc)
                break
    if not scenario:
        scenario = random.choice(scenarios)

    scenario_type, impact = scenario

    return {
        "unit": unit,
        "sector": sector,
        "scenario_type": scenario_type,
        "impact": impact,
        "recommendation": "Review alternate supply routes and increase convoy security."
    }