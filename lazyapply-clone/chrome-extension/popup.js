// This runs when "Apply Now" is clicked
document.getElementById("applyBtn").addEventListener("click", () => {
  const link = document.getElementById("jobLink").value;

  // Send the link to the background script
  chrome.runtime.sendMessage({ jobLink: link });
});
