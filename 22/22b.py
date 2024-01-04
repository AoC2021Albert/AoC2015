def simulate_fight(player_hp, boss_hp, boss_damage, mana, active_spells, mana_spent, player_turn):
    # Check for active spell effects
    if active_spells['Shield'] > 0:
        player_armor = 7
        active_spells['Shield'] -= 1
    else:
        player_armor = 0

    if active_spells['Poison'] > 0:
        boss_hp -= 3
        active_spells['Poison'] -= 1

    if active_spells['Recharge'] > 0:
        mana += 101
        active_spells['Recharge'] -= 1

    # Check win/lose conditions
    if boss_hp <= 0:
        return mana_spent
    if mana_spent > global_min_mana[0]:
        return float('inf')

    # Player's turn
    if player_turn:
        min_mana_cost = float('inf')
        for spell, cost in spells.items():
            if mana >= cost and active_spells[spell] == 0:
                new_spells = active_spells.copy()
                new_mana = mana - cost
                new_mana_spent = mana_spent + cost

                if spell == 'Magic Missile':
                    boss_hp -= 4
                elif spell == 'Drain':
                    boss_hp -= 2
                    player_hp += 2
                elif spell in ['Shield', 'Poison', 'Recharge']:
                    new_spells[spell] = spells_duration[spell]

                mana_cost = simulate_fight(player_hp, boss_hp, boss_damage, new_mana, new_spells, new_mana_spent, False)
                min_mana_cost = min(min_mana_cost, mana_cost)

        return min_mana_cost

    # Boss's turn
    else:
        player_damage = max(1, boss_damage - player_armor)
        player_hp -= player_damage
        if player_hp <= 0:
            return float('inf')
        return simulate_fight(player_hp, boss_hp, boss_damage, mana, active_spells, mana_spent, True)


# Spell definitions
spells = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229
}
spells_duration = {
    'Shield': 6,
    'Poison': 6,
    'Recharge': 5
}

# Global variable to store the minimum mana spent
global_min_mana = [float('inf')]

# Initial conditions
player_hp = 50
boss_hp = 58
boss_damage = 9
mana = 500

# Initial active spells
active_spells = {spell: 0 for spell in spells}

# Start simulation
min_mana_cost = simulate_fight(player_hp, boss_hp, boss_damage, mana, active_spells, 0, True)
print(f"Minimum mana to win: {min_mana_cost}")
