import math
class KalmanFilter(object):

	PREDICT_X = 0
	PREDICT_C = 0
	K = 0
	def __init__(self, R = 1, Q = 1, A = 1, B = 0, C = 1):

		self.R = R
		self.Q = Q
		self.A = A
		self.C = C
		self.B = B
		self.cov = 0
		self.x = None

	def filter(self, z, u=0):

		if self.x is None:
			self.x = 1 / self.C * z
			self.cov = 1 / self.C * self.Q * (1/self.C)
			return self.x
		else:
			# Prediction
			self.PREDICT_X = self.A * self.x + self.B * u
			self.PREDICT_C = self.A * self.cov * self.A + self.R

			# Kalman gain
	      	self.K = self.PREDICT_C * self.C * (1 / (self.C * self.PREDICT_C * self.C + self.Q))

	      	# Correction
	      	self.x = self.PREDICT_X + self.K * (z - self.C * self.PREDICT_X)
	      	self.cov = self.PREDICT_C - self.K * self.C * self.PREDICT_C
	      	
		return self.x

	def lastMeasurement(self):
		return self.x

	def setMeasurementNoise(self, noise): 
		self.Q = noise
  
  	def setProcessNoise(self, noise): 
  		self.R = noise






  