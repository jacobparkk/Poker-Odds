import random

# 1. Card Representation and Deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']
deck = [(rank, suit) for rank in ranks for suit in suits]

# 2. Hand Evaluation (Simplified)
def evaluate_hand(hand):
    """
    Evaluates a 5-card hand (simplified for this example).
    Returns a tuple: (hand_rank, high_card_rank)
    where hand_rank is a number representing the hand's strength:
    0: High Card
    1: Pair
    2: Two Pair
    3: Three of a Kind
    4: Straight
    5: Flush
    6: Full House
    7: Four of a Kind
    8: Straight Flush
    """

    ranks_count = {}
    suits_count = {}
    for rank, suit in hand:
        ranks_count[rank] = ranks_count.get(rank, 0) + 1
        suits_count[suit] = suits_count.get(suit, 0) + 1

    rank_values = [ranks.index(rank) for rank, _ in hand]
    rank_values.sort(reverse=True)

    is_flush = len(suits_count) == 1
    is_straight = (max(rank_values) - min(rank_values) == 4) and len(set(rank_values)) == 5

    if is_straight and is_flush:
        return (8, rank_values[0])  # Straight Flush
    elif 4 in ranks_count.values():
        four_kind_rank = [rank for rank, count in ranks_count.items() if count == 4][0]
        return (7, ranks.index(four_kind_rank))  # Four of a Kind
    elif 3 in ranks_count.values() and 2 in ranks_count.values():
        three_kind_rank = [rank for rank, count in ranks_count.items() if count == 3][0]
        return (6, ranks.index(three_kind_rank))  # Full House
    elif is_flush:
        return (5, rank_values[0])  # Flush
    elif is_straight:
        return (4, rank_values[0])  # Straight
    elif 3 in ranks_count.values():
        three_kind_rank = [rank for rank, count in ranks_count.items() if count == 3][0]
        return (3, ranks.index(three_kind_rank))  # Three of a Kind
    elif len([count for count in ranks_count.values() if count == 2]) == 2:
        two_pair_ranks = [ranks.index(rank) for rank, count in ranks_count.items() if count == 2]
        two_pair_ranks.sort(reverse=True)
        return (2, two_pair_ranks[0]) # Two Pair
    elif 2 in ranks_count.values():
        pair_rank = [rank for rank, count in ranks_count.items() if count == 2][0]
        return (1, ranks.index(pair_rank))  # Pair
    else:
        return (0, rank_values[0])  # High Card

# 3. Monte Carlo Simulation
def calculate_odds(my_hand, community_cards, num_simulations=10000):
    wins = 0
    for _ in range(num_simulations):
        temp_deck = deck[:]  # Create a copy of the deck
        random.shuffle(temp_deck)

        # Remove my hand and known community cards from the deck
        for card in my_hand:
            temp_deck.remove(card)
        for card in community_cards:
            temp_deck.remove(card)

        # Deal remaining community cards (if any)
        num_remaining_community_cards = 5 - len(community_cards)
        remaining_community_cards = temp_deck[:num_remaining_community_cards]
        temp_deck = temp_deck[num_remaining_community_cards:]

        # Deal opponent's hand
        opponent_hand = temp_deck[:2]

        # Evaluate hands
        my_full_hand = my_hand + community_cards + remaining_community_cards
        opponent_full_hand = opponent_hand + community_cards + remaining_community_cards
        my_hand_rank = evaluate_hand(my_full_hand)
        opponent_hand_rank = evaluate_hand(opponent_full_hand)

        # Determine the winner
        if my_hand_rank > opponent_hand_rank:
            wins += 1

    return wins / num_simulations

# 4. Get User Input for Cards
def get_user_card(prompt):
    while True:
        card_str = input(prompt).upper()
        if len(card_str) != 2:
            print("Invalid card format. Please use two characters (rank and suit).")
            continue

        rank = card_str[0]
        suit = card_str[1]

        if rank not in ranks or suit not in suits:
            print("Invalid card rank or suit.")
            continue

        card = (rank, suit)
        if card not in deck:
            print("Card already taken or invalid. Please choose another card.")
            continue

        return card

# --- Main Program ---
if __name__ == "__main__":
    print("Enter your two hole cards:")
    card1 = get_user_card("Enter card 1 (e.g., AH for Ace of Hearts, TS for Ten of Spades): ")
    card2 = get_user_card("Enter card 2: ")
    my_hand = [card1, card2]

    win_probability = calculate_odds(my_hand, [])
    print(f"Approximate win probability (pre-flop) with {my_hand}: {win_probability:.4f}")

    # Get Flop cards
    print("\nEnter the flop cards (3 cards):")
    flop_card1 = get_user_card("Enter flop card 1: ")
    flop_card2 = get_user_card("Enter flop card 2: ")
    flop_card3 = get_user_card("Enter flop card 3: ")
    flop_cards = [flop_card1, flop_card2, flop_card3]

    win_probability = calculate_odds(my_hand, flop_cards)
    print(f"Approximate win probability (after flop) with {my_hand} and flop {flop_cards}: {win_probability:.4f}")

    # Get Turn card
    turn_card = get_user_card("\nEnter the turn card: ")
    turn_cards = flop_cards + [turn_card]

    win_probability = calculate_odds(my_hand, turn_cards)
    print(f"Approximate win probability (after turn) with {my_hand} and turn {turn_cards}: {win_probability:.4f}")

    # Get River card
    river_card = get_user_card("\nEnter the river card: ")
    river_cards = turn_cards + [river_card]

    win_probability = calculate_odds(my_hand, river_cards)
    print(f"Approximate win probability (after river) with {my_hand} and river {river_cards}: {win_probability:.4f}")