"""Newton-step plot, styled for the yalix dark 'terminal notebook' theme.

f(x) = 0.05x^4 - 0.2x^3 - 0.5x^2 + x + 2, one Newton step from x_k = 3.5.
Run:  python3 newton_step.py   ->   newton_step.png (transparent, dark-ready)
"""

import numpy as np
import matplotlib.pyplot as plt

INK = "#22261F"     # curve / axes
MUTED = "#7C8274"   # ticks
TEAL = "#4F6B4C"    # x_k  (sage accent)
WARM = "#C18A4A"    # x_{k+1} (warm)


def f(x):
    return 0.05 * x**4 - 0.2 * x**3 - 0.5 * x**2 + x + 2


def df(x):
    return 0.2 * x**3 - 0.6 * x**2 - x + 1


def d2f(x):
    return 0.6 * x**2 - 1.2 * x - 1


x_k = 3.5
t = -df(x_k) / d2f(x_k)
x_next = x_k + t

xs = np.linspace(-2.6, 5.2, 400)
fig, ax = plt.subplots(figsize=(5, 3.1))
ax.plot(xs, f(xs), color=INK, linewidth=2)
ax.axhline(0, color=MUTED, linewidth=0.8)
ax.axvline(0, color=MUTED, linewidth=0.8)

ax.plot(x_k, f(x_k), "o", color=TEAL, markersize=6)
ax.annotate("x_k", (x_k, f(x_k)), textcoords="offset points",
            xytext=(-6, -14), color=TEAL, fontweight="bold")
ax.plot(x_next, f(x_next), "o", color=WARM, markersize=6)
ax.annotate("x_{k+1}", (x_next, f(x_next)), textcoords="offset points",
            xytext=(2, -16), color=WARM, fontweight="bold")

ax.set_xticks([-2, 0, 2, 4])
ax.set_yticks([-2, 2])
ax.tick_params(colors=MUTED, labelsize=8)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_facecolor("none")
fig.patch.set_alpha(0.0)          # transparent -> sits on the panel
plt.tight_layout()
plt.savefig("newton_step.png", dpi=200, transparent=True)
print(f"t = {t:.3f},  x_next = {x_next:.3f}")
