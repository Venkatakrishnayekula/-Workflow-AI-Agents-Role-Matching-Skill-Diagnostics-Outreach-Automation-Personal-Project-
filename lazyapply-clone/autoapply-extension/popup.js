document.getElementById("apply").addEventListener("click", () => {
  chrome.runtime.sendMessage({ action: "startApply" });
});
document.getElementById("toggleVoice").addEventListener("click", () => {
  chrome.runtime.sendMessage({ action: "toggleVoiceMode" });
});