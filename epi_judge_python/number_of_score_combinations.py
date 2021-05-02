from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    num_combs = [[1] + [0] * final_score
                 for _ in individual_play_scores]

    for i, play_score in enumerate(individual_play_scores):
        for cur_score in range(1, final_score + 1):
            without = num_combs[i - 1][cur_score] if play_score >= 0 else 0
            withit = (num_combs[i][cur_score - play_score]
                      if cur_score >= play_score else 0)

            num_combs[i][cur_score] = without + withit

    return num_combs[-1][-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
