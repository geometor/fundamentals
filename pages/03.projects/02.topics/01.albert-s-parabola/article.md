---
title: 'Albert''s Parabola'
subtitle: 'distance from parabola to point on directrix'
author: /home
collection:
    name: Articles
    showCount: true
    showMenu: true
content:
    items: '@self.children'
child_type: article
gallery:
    show: true
---

This article explores the problem of finding the shortest distance between a parabola and a point on its directrix. This problem is known as "Albert's Parabola Problem".

## The Problem

Given a parabola and a point **M** on its directrix, we want to find the shortest distance **d** between the point **M** and the parabola.

### Parabola Definition

Let's define the parabola by the equation:

```
y = x^2 + 1
```

This parabola has the following properties:
- **Vertex (V):** (0, 1)
- **Focus (F):** (0, 2)
- **Directrix:** y = 0 (the x-axis)

### Point on the Directrix

Let the point **M** on the directrix be defined as:

```
P = (M, 0)
```

### Point on the Parabola

Let a point **Q** on the parabola be defined as:

```
Q = (x, y) = (x, x^2 + 1)
```

## Solution Approach

The distance **d** between the point **P** on the directrix and the point **Q** on the parabola is given by the standard distance formula:

```
d^2 = (x_p - x_q)^2 + (y_p - y_q)^2
```

Substituting the coordinates of our points **P** and **Q**:

```
d^2 = (M - x)^2 + (0 - (x^2 + 1))^2
d^2 = (M - x)^2 + (x^2 + 1)^2
```

To find the shortest distance, we need to find the value of **x** that minimizes **d** (or **d^2**). We can do this using calculus:

1. **Find the expression for d^2 in terms of x.**
   We already have this: `d^2 = (M - x)^2 + (x^2 + 1)^2`

2. **Find the derivative of d^2 with respect to x.**
   Let `D = d^2`. We need to find `dD/dx`.

   `D = M^2 - 2Mx + x^2 + x^4 + 2x^2 + 1`
   `D = x^4 + 3x^2 - 2Mx + M^2 + 1`

   `dD/dx = 4x^3 + 6x - 2M`

3. **Set the derivative to 0 to find the critical points.**
   `4x^3 + 6x - 2M = 0`
   `2x^3 + 3x - M = 0`

This cubic equation gives the value of **x** for the point **Q** on the parabola that is closest to the point **P** on the directrix. The solution to this equation will give the x-coordinate of the point on the parabola that minimizes the distance.