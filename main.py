import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
 
# ── Global Style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#0d1117',
    'axes.facecolor':   '#161b22',
    'axes.edgecolor':   '#30363d',
    'axes.labelcolor':  '#c9d1d9',
    'xtick.color':      '#8b949e',
    'ytick.color':      '#8b949e',
    'text.color':       '#c9d1d9',
    'grid.color':       '#21262d',
    'grid.linestyle':   '--',
    'grid.alpha':       0.5,
    'font.family':      'DejaVu Sans',
    'axes.titlesize':   14,
    'axes.titleweight': 'bold',
    'axes.titlepad':    14,
    'axes.labelsize':   11,
})
 
IPL_PALETTE   = ['#ff6b35', '#f7c59f', '#efefd0', '#004e89', '#1a936f',
                 '#88d498', '#c6dabf', '#ff9f1c', '#e71d36', '#2ec4b6']
ACCENT_ORANGE = '#ff6b35'
ACCENT_BLUE   = '#1a78c2'
 
# ── Load Data ────────────────────────────────────────────────────────────────
df = pd.read_csv('ipl.csv')

print(f"  IPL 2022 Dataset — {df.shape[0]} rows × {df.shape[1]} columns")
print(df.head())
print()
print(df.info())
print()
print("Missing values:\n", df.isnull().sum())
 
 
# ── 1. Most Match Wins by Team ────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
winner = df['match_winner'].value_counts()
 
bars = ax.barh(winner.index, winner.values, color=IPL_PALETTE[:len(winner)],
               edgecolor='none', height=0.65)
 
for bar, val in zip(bars, winner.values):
    ax.text(val + 0.15, bar.get_y() + bar.get_height() / 2,
            str(val), va='center', color='#c9d1d9', fontsize=10)
 
ax.set_title('Most Match Wins by Team — IPL 2022', color='#ffffff')
ax.set_xlabel('Matches Won')
ax.set_ylabel('')
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(0, winner.values.max() + 2)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('1_match_wins.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
 
 
# ── 2. Toss Decision Distribution ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
toss_counts = df['toss_decision'].value_counts()
colors = [ACCENT_ORANGE, ACCENT_BLUE]
 
bars = ax.bar(toss_counts.index, toss_counts.values, color=colors,
              edgecolor='none', width=0.45)
 
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            str(bar.get_height()), ha='center', fontsize=11, color='#c9d1d9')
 
ax.set_title('Toss Decision — Field vs Bat', color='#ffffff')
ax.set_xlabel('Toss Decision')
ax.set_ylabel('Count')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('2_toss_decision.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
 
 
# ── 3. Toss Winner = Match Winner? ───────────────────────────────────────────
toss_wins   = (df['toss_winner'] == df['match_winner']).sum()
toss_losses = len(df) - toss_wins
labels  = ['Won toss + match', 'Won toss, lost match']
sizes   = [toss_wins, toss_losses]
colors  = [ACCENT_ORANGE, '#30363d']
 
fig, ax = plt.subplots(figsize=(6, 5))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%',
    colors=colors, startangle=90,
    wedgeprops=dict(edgecolor='#0d1117', linewidth=2),
    textprops=dict(color='#c9d1d9')
)
for at in autotexts:
    at.set_fontsize(11)
    at.set_color('#ffffff')
 
ax.set_title('Does Winning the Toss Help?\n(IPL 2022)', color='#ffffff')
plt.tight_layout()
plt.savefig('3_toss_advantage.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
print(f"\nToss winner = Match winner: {toss_wins}/{len(df)} matches ({toss_wins/len(df)*100:.1f}%)")
 
 
# ── 4. How Teams Win — Runs vs Wickets ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 5))
won_by = df['won_by'].value_counts()
colors = [ACCENT_ORANGE if 'run' in str(v).lower() else ACCENT_BLUE for v in won_by.index]
 
bars = ax.bar(won_by.index, won_by.values, color=colors, edgecolor='none', width=0.45)
 
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            str(bar.get_height()), ha='center', fontsize=11, color='#c9d1d9')
 
ax.set_title('How Teams Win — Runs vs Wickets', color='#ffffff')
ax.set_xlabel('Win Type')
ax.set_ylabel('Count')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('4_win_type.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
 
 
# ── 5. Top 10 Player of the Match Awards ────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
potm = df['player_of_the_match'].value_counts().head(10)
 
bars = ax.barh(potm.index[::-1], potm.values[::-1],
               color=sns.color_palette('flare', 10)[::-1],
               edgecolor='none', height=0.65)
 
for bar, val in zip(bars, potm.values[::-1]):
    ax.text(val + 0.05, bar.get_y() + bar.get_height() / 2,
            str(val), va='center', fontsize=10, color='#c9d1d9')
 
ax.set_title('Top 10 Player of the Match — IPL 2022', color='#ffffff')
ax.set_xlabel('Awards')
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(0, potm.values.max() + 1.5)
plt.tight_layout()
plt.savefig('5_potm.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
 
 
# ── 6. Top 2 High Scorers ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
high = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)
 
colors = [ACCENT_ORANGE, ACCENT_BLUE]
bars = ax.barh(high.index, high.values, color=colors, edgecolor='none', height=0.4)
 
for bar, val in zip(bars, high.values):
    ax.text(val + 1, bar.get_y() + bar.get_height() / 2,
            str(val), va='center', fontsize=11, color='#c9d1d9')
 
ax.set_title('Top 2 High Scorers — IPL 2022', color='#ffffff')
ax.set_xlabel('Total Runs')
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(0, high.values.max() + 50)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('6_top_scorers.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
 
print("\nAnalysis complete! All plots saved.")