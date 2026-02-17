# Finite Difference Solver for the 2D Poisson Equation

## Overview

This project implements a finite difference solver for the 2D Poisson equation with mixed boundary conditions.

The system models steady-state heat distribution in a rectangular domain with:

- Dirichlet boundary conditions on left and right edges
- Robin and Neumann boundary conditions on top and bottom
- Constant volumetric source term

The solution is computed iteratively until convergence.

---

## Numerical Method

- Spatial discretization using second-order finite differences
- Uniform grid
- Iterative relaxation method (Jacobi-style update)
- Convergence criterion based on L2 norm

---

## Equation

∇²T = -f

with mixed boundary conditions.

---

## Results

The solver is tested for increasing grid resolutions to observe convergence and computational cost scaling.

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib

---

## Author

Esther Menéndez
BSc Physics
