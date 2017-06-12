import unittest

from mock import Mock

from container import Container
from population import Population


class PopulationTest(unittest.TestCase):
    def test_population_for_calculate_fitness_and_sort_containers(self):
        containers = self.get_list_of_mock_containers()
        population = Population(containers=containers)
        self.assertEquals(population.fitness, sorted([2, 1] * 100)[::-1])

    def test_population_generate_next_population_gives_same_population_for_zero_kill_percentage(self):
        Population.kill_percentage = 0
        containers = self.get_list_of_mock_containers()
        population = Population(containers=containers)
        next_population = population.next_population()
        self.assertEquals(next_population.fitness, population.fitness)

    def test_population_generate_next_population_gives_new_population_when_kill_percentage_is_hundred(self):
        Population.kill_percentage = 50
        containers = self.get_list_of_mock_containers()
        population = Population(containers=containers)
        next_population = population.next_population()
        self.assertNotEqual(next_population.fitness, population.fitness)
        self.assertEquals(len(next_population.containers), len(population.containers))

    def get_list_of_mock_containers(self):
        mock_container_1 = Mock(spec=Container)
        mock_container_2 = Mock(spec=Container)
        child_container_1 = Mock(spec=Container)
        child_container_2 = Mock(spec=Container)
        mock_container_1.fitness = Mock(return_value=1)
        mock_container_2.fitness = Mock(return_value=2)
        mock_container_1.crossover = mock_container_2.crossover = Mock(return_value=(child_container_1, child_container_2))
        container_list = [mock_container_1, mock_container_2] * 100
        return container_list
