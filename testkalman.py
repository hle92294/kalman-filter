from kalman import KalmanFilter
import math 

process_noise = 0.05 # Kalman parameter {R}
measurement_noise = 3	# Kalman parameter {Q}
use_kalman_filter = 0

kf = KalmanFilter(R = 0.01, Q =3)

data = [42.1, 22.2, 34, 44, 56, 44.1, 31.5]

data = map(kf.filter, data)

print data



