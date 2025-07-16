import matplotlib.pyplot as plt

# -------------------------------
# 1. Input Section
# -------------------------------
print("📌 Value Proposition Canvas Builder")
print("----------------------------------")

# Customer Profile
customer_jobs = input("Enter customer's jobs (comma-separated): ").split(",")
customer_pains = input("Enter customer's pains (comma-separated): ").split(",")
customer_gains = input("Enter customer's gains (comma-separated): ").split(",")

# Value Map
pain_relievers = input("Enter pain relievers (comma-separated): ").split(",")
gain_creators = input("Enter gain creators (comma-separated): ").split(",")
products_services = input("Enter products & services (comma-separated): ").split(",")

# -------------------------------
# 2. Fit Analysis
# -------------------------------
def analyze_fit(pains, pain_relievers, gains, gain_creators):
    fit_score = 0
    analysis = []

    for pain in pains:
        match = any(pain.lower().strip() in rel.lower() for rel in pain_relievers)
        analysis.append(f"Pain: '{pain.strip()}' → {'✅ Addressed' if match else '❌ Not Addressed'}")
        fit_score += 1 if match else 0

    for gain in gains:
        match = any(gain.lower().strip() in creator.lower() for creator in gain_creators)
        analysis.append(f"Gain: '{gain.strip()}' → {'✅ Created' if match else '❌ Not Created'}")
        fit_score += 1 if match else 0

    total = len(pains) + len(gains)
    score = (fit_score / total) * 100 if total > 0 else 0
    return analysis, score

analysis_results, fit_percentage = analyze_fit(customer_pains, pain_relievers, customer_gains, gain_creators)

# -------------------------------
# 3. Persona Generation
# -------------------------------
def generate_persona(jobs, pains, gains):
    return {
        "Name": "Alex (Hypothetical User)",
        "Goals": gains[0].strip() if gains else "N/A",
        "Frustrations": pains[0].strip() if pains else "N/A",
        "Context": jobs[0].strip() if jobs else "N/A"
    }

persona = generate_persona(customer_jobs, customer_pains, customer_gains)

# -------------------------------
# 4. Print Results
# -------------------------------
print("\n🧠 Fit Analysis:")
for line in analysis_results:
    print(line)
print(f"\n🎯 Fit Score: {fit_percentage:.1f}%")
if fit_percentage >= 80:
    print("✅ Strong value proposition fit.")
elif fit_percentage >= 50:
    print("⚠️ Partial fit. Consider improving alignment.")
else:
    print("❌ Weak fit. Your offering may not address key user needs.")

print("\n🎭 Generated Persona:")
for key, value in persona.items():
    print(f"- {key}: {value}")

# -------------------------------
# 5. Visualization (Fit Score)
# -------------------------------
labels = ['Addressed', 'Not Addressed']
values = [fit_percentage, 100 - fit_percentage]
colors = ['#4CAF50', '#F44336']

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Value Proposition Fit Score')
plt.tight_layout()
plt.show()

# -------------------------------
# 6. AI Suggestions
# -------------------------------
def suggest_features(unmatched_pains, unmatched_gains):
    suggestions = []

    for pain in unmatched_pains:
        suggestions.append(f"💡 To relieve pain '{pain.strip()}', consider automation, customer support, or tutorials.")

    for gain in unmatched_gains:
        suggestions.append(f"🚀 To create gain '{gain.strip()}', consider loyalty programs, seamless UX, or faster delivery.")

    return suggestions

# Identify unmatched pains/gains
unmatched_pains = [p for p in customer_pains if not any(p.lower().strip() in rel.lower() for rel in pain_relievers)]
unmatched_gains = [g for g in customer_gains if not any(g.lower().strip() in creator.lower() for creator in gain_creators)]

# Generate Suggestions
ai_suggestions = suggest_features(unmatched_pains, unmatched_gains)

# Print Suggestions
print("\n🤖 AI-Powered Feature Suggestions:")
if ai_suggestions:
    for idea in ai_suggestions:
        print(f"- {idea}")
else:
    print("✅ No additional suggestions — great fit!")