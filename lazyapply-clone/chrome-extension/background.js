chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  let jobLink = request.jobLink;

  fetch(`http://localhost:5000/runbot?link=${encodeURIComponent(jobLink)}`)
    .then(res => res.json())
    .then(data => {
      sendResponse({ status: data.status });
    });

  return true; // Allows async response
});