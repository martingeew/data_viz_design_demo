import morethemes as mt
import matplotlib.pyplot as plt
import pandas as pd
from pyfonts import load_font
from highlight_text import ax_text

mt.set_theme("minimal")

# Load US CPI quarterly data from GitHub
cpi_data = pd.read_csv(
    "https://raw.githubusercontent.com/martingeew/data_viz_design_demo/main/data/us_cpi_quarterly.csv",
    parse_dates=["date"],
    index_col="date",
)

# Load stylish fonts using pyfonts

title_font = load_font(
    "https://github.com/google/fonts/blob/main/ofl/cabincondensed/CabinCondensed-SemiBold.ttf?raw=true"
)
subtitle_font = load_font(
    "https://github.com/google/fonts/blob/main/ofl/cabincondensed/CabinCondensed-Regular.ttf?raw=true"
)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot CPI data as a line chart
ax.plot(
    cpi_data.index, cpi_data["value"] * 100, color="#2E86AB", linewidth=2.5, alpha=0.9
)

# Customize the plot
ax.tick_params(axis="both", which="major", labelsize=12.5)  # 25% larger tick labels
ax.grid(True, alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Find min and max values for annotations
min_idx = cpi_data["value"].idxmin()
max_idx = cpi_data["value"].idxmax()
min_value = cpi_data["value"].min() * 100  # Convert to percentage
max_value = cpi_data["value"].max() * 100  # Convert to percentage

# Extract quarter information
min_quarter = f"{min_idx.year}Q{min_idx.quarter}"
max_quarter = f"{max_idx.year}Q{max_idx.quarter}"

# Add marker points for min and max values
ax.scatter(min_idx, min_value, color="#D32F2F", s=100, zorder=5)  # GFC marker (red)
ax.scatter(
    max_idx, max_value, color="#FF5722", s=100, zorder=5
)  # Covid marker (orange)

# Add highlighted annotations using highlight_text
# Min value annotation (GFC)
ax_text(
    x=pd.Timestamp("2008-01-01"),  # Position to the left of min point
    y=min_value + 0.5,  # Position above the point
    s=f"<{min_quarter}> <(GFC):> {min_value:.1f}%",
    highlight_textprops=[
        {"color": "#D32F2F", "weight": "bold", "font": title_font},
        {"color": "#D32F2F", "weight": "bold", "font": title_font},
    ],
    color="#666666",  # Similar to tick mark color
    fontsize=16.5,  # 50% bigger
    font=subtitle_font,
    ha="right",  # Right-align so text flows towards the point
    va="bottom",
    ax=ax,
)

# Max value annotation (Covid)
ax_text(
    x=max_idx,
    y=max_value + 0.3,  # Position closer to the point
    s=f"<{max_quarter}> <(Covid):> {max_value:.1f}%",
    highlight_textprops=[
        {"color": "#FF5722", "weight": "bold", "font": title_font},
        {"color": "#FF5722", "weight": "bold", "font": title_font},
    ],
    color="#666666",  # Similar to tick mark color
    fontsize=16.5,  # 50% bigger
    font=subtitle_font,
    ha="center",
    va="bottom",
    ax=ax,
)

# Add stylish title using custom font
fig.text(
    0.05,
    0.95,
    "Consumer Price Index: Total for United States",
    fontsize=30,
    font=title_font,
    weight="bold",
    color="#2C3E50",
)

# Add subtitle using different font
fig.text(
    0.05,
    0.90,
    "Growth rate same period previous year, Quarterly, Not Seasonally Adjusted",
    fontsize=17.5,
    font=subtitle_font,
    color="#7F8C8D",
)

# Add source attribution
fig.text(
    0.95,
    0.02,
    "Source: FRED",
    fontsize=12.5,
    font=subtitle_font,
    color="#95A5A6",
    ha="right",
)

# Improve layout
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.1)

# Display the plot
plt.show()
