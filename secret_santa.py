import random
import os
import sys
import time

def clear_screen():
    """Clears the terminal screen based on the OS."""
    # 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_participants():
    """Gets a list of names from the user."""
    participants = []
    print("--- 🎅 Secret Santa Setup 🎅 ---")
    print("Enter the names of the participants.")
    print("Type 'done' when you are finished adding names.")
    print("-" * 30)
    
    while True:
        name = input(f"Enter name #{len(participants) + 1}: ").strip()
        
        if name.lower() == 'done':
            if len(participants) < 2:
                print("❌ Error: You need at least 2 people for Secret Santa!")
                continue
            break
        
        if name:
            if name in participants:
                print(f"⚠️  '{name}' is already in the list. Please use a unique name/nickname.")
            else:
                participants.append(name)
                
    return participants

def generate_pairs(participants):
    """
    Generates Secret Santa pairs using a circular shift.
    This guarantees no one gets themselves and everyone gets exactly one person.
    """
    shuffled = participants[:]
    random.shuffle(shuffled)
    
    pairs = {}
    count = len(shuffled)
    
    for i in range(count):
        giver = shuffled[i]
        # Assign to the next person in the list, wrapping around to the start
        receiver = shuffled[(i + 1) % count] 
        pairs[giver] = receiver
        
    return pairs

def run_reveal_process(pairs):
    """Interactive loop to reveal names secretly."""
    givers = list(pairs.keys())
    # Shuffle the order of givers so the "circle" pattern isn't obvious
    random.shuffle(givers) 
    
    clear_screen()
    print("--- 🤫 Secret Santa Reveal Phase 🤫 ---")
    print("Gather everyone around, but come to the computer ONE BY ONE.")
    print("When you are done, press Enter to clear the screen for the next person.")
    print("-" * 50)
    input("Press Enter to start...")

    for giver in givers:
        clear_screen()
        print(f"👋 Hello, {giver}!")
        input(f"Press Enter to reveal who you are buying for...")
        
        print("\n" * 2)
        print(f"   🎁  You are the Secret Santa for:  👉  {pairs[giver]}  👈  🎁")
        print("\n" * 2)
        
        input("Press Enter to clear the screen for the next person (DON'T LET THEM SEE!)...")
        clear_screen()

    print("🎉 All names have been drawn! Merry Christmas! 🎉")

def main():
    try:
        clear_screen()
        participants = get_participants()
        pairs = generate_pairs(participants)
        run_reveal_process(pairs)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

if __name__ == "__main__":
    main()