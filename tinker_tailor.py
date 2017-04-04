import time


class Main:

    @staticmethod
    def tinker_tailor(n, k):
        start_time = time.time()
        players = list(range(1, n + 1))  # Fill a list with n pieces of number
        index_to_remove = 0
        pop_list = []
        while players:
            index_to_remove = (index_to_remove + k - 1) % len(players)  # k-1 because of the index
            pop_list.append(players.pop(index_to_remove))
        print("--- %s seconds ---" % (time.time() - start_time))
        print('Result:', pop_list, '\nWinner:', pop_list[-1])

if (__name__ == "__main__"):
    Main.tinker_tailor(5, 3)
