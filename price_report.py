def adjust_price(predicted_price, release_year, days_used, current_year=2024):
    # Depreciation rates
    yearly_depreciation_rate = 0.10  # 10% per year
    daily_depreciation_rate = 0.0002  # 0.02% per day

    # Calculate the age of the phone
    age_in_years = current_year - release_year

    # Calculate the depreciation factors
    year_depreciation = 1 - (age_in_years * yearly_depreciation_rate)
    day_depreciation = 1 - (days_used * daily_depreciation_rate)

    # Adjust the predicted price
    adjusted_price = predicted_price * year_depreciation * day_depreciation

    # Ensure the price doesn't go below a minimum threshold
    return max(10000, adjusted_price)


def pricereport(model, batcap, ss, sto, ram, c1, c2, c3, c4, c5, release_year, days_used):
    import matplotlib.pyplot as plt
    import numpy as np
    # import pickle
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)

    # Load the trained model
    # with open('model.pickle', 'rb') as f:
    #     model = pickle.load(f)

    # Feature importance from the model
    feature_importances = model.feature_importances_
    feature_names = ['battery', 'screen_size', 'storage', 'ram', 'cam1', 'cam2', 'cam3', 'cam4', 'cam5']

    # Smartphone features for the given device
    smartphone_features = np.array([batcap, ss, sto, ram, c1, c2, c3, c4, c5])

    # Calculate contributions based on feature importance
    contribution = feature_importances * smartphone_features
    contribution_normalized = contribution / np.sum(contribution)

    # Create a figure with two subplots: one for the pie chart, one for the text
    fig, axs = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1]})

    # Plot pie chart of feature importance in the left subplot
    axs[0].pie(feature_importances, labels=feature_names, autopct='%1.1f%%', startangle=140)
    axs[0].set_title('Feature Importances')

    # Predict the price for the given smartphone features
    predicted_price = model.predict([[batcap, ss, sto, ram, c1, c2, c3, c4, c5]])[0]

    # Calculate the price contribution for each feature
    feature_price_contribution = feature_importances * predicted_price

    # Sort features based on their contribution
    sorted_contribution = sorted(zip(feature_names, feature_price_contribution), key=lambda x: x[1], reverse=True)

    # Display the price contribution on the right subplot
    axs[1].axis('off')  # Turn off the axis for the text plot
    axs[1].text(0, 1, 'Price Contribution by Feature (in descending order):', fontsize=12, weight='bold')

    y_offset = 0.9  # Starting y position for the text display
    for feature, contribution in sorted_contribution:
        axs[1].text(0, y_offset, f"{feature}: {contribution:.2f}", fontsize=10)
        y_offset -= 0.05  # Move down for the next line of text

    # Adjust the price based on release year and days used
    adjusted_price = adjust_price(predicted_price, release_year, days_used)

    # Print the depreciation due to the release year and number of days used
    year_depreciation = (2024 - release_year) * 0.10  # 10% depreciation per year
    days_depreciation = days_used * 0.0002  # 0.02% depreciation per day
    total_depreciation = predicted_price * (year_depreciation + days_depreciation)

    # Display depreciation and final adjusted price
    axs[1].text(0, y_offset - 0.05, f"\nDepreciation due to age: -{total_depreciation:.2f}", fontsize=10, color='red')
    axs[1].text(0, y_offset - 0.10, f"\nFinal Adjusted Price: {adjusted_price:.2f}", fontsize=12, color='blue')

    # Print the final predicted price
    axs[1].text(0, y_offset - 0.15, f"\nPredicted Price (Before Depreciation): {predicted_price:.2f}", fontsize=12, color='green')

    # Adjust layout and display the figure
    plt.tight_layout()
    plt.show()


# pricereport(5000, 6.7, 128, 8, 50, 48, 32, 0, 0, 2023, 160)


