// Get the file name of the current PDF document
fn = documentFileName;
// Replace the file name PDF extension with the FDF extension
fn = fn.replace(/\.pdf/i, ".fdf");

// Import the FDF file
importAnFDF(fn);

// Flatten the page to finalize the form contents and disable editing
flattenPages();
