import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

ambang_batas = 35

print("=== MONITORING KUALITAS UDARA ===")
print(data.to_string(index=False))

rata_rata = data["pm25"].mean()
print(f"\nRata-rata PM2.5: {rata_rata:.2f}")

if data["pm25"].max() > ambang_batas:
    print("Peringatan: PM2.5 melewati ambang simulasi!")
else:
    print("Kualitas udara di bawah ambang simulasi.")

plt.plot(data["waktu"], data["pm25"], marker="o")
plt.axhline(
    y=ambang_batas,
    linestyle="--",
    label="Ambang simulasi"
)

plt.title("Monitoring Kualitas Udara PM2.5")
plt.xlabel("Waktu")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()