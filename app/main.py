from errors import VaccineError


def go_to_cafe(friends: list[dict], cafe) -> str:
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

    masks_to_buy = 0

    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

    if masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
