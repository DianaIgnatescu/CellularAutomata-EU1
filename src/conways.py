import pygame, random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
BTN_COLOR = (175, 203, 255)
MARGIN = 3
SQ_LENGTH = 20
SQ_NUM = 25
WIN_SIZE = (SQ_NUM + 1) * MARGIN + SQ_NUM * SQ_LENGTH
BTN_SIZE = 30

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE + BTN_SIZE + 20)
screen = pygame.display.set_mode(size)

# Initial state
automata = [0] * (SQ_NUM * SQ_NUM)

# TODO add some variables to track generations and speed of game start and stop etc
generations = 0
time_step = 5
running = True

# Assign Random Values to our Automata
# rowx:
#     col:
#         automata[row * SQ_NUM + col] = set to a random number

# for i in range(SQ_NUM * SQ_NUM):
#     automata[i] = random.randint(0, 1)


# Assign Random Values to our Automata
for row in range(SQ_NUM):
    for col in range(SQ_NUM):
        automata[row * SQ_NUM + col] = random.randint(0, 1)


# TODO add some special figures on to the screen

# Block
automata[3] = 1
automata[4] = 1
automata[SQ_NUM + 3] = 1
automata[SQ_NUM + 4] = 1

# Bee-Hive

automata[SQ_NUM - 6] = 1
automata[SQ_NUM - 5] = 1
automata[SQ_NUM + SQ_NUM - 4] = 1
automata[SQ_NUM + SQ_NUM - 7] = 1
automata[2 * SQ_NUM + SQ_NUM - 5] = 1
automata[2 * SQ_NUM + SQ_NUM - 6] = 1

# Blinker
# Beacon
# Glider

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# TODO add a font

font = pygame.font.Font('freesansbold.ttf', 14)

# TODO Add a button

inc_timestep_button = pygame.draw.rect(screen, BTN_COLOR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #     Click event
    #     TODO this is where all events are added
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()

            # use the pos of mouse to decide which button was pressed
            if inc_timestep_button.collidepoint(click_position) and time_step < 20:
                print("faster")
                time_step += 1

    # --- Game logic should go here

    # Update State ( Add Rules to update each cell based on it's previous state )
    # Create a new automata for the next state
    new_automata = [0] * (SQ_NUM * SQ_NUM)

    for i in range(len(automata)):
        live = 0
        dead = 8

        # Look at neighbors

        # Left
        if i - 1 >= 0 and automata[i - 1]:
            live += 1
        # Right
        if i + 1 < (SQ_NUM * SQ_NUM) and automata[i + 1]:
            live += 1
        # Top
        if i - SQ_NUM >= 0 and automata[i - SQ_NUM]:
            live += 1
        # Bottom
        if i + SQ_NUM < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM]:
            live += 1
        # Top left
        if i - SQ_NUM - 1 >= 0 and automata[i - SQ_NUM - 1]:
            live += 1
        # Top right
        if i - SQ_NUM + 1 >= 0 and automata[i - SQ_NUM + 1]:
            live += 1
        # Bottom left
        if i + SQ_NUM - 1 < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM - 1]:
            live += 1
        # Bottom right
        if i + SQ_NUM + 1 < (SQ_NUM * SQ_NUM) and automata[i + SQ_NUM + 1]:
            live += 1

        # Update State

        # If there are less than 2 living neighbors, the cell dies
        if automata[i] and live < 2:
            new_automata[i] = 0
        # If alive and has less than 4 neighbors, the cell carries on living
        elif automata[i] and live < 4:
            new_automata[i] = 1
        # If alive and has more than 4 live neighbors, the cell dies
        elif automata[i] and live > 4:
            new_automata[i] = 0
        # If alive and has exactly 2 neighbors, the cell stays alive
        elif automata[i] and (live == 2 or live == 3):
            new_automata[i] = 1
        # If dead and has exactly 3 live neighbors, the cell comes to life
        elif not automata[i] and live == 3:
            new_automata[i] = 1
        else:
            automata[i] = 0

    # swap the data for the next generations data
    automata = new_automata

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
    # automata[12] = 1

    # --- Drawing code should go here
    # pygame.draw.rect(screen, RED, pygame.Rect(20, 20, 20, 20))

    y = MARGIN
    i = 0
    while y < WIN_SIZE:
        x = MARGIN
        while x < WIN_SIZE:
            if automata[i] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
            i += 1
            x += SQ_LENGTH + MARGIN
        y += SQ_LENGTH + MARGIN
    # Update inc timestep button
    inc_timestep_button = pygame.draw.rect(screen, BTN_COLOR, pygame.Rect(10, WIN_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    text = font.render("Increment", True, (14, 28, 54))  # Change text in button and refactor colour
    text_rect = text.get_rect()
    text_rect.center = (inc_timestep_button.center[0], inc_timestep_button.center[1])
    screen.blit(text, text_rect)


    # TODO add other button updates

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(time_step)

# Close the window and quit.
pygame.quit()