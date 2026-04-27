import json

file_path = 'summary_statistics.ipynb'
with open(file_path, 'r') as f:
    nb = json.load(f)

new_cells = [
    {
        "cell_type": "markdown",
        "id": "scatter_plot_header",
        "metadata": {},
        "source": [
            "## Scatter Plot: Output Voltage vs Light Intensity\n",
            "\n",
            "Generate a scatter plot to visualize the relationship between light intensity and output voltage, colored by panel type."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "scatter_plot_code",
        "metadata": {},
        "outputs": [],
        "source": [
            "import seaborn as sns\n",
            "\n",
            "plt.figure(figsize=(10, 6))\n",
            "sns.scatterplot(data=df, x='Light Intensity', y='Output Voltage', hue='PanelType', style='PanelType', s=100)\n",
            "\n",
            "plt.title('Output Voltage vs Light Intensity', fontsize=14)\n",
            "plt.xlabel('Light Intensity (W/m²)', fontsize=12)\n",
            "plt.ylabel('Output Voltage (V)', fontsize=12)\n",
            "plt.grid(True, linestyle='--', alpha=0.6)\n",
            "plt.legend(title='Panel Type')\n",
            "plt.show()"
        ]
    }
]

nb['cells'].extend(new_cells)

with open(file_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Cells added successfully.")
