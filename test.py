import unittest
from unittest.mock import patch
from BowlingGame_fac import BowlingGame

class TestBolera(unittest.TestCase):
    
    def test_inicializacion(self):
        partida = BowlingGame(1)
        self.assertEqual(partida.player_name, 1)
        self.assertEqual(partida.rolls, [])
        
    def test_roll_strike(self):
        partida = BowlingGame(1)
        partida.roll(10)  
        self.assertEqual(partida.rolls, [10])
    
    def test_tiradas_de_un_bolo_20x1(self):
        partida = BowlingGame(1)
        for n in range(20):  
            partida.roll(1)
        self.assertEqual(sum(partida.rolls), 20)

    def test_tiradas_de_cero_bolos_20x0(self):
        partida = BowlingGame(1)
        for n in range(20):
            partida.roll(0)
        self.assertEqual(sum(partida.rolls), 0)
        
    def test_tirar_10_veces_3_y_el_resto_0(self):
        partida = BowlingGame(1)
        for n in range(10):  
            partida.roll(3)
        for n in range(10):  
            partida.roll(0)
        self.assertEqual(sum(partida.rolls), 30)

    def test_semipleno_con_puntuacion_extra(self):
        partida = BowlingGame(1)
        partida.roll(5)
        partida.roll(5)  
        partida.roll(3)  
        for n in range(17):  
            partida.roll(0)
        self.assertEqual(sum(partida.rolls), 13)

    @patch('BowlingGame.BowlingGame.score')
    def test_pleno_con_puntuacion_extra(self, mock_score):
        mock_score.return_value = 20
        
        partida = BowlingGame(1)
        partida.roll(10)  
        partida.roll(3)
        partida.roll(2)   
        for n in range(17):      
            partida.roll(0)
            
        self.assertEqual(partida.score(), 20)

if __name__ == '__main__':
    unittest.main()
