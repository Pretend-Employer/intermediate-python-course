def main():
    import random
    dice_rolls = int(input("How many die would you like to roll: "))
    dice_size = int(input("How many sides are the dice? "))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a: {roll}, bad luck!')
        elif roll == dice_size:
            print(f'You rolled a: {roll}, great!')
        else:
            print(f'You rolled a: {roll}')

    print(f'Your roll totaled: {dice_sum}')


if __name__ == "__main__":
    main()
