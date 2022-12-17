# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:57:28 2022

@author: leonardo.braga
"""
import dists
import time


def astar(start, goal='Bucharest'):
    i=0
    validation_path = []
    while goal not in validation_path:
        if len(validation_path) == 0:
            validation_path.append(start)
        else:
            i += 1
            option = validation_path[-1]
            option_nb = sorted(dists.dists_cost[option], key=lambda x: x[1])
            if option_nb[0][0] in validation_path:
                next_dest = option_nb[1][0]
            else:
                next_dest = option_nb[0][0]
            validation_path.append(next_dest)
            print('-'*110)
            time.sleep(2)
        print(f'The best choice for the {i} station was: {validation_path}')

#You can pick a different start point from dist dictionary and check the best route...
astar('Lugoj')

#    in_validation = set([start])
#    chosen_path = APPEND.sort(dists.dist_euclidiana[in_validation])
    
#    print(dists.dist_euclidiana[start])
