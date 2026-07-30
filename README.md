# Probabilistic Racetrack Localization

Author: Georgia Kalapotharakou

This repository contains a probabilistic racetrack simulation project using Kalman filtering, particle filtering, Bayesian networks, and stochastic noise models. The project simulates two cars on a racetrack and estimates their positions under different sensor and GPS noise conditions.

## My Contributions

This project was built on top of a course-provided racetrack simulator framework. The provided framework included parts of the car dynamics, GUI, racetrack representation, and simulation environment.

My main contributions were implementing and extending the probabilistic modeling components, including:

- Kalman filter state estimation for car position and velocity
- Particle filter initialization, transition sampling, weighting, resampling, and pose estimation
- Bayesian network construction and inference experiments
- Additional noise models, including Laplace and Cauchy noise
- Extra-credit adaptive particle filtering using KLD sampling
- Plotting and comparison tools for filter performance
  
## Files

### Implemented / Modified Components

- `kalman_filter.py` - Kalman filter implementation for GPS-based state estimation
- `particle_filter.py` - particle filter implementation for estimating car pose
- `particle_filter_extra.py` - extra-credit adaptive particle filter using KLD sampling
- `bayesian_network.py` - Bayesian network construction and inference experiments
- `utils.py` - helper functions, including additional noise models
- `plots.py` - plotting script for comparing true and estimated trajectories

### Course-Provided Framework Files

- `gui.py` - interactive Tkinter GUI for the racetrack simulator
- `simulator.py` - main simulator loop, checkpoints, cars, and filter integration
- `car.py` - car dynamics and sensor/GPS measurement logic
- `racetrack.py` - racetrack representation and geometry utilities
- `probability.py` - probability/Bayesian-network helper code

### Data Files
The `data/` folder is required but omitted because it was course-provided.

## Requirements

Install dependencies with `pip install -r requirements.txt`

## How to Run the GUI
Use `python gui.py`.
You can also change the number of particles, sensor range, sensor noise, GPS noise, and noise type:
- python gui.py -n 100 -m 50 -s 2.0 -nt gaussian
- python gui.py -n 100 -m 50 -s 2.0 -nt laplace
- python gui.py -n 100 -m 50 -s 2.0 -nt cauchy

## GUI Controls
- Arrow keys: control Car 1
- WASD: control Car 2
- p: toggle particle filtering
- k: toggle Kalman filtering
- o: toggle occupancy grid/sensors
- r: toggle particle display
- g: switch GPS noise distribution

## Generate Plots
### Particle filter:
- python plots.py -w pf -n 100 -m 50 -s 2.0 -sd gaussian -f particle_filter.png

### Kalman filter:
- python plots.py -w kf -d gaussian -gv 10.0 -f kalman_filter.png
- python plots.py -w kf -d uniform -gw 20 -f kalman_uniform.png

Plots are saved in the `plots/` directory. I have included some of my own plots from my runs as examples.
