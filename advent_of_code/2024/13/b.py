from itertools import batched
import re
from typing import NamedTuple, Optional

from nptyping import Int, NDArray, Shape
import numpy as np

from algutils.color_print import cpprint, cprint
from algutils.utils import debug, vdebug, vvdebug


Vector2D = NDArray[Shape["1, 2"], Int]


def vector_2d(vₓ: int, vᵧ: int) -> Vector2D:
    return np.array([vₓ, vᵧ], dtype=int)


class MachineBehavior(NamedTuple):
    a⃗: Vector2D
    b⃗: Vector2D
    p⃗: Vector2D


MachinesBehavior = list[MachineBehavior]
PrizeCost = int


# 𝛼, 𝛽 ∈ ℕ₀,  a⃗, b⃗ ∈ ℤ²
# 𝛼a⃗ + 𝛽b⃗ = p⃗
# 3𝛼 + 𝛽 minimal
#
#   ⇓
#
# ⎧ 𝛼aₓ + 𝛽bₓ = pₓ
# ⎨
# ⎩ 𝛼aᵧ + 𝛽bᵧ = pᵧ
#
#   ⇓
#
# 1° a⃗, b⃗ linearly independent    2° a⃗, b⃗ linearly dependent    3° Else
#                                  ∧ a⃗, p⃗ linearly dependent
#
#     aₓbᵧ - aᵧbₓ ≠ 0                 TBD                           No solutions exist
#
#     ⎧     pₓbᵧ - pᵧbₓ
#     ⎪ 𝛼 = ───────────
#     ⎪     aₓbᵧ - aᵧbₓ
#     ⎨
#     ⎪     pₓaᵧ - pᵧaₓ
#     ⎪ 𝛽 = ───────────
#     ⎩     bₓaᵧ - bᵧaₓ


def solve_linearly_independent(
    a⃗: Vector2D, b⃗: Vector2D, p⃗: Vector2D
) -> Optional[PrizeCost]:
    aₓ: int
    aᵧ: int
    bₓ: int
    bᵧ: int
    pₓ: int
    pᵧ: int

    aₓ, aᵧ = a⃗
    bₓ, bᵧ = b⃗
    pₓ, pᵧ = p⃗
    # fmt: off
    𝛼 = (
        (pₓ * bᵧ - pᵧ * bₓ) //
        (aₓ * bᵧ - aᵧ * bₓ)
    )
    𝛽 = (
        (pₓ * aᵧ - pᵧ * aₓ) //
        (bₓ * aᵧ - bᵧ * aₓ)
    )
    # fmt: on

    if vvdebug():
        cprint(f"𝛼={𝛼}, 𝛽={𝛽}")

    if 𝛼 < 0 or 𝛽 < 0:
        return None
    if (𝛼 * a⃗ + 𝛽 * b⃗ == p⃗).all():
        return 3 * 𝛼 + 𝛽
    return None


def solve_linearly_dependent(
    a⃗: Vector2D, b⃗: Vector2D, p⃗: Vector2D
) -> Optional[PrizeCost]:
    raise NotImplementedError()


def are_linearly_dependent(u⃗: Vector2D, v⃗: Vector2D) -> bool:
    uₓ: int
    uᵧ: int
    vₓ: int
    vᵧ: int

    uₓ, uᵧ = u⃗
    vₓ, vᵧ = v⃗

    return uₓ * vᵧ - uᵧ * vₓ == 0


def read_input_from_stdin() -> MachinesBehavior:
    machines_behavior: MachinesBehavior = []
    while True:
        machine_behavior_str = "\n".join(input().strip() for _ in range(3))
        re_pattern = r"""
^Button A: X\+(\d+), Y\+(\d+)$
^Button B: X\+(\d+), Y\+(\d+)$
^Prize: X=(\d+), Y=(\d+)$
""".strip()
        match = re.match(re_pattern, machine_behavior_str, re.MULTILINE)
        if match is None:
            raise ValueError(
                f"""
Unexpected input `
{machine_behavior_str}
', Expected `
{re_pattern}
'
""".strip()
            )
        int_match_groups = (int(coordinate_str) for coordinate_str in match.groups())
        a⃗, b⃗, p⃗ = (vector_2d(vₓ, vᵧ) for vₓ, vᵧ in batched(int_match_groups, n=2))
        p⃗ += vector_2d(10**13, 10**13)
        machine_behavior = MachineBehavior(a⃗, b⃗, p⃗)
        machines_behavior.append(machine_behavior)

        try:
            blank_line = input().strip()
            if blank_line != "":
                raise ValueError(
                    f"Unexpected input `{blank_line}', expected `' (blank line)"
                )
        except EOFError:
            return machines_behavior


def main() -> None:
    machines_behavior = read_input_from_stdin()

    if debug():
        cprint("machines_behavior=")
        cpprint(machines_behavior)

    prizes_cost = 0
    for machine_number, machine_behavior in enumerate(machines_behavior):
        if vdebug():
            print()
            cprint(f"machine_number={machine_number}")

        a⃗, b⃗, p⃗ = machine_behavior

        if not are_linearly_dependent(a⃗, b⃗):
            if vvdebug():
                cprint("1°")
            prize_cost = solve_linearly_independent(a⃗, b⃗, p⃗)
        elif are_linearly_dependent(a⃗, p⃗):
            if vvdebug():
                cprint("2°")
            prize_cost = solve_linearly_dependent(a⃗, b⃗, p⃗)
        else:
            if vvdebug():
                cprint("3°")
            prize_cost = None

        if prize_cost is not None:
            prizes_cost += prize_cost

        if vdebug():
            cprint(f"prize_cost={prize_cost}")

    print()
    cprint(f"prizes_cost={prizes_cost}")


if __name__ == "__main__":
    main()
