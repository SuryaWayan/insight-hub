# insight-hub

Develop a Python-based web application using Streamlit tailored for data analysts to effortlessly visualize and analyze CSV data. Ensure the application offers a seamless user experience with clear instructions at each step. The goal is to empower users to explore and understand their data effectively.

Key Features:

CSV Upload: Implement a button to allow users to upload CSV files seamlessly. Upon upload, display a confirmation message and allow users to proceed to the next steps.

Data Overview: Provide a summary of the uploaded CSV data, including the total number of rows and columns. This summary should give users an initial understanding of the dataset's size and structure.

Column List: Present a list of all column names in the uploaded dataset. This feature assists users in identifying and selecting specific columns for further analysis.

Interactive Table Generation: Before displaying the table, enable users to select the columns they wish to include and specify the number of rows to be shown. This interactive feature enhances user control and ensures focused data exploration.

Dynamic Chart Generation: Offer a variety of visually appealing charts for data visualization. Allow users to configure up to 10 different charts vertically. Users should be able to specify the X and Y axes from the available columns in the dataset. Additionally, support multiple columns for the Y axis to enable comprehensive data comparison. Ensure that when users do not specify any configuration, the charts gracefully handle the absence of data.

Chart Customization: Provide options for users to customize the appearance of charts, such as adjusting colors, labels, and titles. This feature enhances the flexibility of data visualization to suit individual preferences and presentation needs.

Export and Share: Enable users to export generated charts in various formats (e.g., PNG, PDF) and share them seamlessly with colleagues or stakeholders. This functionality facilitates collaboration and communication based on insights derived from the data.

Data Filtering and Sorting: Implement advanced filtering and sorting options for the displayed table to enable users to focus on specific subsets of data efficiently. This feature enhances data exploration and analysis capabilities.

Interactive User Guide: Incorporate an interactive user guide or tutorial within the application to assist users in navigating through different features and functionalities. This guide should offer step-by-step instructions, tooltips, and examples to enhance user proficiency and confidence.

Responsive Design: Ensure that the web application is responsive across various devices and screen sizes, providing a consistent and optimized user experience regardless of the platform used.

Additional Features:

X-Axis Variation: For each chart, enable users to vary the X-axis using a slicer-like feature. This functionality allows for dynamic exploration and comparison across different variables.

Trend Analysis: Provide users with the option to add trends (linear, exponential, polynomial, etc.) to each chart. This feature enhances data interpretation by highlighting patterns and relationships within the dataset.

By integrating these features, the Python-based web application will empower data analysts to explore, visualize, and derive insights from their CSV data efficiently and effectively.

## Collaborate with GPT Engineer

This is a [gptengineer.app](https://gptengineer.app)-synced repository 🌟🤖

Changes made via gptengineer.app will be committed to this repo.

If you clone this repo and push changes, you will have them reflected in the GPT Engineer UI.

## Setup

```sh
git clone https://github.com/GPT-Engineer-App/insight-hub.git
cd insight-hub
npm i
```

```sh
npm run dev
```

This will run a dev server with auto reloading and an instant preview.

## Tech stack

- [Vite](https://vitejs.dev/)
- [React](https://react.dev/)
- [Chakra UI](https://chakra-ui.com/)

## Requirements

- Node.js & npm - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
