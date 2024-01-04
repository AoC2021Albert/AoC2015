def simulate_fight(player_hp, player_mana, boss_hp, boss_damage, mana_spent, active_effects, is_player_turn):
    # Base case: Check for win or loss conditions
    if boss_hp <= 0:
        return mana_spent  # Player wins
    if player_hp <= 0:# or mana_spent >= min_mana_to_win:
        return float('inf')  # Player loses or has already spent too much mana

    # Apply effects
    player_armor = 0
    if 'Shield' in active_effects:
        player_armor += 7
    if 'Poison' in active_effects:
        boss_hp -= 3
    if 'Recharge' in active_effects:
        player_mana += 101

    # Update effects durations
    active_effects = {effect: duration - 1 for effect, duration in active_effects.items() if duration > 1}

    if is_player_turn:
        # Player's turn: Choose a spell to cast
        min_mana = float('inf')
        for spell, cost in spells.items():
            if cost <= player_mana and spell not in active_effects:
                new_mana_spent = simulate_fight(
                    player_hp,
                    player_mana - cost,
                    boss_hp,
                    boss_damage,
                    mana_spent + cost,
                    {**active_effects, **spell_effects[spell]},
                    False  # Next turn is the boss's turn
                )
                min_mana = min(min_mana, new_mana_spent)
        return min_mana
    else:
        # Boss's turn
        player_damage = max(1, boss_damage - player_armor)
        return simulate_fight(
            player_hp - player_damage,
            player_mana,
            boss_hp,
            boss_damage,
            mana_spent,
            active_effects,
            True  # Next turn is the player's turn
        )

# Define spells and their effects
spells = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229
}
spell_effects = {
    # Define the effects and durations of each spell
}

min_mana_to_win = simulate_fight(50, 500, 58, 9, 0, {}, True)
