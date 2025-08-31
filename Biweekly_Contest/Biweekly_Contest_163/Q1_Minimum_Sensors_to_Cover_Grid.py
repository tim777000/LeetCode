class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        sensor_range = k*2 + 1
        n_sensor = n // sensor_range + (0 if n % sensor_range == 0 else 1)
        m_sensor = m // sensor_range + (0 if m % sensor_range == 0 else 1)
        return n_sensor * m_sensor
