import os
import sys
import numpy as np
import threading
import queue


class Gnome:
	
	def __init__(self,memory_size,memory_depth):
		self.memory_size = memory_size
		self.memory_depth = memory_depth

	def __repr__(self):
		return "<Gnome object which holds struct of 2d matrix>"


	def instantiate_matrix(self):
		return np.array([[0] * self.memory_size] * self.memory_depth)



	def update_matrix_dimentions(self,matrix,delx,dely):
		print(matrix,"1")
		for x in range(delx):
			matrix = np.vstack((matrix,[0] * self.memory_size))
		for x in range(dely):
			matrix = np.column_stack((matrix, [0] * (self.memory_depth+delx)))
		return matrix
	
	def update_matrix(self,matrix,delx,dely,val):
		return matrix[delx][dely] = val

	@classmethod
	def long_seq_str(cls,s):
		# perform all compression here!
		return 	s





g = Gnome(3,3)
a = g.instantiate_matrix()
#print(g.update_matrix_dimentions(a,2,7))


class Process:
	
	def __inti__(self,qname,per_gain,pos,w,matrix):
		self.update = Gnome()
		self.qname = qname
		self.per_gain = per_gain
		self.position = pos
		self.width = w
		self.matrix = matrix

	def update_matrix_dimentions(self,row,col,val):
		return self.update.update_matrix(matrix,delx,dely,val)	


	def run_this(self,matrix,qname,qstr,otpq):
		jstr = json.loads(qstr)
		val = sum[x for x in jstr['list_val']]
		if val>0:
			self.per_gain = val
		if val<0:
			self.width -=1
		
		#update_matrix_dimentions(row,col,val):	
		# update val in position in matrix and return a list of pos and width
		# call back for if process want to wait do check 2d matrx

			
	def runner(self,qstr,out_queue):
		t = threading.Thread(target=self.run_this,args=(self.qname,qstr,out_queue,))
		t.start()
		#bug not thread safe add mutex or use blockingq 
		return out_queue.get()





# class redis and db to be implemented 







		
		
	
		
		

	 
		
