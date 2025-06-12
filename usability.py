# --------------------------------------------
# McCall's Software Quality Model Evaluation
# --------------------------------------------

# Step 1: Define quality factors and their weights
quality_factors = {
    "Reliability": 0.4,     # Weight for reliability
    "Maintainability": 0.3, # Weight for maintainability
    "Usability": 0.3        # Weight for usability
}

# Step 2: Function to get input score for each factor
def get_scores():
    scores = {}
    print("Rate the software on a scale from 1 (worst) to 10 (best):\n")

    for factor in quality_factors:
        while True:
            try:
                score = float(input(f"{factor} score: "))
                if 1 <= score <= 10:
                    scores[factor] = score
                    break
                else:
                    print("Please enter a value between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return scores

# Step 3: Compute weighted quality score
def compute_quality_score(scores):
    total_score = 0
    for factor, score in scores.items():
        weight = quality_factors[factor]
        total_score += score * weight
    return total_score

# Step 4: Interpret the score
def interpret_score(score):
    if score >= 8:
        return "Excellent quality"
    elif score >= 6:
        return "Good quality"
    elif score >= 4:
        return "Average quality"
    else:
        return "Poor quality"

# Step 5: Main execution
def main():
    print("McCall's Software Quality Evaluation\n")
    scores = get_scores()
    quality_score = compute_quality_score(scores)
    interpretation = interpret_score(quality_score)

    print("\n--- Evaluation Summary ---")
    for factor in quality_factors:
        print(f"{factor}: {scores[factor]} (Weight: {quality_factors[factor]})")

    print(f"\nOverall Quality Score: {quality_score:.2f}")
    print(f"Assessment: {interpretation}")

# Run the program
if __name__ == "__main__":
    main()
