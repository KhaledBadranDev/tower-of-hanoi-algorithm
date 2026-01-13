def hanoi_solver(n: int) -> str:
    """
    Solves the Tower of Hanoi puzzle for n disks.
    Returns a string representing the state of the rods at each step.
    """
    
    # Initialize rods: 
    # Rod 0 (Source): Contains disks n down to 1 (e.g., [3, 2, 1])
    # Rod 1 (Auxiliary): Empty initially
    # Rod 2 (Target): Empty initially
    source = list(range(n, 0, -1))
    aux = []
    target = []
    
    # We keep references to the lists in a main 'rods' list for easy printing
    rods = [source, aux, target]
    
    # This list will store the snapshots of the game state
    moves_history = []

    def record_current_state():
        """
        Helper to format the current state of rods into the required string format.
        Example: "[3, 2, 1] [] []"
        """
        # Convert each rod list to a string and join them with spaces
        state = f"{rods[0]} {rods[1]} {rods[2]}"
        moves_history.append(state)

    # Record the initial state before any moves are made
    record_current_state()

    def move_disks(k, source_idx, target_idx, aux_idx):
        """
        Recursive function to move k disks from source_idx to target_idx
        using aux_idx as the helper rod.
        """
        # Base case: If no disks to move, stop.
        if k == 0:
            return

        # Step 1: Move k-1 disks from Source to Auxiliary
        move_disks(k - 1, source_idx, aux_idx, target_idx)

        # Step 2: Move the k-th (largest in this stack) disk from Source to Target
        # logic: pop from source list, append to target list
        disk = rods[source_idx].pop()
        rods[target_idx].append(disk)
        
        # Record the state after the physical move
        record_current_state()

        # Step 3: Move the k-1 disks from Auxiliary to Target
        move_disks(k - 1, aux_idx, target_idx, source_idx)

    # Trigger the recursion
    # 0 is the index of Source, 2 is Target, 1 is Auxiliary
    move_disks(n, 0, 2, 1)

    # Join all recorded states with a newline character
    return "\n".join(moves_history)

if __name__ == "__main__":
    # Test with n=3 as per the example in plan.md
    print(hanoi_solver(3))