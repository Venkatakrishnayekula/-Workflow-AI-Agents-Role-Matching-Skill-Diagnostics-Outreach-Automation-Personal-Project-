const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.onresult = function(event) {
  const command = event.results[0][0].transcript;
  if (command.includes("apply")) {
    chrome.runtime.sendMessage({ action: "startApply" });
  }
};
recognition.start();