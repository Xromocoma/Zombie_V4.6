def start_menu():
    print("""Hello stranger, this is Zombie_v4.6 simulator
            Today you can see what happened if you didn`t use a medical mask in public places
            You can choose mode: 
            1 - if you want to use own options to create a simulation
            2 - if you want to generate random options for simulation
            0 - exit
            """, flush=True)
    while True:
        try:
            player_choose = int(input("Your choose:"))
            if player_choose == 0:
                exit(0)
            elif player_choose == 1 or player_choose == 2:
                break
            else:
                print("You entered an incorrect selection, enter 0, 1, or 2 to select options.", flush=True)
                continue
        except Exception as e:
            print("You entered an incorrect selection, enter 0, 1, or 2 to select options.", flush=True)

    return player_choose
