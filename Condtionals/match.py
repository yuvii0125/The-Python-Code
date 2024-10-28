def process_value(value):
    match value:
        case (x, y):
            print(f"Matched a tuple: x={x}, y={y}")
        
        case {"type": "circle", "radius": r}:
            area = 3.14 * r * r
            print(f"Matched a circle with radius {r}. Area = {area:.2f}")

        case {"type": "rectangle", "width": w, "height": h}:
            area = w * h
            print(f"Matched a rectangle with width {w} and height {h}. Area = {area:.2f}")

        case [first, *rest]:
            print(f"Matched a list with first element: {first} and rest: {rest}")

        case _:
            print("No match found.")

# Test cases
print("Testing with a tuple:")
process_value((10, 20))

print("\nTesting with a circle:")
process_value({"type": "circle", "radius": 5})

print("\nTesting with a rectangle:")
process_value({"type": "rectangle", "width": 4, "height": 6})

print("\nTesting with a list:")
process_value([1, 2, 3, 4])

print("\nTesting with an unmatched value:")
process_value(42)
