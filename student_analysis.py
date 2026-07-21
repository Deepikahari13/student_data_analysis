import pandas as pd
df = pd.read_csv("student_data.csv")
df.columns = df.columns.str.strip()
print("Student Data:")
print(df)
df["Average"] = (df["Maths"] + 
df["Science"] + df["English"]) / 3
print("\nAverage marks:")
print(df[["Student","Average"]])
print("\nTopper:")
print(df.loc[df["Average"].idxmax()])
print("\nLowest Scorer:")
print(df.loc[df["Average"].idxmin()])
import matplotlib.pyplot as plt
plt.bar(df["Student"], df["Average"])
plt.title("Stdent Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()


