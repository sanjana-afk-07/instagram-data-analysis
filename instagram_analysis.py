# 📊 Instagram Data Analysis – Readme Brand

# ===============================
# 1. IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 2. LOAD DATASET
# ===============================
df = pd.read_csv("instagram_data.csv")  # change file name if needed

print("\n🔹 First 5 rows:")
print(df.head())

# ===============================
# 3. BASIC INFO
# ===============================
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Statistical Summary:")
print(df.describe())

# ===============================
# 4. MISSING VALUES
# ===============================
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# ===============================
# 5. DATA CLEANING
# ===============================
df = df.dropna()
df = df.drop_duplicates()

print("\n🔹 After Cleaning:")
print(df.shape)

# ===============================
# 6. COLUMN CHECK
# ===============================
print("\n🔹 Columns:")
print(df.columns)

# ===============================
# 7. TOP POSTS BY LIKES
# ===============================
if "likes" in df.columns:
    top_posts = df.sort_values(by="likes", ascending=False).head(10)
    print("\n🔹 Top 10 Posts by Likes:")
    print(top_posts)

    plt.figure(figsize=(10,5))
    sns.barplot(x=top_posts["likes"], y=top_posts.index)
    plt.title("Top 10 Instagram Posts by Likes (Realme)")
    plt.xlabel("Likes")
    plt.ylabel("Post Index")
    plt.show()

# ===============================
# 8. ENGAGEMENT ANALYSIS
# ===============================
if "likes" in df.columns and "comments" in df.columns:
    df["engagement"] = df["likes"] + df["comments"]

    print("\n🔹 Engagement Data:")
    print(df[["likes", "comments", "engagement"]].head())

    plt.figure(figsize=(10,5))
    sns.lineplot(data=df["engagement"])
    plt.title("Engagement Trend (Realme Instagram Data)")
    plt.show()

# ===============================
# 9. CORRELATION HEATMAP
# ===============================
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ===============================
# 10. TOP HASHTAGS (IF EXISTS)
# ===============================
if "hashtags" in df.columns:
    print("\n🔹 Top Hashtags:")
    print(df["hashtags"].value_counts().head(10))

# ===============================
# 11. FINAL MESSAGE
# ===============================
print("\n✅ Instagram Data Analysis Completed Successfully!")
