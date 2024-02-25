class BowlingGame:
    
    """Representa un juego de bolos."""
    
    def __init__(self, player_name):
        self.player_name = player_name  
        self.rolls = []  

    def roll(self, pins):
        """Añade el número de pines derribados en un lanzamiento a la lista de lanzamientos."""
        assert 0 <= pins <= 10, "El número de pines debe estar entre 0 y 10."
        self.rolls.append(pins)

    def score(self):
        """Calcula la puntuación total del juego después de 10 frames."""
        return self.score_up_to_frame(10)

    def score_up_to_frame(self, frame):
        """Calcula la puntuación hasta un frame específico."""
        score = 0
        roll_index = 0  
        for frame_number in range(1, frame + 1):
            if self.is_strike(roll_index):  
                score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):  
                score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:  
                score += self.sum_of_balls_in_frame(roll_index)
                roll_index += 2
            
            # Bonificación especial para el décimo frame.
            if frame_number == 10 and roll_index < len(self.rolls):  # Ajuste para el décimo frame
                score += sum(self.rolls[roll_index:roll_index+3]) - self.sum_of_balls_in_frame(roll_index)
                break

        return score

    # Funciones auxiliares para calcular bonificaciones y verificar condiciones de strike y spare.
    # def tenth_frame_bonus(self, roll_index):
    #     """Calcula la bonificación en el décimo frame."""
    #     bonus_rolls = self.rolls[roll_index:roll_index+3]  
    #     return sum(bonus_rolls)

    def is_strike(self, roll_index):
        """Verifica si el lanzamiento fue un strike."""
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        """Verifica si el lanzamiento fue un spare."""
        return sum(self.rolls[roll_index:roll_index+2]) == 10

    def strike_bonus(self, roll_index):
        """Calcula la bonificación por strike."""
        return sum(self.rolls[roll_index+1:roll_index+3])

    def spare_bonus(self, roll_index):
        """Calcula la bonificación por spare."""
        return self.rolls[roll_index+2]

    def sum_of_balls_in_frame(self, roll_index):
        """Suma de pines derribados en un frame."""
        return sum(self.rolls[roll_index:roll_index+2])
    
def get_player_roll(player_name, roll_num):
    """Solicita al jugador el número de pines derribados en un lanzamiento."""
    while True:
        try:
            pins = int(input(f"{player_name}, ingresa los pines derribados en el lanzamiento {roll_num}: "))
            if 0 <= pins <= 10:
                return pins
            else:
                print("Por favor, ingresa un número válido de pines (0-10).")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def main():
    """Función principal para ejecutar el juego de bolos."""
    num_players = int(input("Ingrese el número de jugadores: "))
    players = [BowlingGame(input(f"Nombre del jugador {i+1}: ")) for i in range(num_players)]

    # Proceso de juego para cada frame.
    for frame in range(1, 11):
        print(f"\nFrame {frame}")
        for player in players:
            print(f"\nTurno de {player.player_name}:")
            player_rolls_in_frame(player, frame)

    # Imprimir puntuaciones finales.
    for player in players:
        print(f"\nPuntuación final de {player.player_name}: {player.score()}")

def player_rolls_in_frame(player, frame):
    """Maneja los lanzamientos de un jugador en un frame específico."""
    if frame < 10:
        first_roll = get_player_roll(player.player_name, 1)
        player.roll(first_roll)
        if first_roll < 10:
            second_roll = get_player_roll(player.player_name, 2)
            player.roll(second_roll)
    else:  
        for roll in range(1, 4):
            pins = get_player_roll(player.player_name, roll)
            player.roll(pins)
            # Condiciones especiales para el décimo frame.
            if roll == 1 and pins < 10:
                if roll == 2 and (player.rolls[-2] + player.rolls[-1] < 10):
                    break

    print(f"Puntuación hasta el frame {frame}: {player.score_up_to_frame(frame)}")

if __name__ == "__main__":
    main()
