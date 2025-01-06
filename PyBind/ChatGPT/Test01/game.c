// game.c
#include <stdio.h>

typedef struct {
    int x, y; // Player position
} Player;

Player player = {0, 0};

// Moves the player
void move_player(char direction) {
    switch (direction) {
        case 'w': player.y -= 1; break; // Up
        case 's': player.y += 1; break; // Down
        case 'a': player.x -= 1; break; // Left
        case 'd': player.x += 1; break; // Right
        default: printf("Invalid direction\n");
    }
}

// Renders the game state
void render() {
    printf("Player is at (%d, %d)\n", player.x, player.y);
}

// Expose functions to Python
void step_game(char direction) {
    move_player(direction);
    render();
}
