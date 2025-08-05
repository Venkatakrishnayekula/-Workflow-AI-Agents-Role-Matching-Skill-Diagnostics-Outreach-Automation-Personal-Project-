const highlightFields = () => {
  document.querySelectorAll("input, textarea, select").forEach(el => {
    el.style.border = "2px solid orange";
  });
};
highlightFields();