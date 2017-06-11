import unittest

from mock import Mock

from container import Container
from population import Population


class PopulationTest(unittest.TestCase):
    def test_population_for_calculate_fitness(self):
        mock_container_1 = Mock(spec=Container)
        mock_container_2 = Mock(spec=Container)
        container_list = [mock_container_1, mock_container_2]
        mock_container_1.fitness = Mock(return_value=1)
        mock_container_2.fitness = Mock(return_value=2)
        population = Population(containers=container_list)
        self.assertEquals(population.fitness, [1, 2])
