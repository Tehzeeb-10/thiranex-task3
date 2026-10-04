import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# TASK 3 - EDA : ALL GRAPHS IN 4 x 4
# ==========================================

# Load cleaned dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Fix country name capitalization
df["Country"] = df["Country"].str.strip().str.title()

# Create output folder
if not os.path.exists("EDA_Graphs"):
    os.mkdir("EDA_Graphs")

# ==========================================
# CALCULATIONS
# ==========================================

item_counts = df["Items Purchased"].value_counts()

item_avg = df.groupby(
    "Items Purchased"
)["Purchase Amount"].mean()

season_avg = df.groupby(
    "Season"
)["Purchase Amount"].mean()

subscription_avg = df.groupby(
    "Subscription Status"
)["Purchase Amount"].mean()

category_avg = df.groupby(
    "Category"
)["Purchase Amount"].mean()

gender_avg = df.groupby(
    "Gender"
)["Purchase Amount"].mean()

shipping_avg = df.groupby(
    "Shipping Type"
)["Purchase Amount"].mean()

profession_avg = df.groupby(
    "Profession"
)["Purchase Amount"].mean()

country_avg = df.groupby(
    "Country"
)["Purchase Amount"].mean().sort_values(
    ascending=False
)

numeric_columns = df.select_dtypes(
    include="number"
)

correlation = numeric_columns.corr()

age_correlation = df["Age"].corr(
    df["Purchase Amount"]
)

# ==========================================
# CREATE 4 x 4 FIGURE
# ==========================================

fig, axes = plt.subplots(
    4,
    4,
    figsize=(20, 18)
)

# ==========================================
# GRAPH 1 - PURCHASE AMOUNT DISTRIBUTION
# ==========================================

axes[0, 0].hist(
    df["Purchase Amount"],
    bins=20
)

axes[0, 0].set_title(
    "Purchase Amount Distribution"
)

axes[0, 0].set_xlabel(
    "Purchase Amount"
)

axes[0, 0].set_ylabel(
    "Customers"
)

# ==========================================
# GRAPH 2 - ITEM TYPE DISTRIBUTION
# ==========================================

item_counts.plot(
    kind="bar",
    ax=axes[0, 1]
)

axes[0, 1].set_title(
    "Purchased Item Types"
)

axes[0, 1].set_xlabel(
    "Item Type"
)

axes[0, 1].set_ylabel(
    "Customers"
)

axes[0, 1].tick_params(
    axis="x",
    rotation=45
)

# ==========================================
# GRAPH 3 - ITEM TYPE vs PURCHASE
# ==========================================

item_avg.plot(
    kind="bar",
    ax=axes[0, 2]
)

axes[0, 2].set_title(
    "Average Purchase by Item Type"
)

axes[0, 2].set_xlabel(
    "Item Type"
)

axes[0, 2].set_ylabel(
    "Average Purchase"
)

axes[0, 2].tick_params(
    axis="x",
    rotation=45
)

# ==========================================
# GRAPH 4 - SEASON
# ==========================================

season_avg.plot(
    kind="bar",
    ax=axes[0, 3]
)

axes[0, 3].set_title(
    "Average Purchase by Season"
)

axes[0, 3].set_xlabel(
    "Season"
)

axes[0, 3].set_ylabel(
    "Average Purchase"
)

axes[0, 3].tick_params(
    axis="x",
    rotation=0
)

# ==========================================
# GRAPH 5 - SUBSCRIPTION
# ==========================================

subscription_avg.plot(
    kind="bar",
    ax=axes[1, 0]
)

axes[1, 0].set_title(
    "Average Purchase by Subscription"
)

axes[1, 0].set_xlabel(
    "Subscription Status"
)

axes[1, 0].set_ylabel(
    "Average Purchase"
)

axes[1, 0].tick_params(
    axis="x",
    rotation=0
)

# ==========================================
# GRAPH 6 - CATEGORY
# ==========================================

category_avg.plot(
    kind="bar",
    ax=axes[1, 1]
)

axes[1, 1].set_title(
    "Average Purchase by Category"
)

axes[1, 1].set_xlabel(
    "Category"
)

axes[1, 1].set_ylabel(
    "Average Purchase"
)

axes[1, 1].tick_params(
    axis="x",
    rotation=30
)

# ==========================================
# GRAPH 7 - GENDER
# ==========================================

gender_avg.plot(
    kind="bar",
    ax=axes[1, 2]
)

axes[1, 2].set_title(
    "Average Purchase by Gender"
)

axes[1, 2].set_xlabel(
    "Gender"
)

axes[1, 2].set_ylabel(
    "Average Purchase"
)

axes[1, 2].tick_params(
    axis="x",
    rotation=0
)

# ==========================================
# GRAPH 8 - SHIPPING TYPE
# ==========================================

shipping_avg.plot(
    kind="bar",
    ax=axes[1, 3]
)

axes[1, 3].set_title(
    "Average Purchase by Shipping Type"
)

axes[1, 3].set_xlabel(
    "Shipping Type"
)

axes[1, 3].set_ylabel(
    "Average Purchase"
)

axes[1, 3].tick_params(
    axis="x",
    rotation=45
)

# ==========================================
# GRAPH 9 - PROFESSION
# ==========================================

profession_avg.plot(
    kind="bar",
    ax=axes[2, 0]
)

axes[2, 0].set_title(
    "Average Purchase by Profession"
)

axes[2, 0].set_xlabel(
    "Profession"
)

axes[2, 0].set_ylabel(
    "Average Purchase"
)

axes[2, 0].tick_params(
    axis="x",
    rotation=45
)

# ==========================================
# GRAPH 10 - COUNTRY
# ==========================================

country_avg.plot(
    kind="bar",
    ax=axes[2, 1]
)

axes[2, 1].set_title(
    "Average Purchase by Country"
)

axes[2, 1].set_xlabel(
    "Country"
)

axes[2, 1].set_ylabel(
    "Average Purchase"
)

axes[2, 1].tick_params(
    axis="x",
    rotation=60
)

# ==========================================
# GRAPH 11 - AGE DISTRIBUTION
# ==========================================

axes[2, 2].hist(
    df["Age"],
    bins=15
)

axes[2, 2].set_title(
    "Age Distribution"
)

axes[2, 2].set_xlabel(
    "Age"
)

axes[2, 2].set_ylabel(
    "Customers"
)

# ==========================================
# GRAPH 12 - AGE vs PURCHASE
# ==========================================

axes[2, 3].scatter(
    df["Age"],
    df["Purchase Amount"]
)

axes[2, 3].set_title(
    "Age vs Purchase Amount"
)

axes[2, 3].set_xlabel(
    "Age"
)

axes[2, 3].set_ylabel(
    "Purchase Amount"
)

# ==========================================
# GRAPH 13 - CORRELATION HEATMAP
# ==========================================

axes[3, 0].imshow(
    correlation,
    cmap="coolwarm",
    interpolation="nearest"
)

axes[3, 0].set_title(
    "Numerical Correlation Heatmap"
)

axes[3, 0].set_xticks(
    range(len(correlation.columns))
)

axes[3, 0].set_xticklabels(
    correlation.columns,
    rotation=90
)

axes[3, 0].set_yticks(
    range(len(correlation.columns))
)

axes[3, 0].set_yticklabels(
    correlation.columns
)

# ==========================================
# GRAPH 14 - PURCHASE AMOUNT BOXPLOT
# ==========================================

axes[3, 1].boxplot(
    df["Purchase Amount"]
)

axes[3, 1].set_title(
    "Purchase Amount Boxplot"
)

axes[3, 1].set_ylabel(
    "Purchase Amount"
)

# ==========================================
# GRAPH 15 - AGE BOXPLOT
# ==========================================

axes[3, 2].boxplot(
    df["Age"]
)

axes[3, 2].set_title(
    "Age Boxplot"
)

axes[3, 2].set_ylabel(
    "Age"
)

# ==========================================
# GRAPH 16 - HIGHEST CATEGORY SUMMARY
# ==========================================

axes[3, 3].bar(
    ["Highest Item", "Highest Category", "Highest Season"],
    [
        item_avg.max(),
        category_avg.max(),
        season_avg.max()
    ]
)

axes[3, 3].set_title(
    "Highest Average Purchase Values"
)

axes[3, 3].set_ylabel(
    "Average Purchase Amount"
)

axes[3, 3].tick_params(
    axis="x",
    rotation=30
)

# ==========================================
# FINAL LAYOUT
# ==========================================

fig.suptitle(
    "Customer Shopping Dataset - Exploratory Data Analysis",
    fontsize=20
)

plt.tight_layout(
    rect=[0, 0, 1, 0.97]
)

# Save ONE combined graph
plt.savefig(
    "EDA_Graphs/EDA_All_Graphs_4x4.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# PRINT RESULTS
# ==========================================

print("\n==========================================")
print("       EDA COMPLETED SUCCESSFULLY")
print("==========================================")

print("\nDataset Shape:", df.shape)

print(
    "\nAverage Purchase Amount:",
    round(df["Purchase Amount"].mean(), 2)
)

print(
    "\nHighest Item Type:",
    item_avg.idxmax(),
    "=",
    round(item_avg.max(), 2)
)

print(
    "\nLowest Item Type:",
    item_avg.idxmin(),
    "=",
    round(item_avg.min(), 2)
)

print(
    "\nHighest Season:",
    season_avg.idxmax(),
    "=",
    round(season_avg.max(), 2)
)

print(
    "\nHighest Category:",
    category_avg.idxmax(),
    "=",
    round(category_avg.max(), 2)
)

print(
    "\nHighest Subscription:",
    subscription_avg.idxmax(),
    "=",
    round(subscription_avg.max(), 2)
)

print(
    "\nAge-Purchase Correlation:",
    round(age_correlation, 4)
)

print(
    "\nAll 16 EDA panels saved as ONE 4x4 figure:"
)

print(
    "EDA_Graphs/EDA_All_Graphs_4x4.png"
)
