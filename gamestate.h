typedef enum gamestate{
    PLAYER_TURN,
    ENEMY_TRUN,
    CARDS_PLAYED,
    HIT,
    HEALTH,
}Gamestate; 

typedef enum Cardstate{
    MANA_COST,
    CARD_EFFECT, 
    DEMAGE_TYPE,
    
};


typedef struct  card
{
    int mana_cost;
    Cardstate cardstate;
    char *effect;
    char *damage;
    
};

