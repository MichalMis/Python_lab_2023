import unittest
import matplotlib.pyplot as plt
from lab12_2 import sorting_alghoritm 

class TestSortingAlgorithm(unittest.TestCase):

    def test_sorting_algorithm(self):
        input_sizes = [10, 50, 100, 200]
        proc_nums = [1, 2, 4]

        results = []

        for input_size in input_sizes:
            for proc_num in proc_nums:
                time_taken = sorting_alghoritm(proc_num, input_size)
                results.append((input_size, proc_num, time_taken))

        # Visualize the results
        self.plot_results(results)

    def plot_results(self, results):
        fig, ax = plt.subplots()

        unique_proc_nums = {proc_num for (_, proc_num, _) in results}

        for proc_num in unique_proc_nums:
            data_for_proc_num = [(size, time) for size, num_processes, time in results if num_processes == proc_num]
            sizes_for_proc_num, times_for_proc_num = zip(*data_for_proc_num)
            ax.plot(sizes_for_proc_num, times_for_proc_num, label=f'{proc_num} processes')

        ax.set_xlabel('Input Size')
        ax.set_ylabel('Time (seconds)')
        ax.set_title('Sorting Algorithm Performance')
        ax.legend()
        plt.show()

if __name__ == '__main__':
    unittest.main()