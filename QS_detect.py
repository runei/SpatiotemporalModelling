import sys
sys.path.insert(0, 'ParticleMethods/ParticleLibrary/')

import numpy as np
from cell_list import *
from verlet_list import *
from particle import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
	positions = np.loadtxt('QSBacterialPos.dat', dtype=float)
	particles = [Particle(pos, ParticleProperties()) for pos in positions]
	cell_list = CellList(particles, 0.5)
	verlet_list = VerletList(cell_list, 0.5)
	x=[]
	y=[]
	# x = [[p.position[0] for p in cell] for cell in cell_list.cells.values()]
	# y = [[p.position[1] for p in cell] for cell in cell_list.cells.values()]
	# y = [p.position[1] for p in cell_list.particles]
	colors_cell_list = []
	colors_verlet_list = []
	# print(len(cell_list.cells))
	for cell in cell_list.cells.values():
		# print(cell.particles)
		if len(cell.particles) >= 20:
			color_cell_list = 'red'
		else:
			color_cell_list = 'blue'
		for p in cell.particles:
			x.append(p.position[0])
			y.append(p.position[1])
			colors_cell_list.append(color_cell_list)
			if len(verlet_list.verlet[p].particles) >= 50:
				colors_verlet_list.append('red')
			else:
				colors_verlet_list.append('blue')


	plt.subplot(2, 1, 1)
	plt.title('cell_list')
	plt.scatter(x, y, c=colors_cell_list)

	plt.subplot(2, 1, 2)
	plt.title('verlet_list')
	plt.scatter(x, y, c=colors_verlet_list)

	plt.show()