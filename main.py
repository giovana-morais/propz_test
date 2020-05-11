import question_1 as hunter_game
import question_3 as stats
import numpy as np

if __name__ == '__main__':
    print("First question")
    hunter_game.game()

    print("Third question")
    sample = np.array([1,2,3,4,1,5,2,2,3])
    stats.get_stats(sample)
