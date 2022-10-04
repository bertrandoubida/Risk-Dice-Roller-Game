

Your name: Bertrand Oubida 

Date finished: 10/3/22




import argparse
import random
random.randint(1, 6)


parser = argparse.ArgumentParser(description='Risk Roll Dice Game')
parser.add_argument('--attacker', type=int)
parser.add_argument('--defender', type=int)
parser.add_argument('--stop',type=int)       

args = parser.parse_args()


# Simulate dice rolls to determine the output.
attackers_remaining = args.attacker
defenders_remaining = args.defender
num_attack_stops = args.stop

if num_attack_stops > attackers_remaining:
    print(f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining")
else:
    while defenders_remaining > 0 or num_attack_stops >= attackers_remaining:
    
        if attackers_remaining >= 3:
            attackers_dice_count = 3
        else:
            attackers_dice_count = attackers_remaining
    
        if defenders_remaining >= 2:
            defenders_dice_count = 2
        else:
            defenders_dice_count = defenders_remaining

        attackers_dice_roll = []
        for x in range(attackers_dice_count):
            attackers_dice_roll.append(random.randint(1,6))
    
        defenders_dice_roll = []
        for x in range(defenders_dice_count):
            defenders_dice_roll.append(random.randint(1,6))

        attackers_dice_roll.sort(reverse=True)
        defenders_dice_roll.sort(reverse=True)

     

        for attackers_dice_roll, defenders_dice_roll in zip(attackers_dice_roll, defenders_dice_roll):
                
                if attackers_dice_roll > defenders_dice_roll:
                    defenders_remaining = defenders_remaining - 1
                else: 
                    attackers_remaining = attackers_remaining - 1
                    break
        print(f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining")
                  
        if num_attack_stops == attackers_remaining:
            print(f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining") 
            break           
                        


#Type into Python terminal to run 'python risk.py --attacker 50 --defender 25 --stop 10 '              

